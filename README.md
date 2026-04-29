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
Glucose Response Modeling (OGTT) – Parameter Estimation & Analysis

## Methods
Parameter Estimation
  Nonlinear least squares fitting is performed using:
  scipy.optimize.curve_fit
Simulation
  Each patient curve is simulated over 100 time points.
  Extracted Features
For each patient, the following metrics are computed:
 . Area Under Curve (AUC)
 . Maximum glucose value (Cmax)
 . Time to peak (Tmax)
 . Return time to within +5% of baseline
 . RMSE (model error) 
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

The model captures the rise and decay of glucose concentration after intake, showing good agreement with measured data.
The variability in AUC reflects inter-patient differences in glucose response.
The RMSE distribution shows that the model provides a consistent fit across patients.

## Project Structure


## Key Insights
Glucose response varies significantly between patients
The model captures the main physiological trend despite its simplicity
RMSE values indicate generally good fitting performance
AUC and Tmax provide meaningful indicators of metabolic response

## Tech Stack
Python
NumPy
SciPy
Matplotlib
Pandas

This project demonstrates how physiological modeling can be combined with data analysis techniques to extract insights from clinical data.
It reflects a transition from Biomedical Engineering → Data Science / AI, focusing on real-world health data applications.


Martina Misiano
