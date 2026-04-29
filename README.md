# GlucoseResponseModelingOralGlucoseIntake
This project models the plasma glucose response after an Oral Glucose Tolerance Test (OGTT) using a bi-exponential model.
The goal is to:
Estimate patient-specific kinetic parameters
Simulate glucose concentration curves
Extract clinically relevant indicators
Identify potential glucose intolerance conditions

## Mathematical Model
The glucose variation from baseline is modeled as:
BGP(t) = A * (exp(-at) - exp(-bt))
Where:
A (mg/dL): amplitude
a, b (h⁻¹): kinetic parameters
BGP(t): glucose variation from baseline
Total glucose concentration:
Glucose(t) = Baseline + BGP(t)


## Dataset
50 patients
10 time points per patient
Measurements: plasma glucose concentration (mg/dL)

## Methods
Parameter Estimation
Nonlinear least squares fitting is performed using:
scipy.optimize.curve_fit
Simulation
Each patient curve is simulated over 100 time points.
Extracted Features
For each patient:
Area Under Curve (AUC)
Maximum glucose value (Cmax)
Time to peak (Tmax)
Return time to within +5% of baseline
Diagnosis Criteria
A patient is flagged as "Glucose Intolerant" if:
Baseline glucose > 110 mg/dL
OR
Peak glucose > 250 mg/dL

Tech Stack
Matlab
Python
NumPy
SciPy
Matplotlib

Project Structure
glucose-modeling/
│
├── data/
│   └── glucose_data.txt
├── main.py
├── model.py
├── analysis.py
└── README.md

Martina Misiano
