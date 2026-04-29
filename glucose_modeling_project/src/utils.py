def diagnose(baseline, Cmax):
    return "Intolerant" if baseline > 110 or Cmax > 250 else "Normal"
