import numpy as np

def compute_rmse(gluc, baseline, t, A, a, b):
    pred = baseline + A * (np.exp(-a*t) - np.exp(-b*t))
    return np.sqrt(np.mean((gluc - pred)**2))

def compute_metrics(t, gluc, baseline):
    AUC = np.trapz(gluc, t)
    Cmax = np.max(gluc)
    Tmax = t[np.argmax(gluc)]

    threshold = baseline * 1.05
    idx = np.where((gluc <= threshold) & (t > Tmax))[0]
    T_return = t[idx[0]] if len(idx) > 0 else np.nan

    return AUC, Cmax, Tmax, T_return
