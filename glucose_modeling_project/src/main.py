import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

from model import model
from metrics import compute_metrics, compute_rmse
from utils import diagnose

os.makedirs("../plots", exist_ok=True)

# Load data
data = pd.read_csv("../data/glucosio_ospedale_1.txt", delim_whitespace=True)
data.columns = ["patient", "time", "glucose"]

patients = data["patient"].unique()
results = []

for p in patients:
    subset = data[data["patient"] == p]

    t = subset["time"].values
    gluc = subset["glucose"].values

    baseline = gluc[0]
    BGP = gluc - baseline

    try:
        popt, _ = curve_fit(model, t, BGP, p0=[100,1,0.1], bounds=(0, np.inf))
    except:
        continue

    A, a, b = popt
    rmse = compute_rmse(gluc, baseline, t, A, a, b)

    t_sim = np.linspace(0,5,100)
    gluc_sim = baseline + model(t_sim, A, a, b)

    AUC, Cmax, Tmax, T_return = compute_metrics(t_sim, gluc_sim, baseline)
    diagnosis = diagnose(baseline, Cmax)

    results.append([p, A, a, b, AUC, Cmax, Tmax, T_return, rmse, diagnosis])

    if p <= 3:
        plt.figure()
        plt.scatter(t, gluc, label="Data")
        plt.plot(t_sim, gluc_sim, label="Fit")
        plt.legend()
        plt.savefig(f"../plots/patient_{p}.png")
        plt.close()

columns = ["Patient","A","a","b","AUC","Cmax","Tmax","T_return","RMSE","Diagnosis"]
df = pd.DataFrame(results, columns=columns)

plt.figure()
plt.hist(df["AUC"], bins=15)
plt.savefig("../plots/auc_distribution.png")
plt.close()

df.to_csv("../results/results.csv", index=False)
print(df.head())
