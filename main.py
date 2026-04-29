import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
os.makedirs("plots", exist_ok=True)
# ======================
# MODELLO
# ======================
def model(t, A, a, b):
    return A * (np.exp(-a*t) - np.exp(-b*t))

# ======================
# CARICAMENTO DATI
# ======================
data = pd.read_csv("glucosio_ospedale_1.txt", delim_whitespace=True)
data.columns = ["patient", "time", "glucose"]

patients = data["patient"].unique()

results = []

# ======================
# LOOP PAZIENTI
# ======================
for p in patients:
    
    subset = data[data["patient"] == p]
    
    t = subset["time"].values
    gluc = subset["glucose"].values
    
    baseline = gluc[0]
    BGP = gluc - baseline
    
    # ======================
    # FIT PARAMETRI
    # ======================
    p0 = [100, 1, 0.1]
    
    try:
        popt, _ = curve_fit(model, t, BGP, p0=p0, bounds=(0, np.inf))
    except:
        continue
    
    A, a, b = popt
    rmse = np.sqrt(np.mean((gluc - (baseline + model(t, A, a, b)))**2))
    
    # ======================
    # SIMULAZIONE
    # ======================
    t_sim = np.linspace(0, 5, 100)
    BGP_sim = model(t_sim, A, a, b)
    gluc_sim = baseline + BGP_sim
    
    # ======================
    # METRICHE
    # ======================
    AUC = np.trapz(gluc_sim, t_sim)
    
    Cmax = np.max(gluc_sim)
    Tmax = t_sim[np.argmax(gluc_sim)]
    
    threshold = baseline * 1.05
    
    after_peak = t_sim > Tmax
    idx = np.where((gluc_sim <= threshold) & after_peak)[0]
    
    T_return = t_sim[idx[0]] if len(idx) > 0 else np.nan
    
    # ======================
    # DIAGNOSI
    # ======================
    if baseline > 110 or Cmax > 250:
        diagnosis = "Intolerant"
    else:
        diagnosis = "Normal"
    
    results.append([p, A, a, b, AUC, Cmax, Tmax, T_return, rmse, diagnosis])
    
    # ======================
    # PLOT (solo primi 3 pazienti)
    # ======================
    if p <= 3:
        plt.figure()
        plt.scatter(t, gluc, label="Data")
        plt.plot(t_sim, gluc_sim, label="Fit")
        plt.xlabel("Time (h)")
        plt.ylabel("Glucose (mg/dL)")
        plt.title(f"Patient {p}")
        plt.legend()
        plt.savefig(f"plots/patient_{p}.png")
        plt.close()
        
# ======================
# RISULTATI
# ======================
columns = ["Patient", "A", "a", "b", "AUC", "Cmax", "Tmax", "T_return", "RMSE", "Diagnosis"]
df_results = pd.DataFrame(results, columns=columns)
plt.figure()
plt.hist(df_results["AUC"], bins=15)
plt.xlabel("AUC")
plt.ylabel("Frequency")
plt.title("AUC Distribution")
plt.savefig("plots/auc_distribution.png")
plt.close()

print(df_results.head())
df_results.to_csv("results.csv", index=False)

