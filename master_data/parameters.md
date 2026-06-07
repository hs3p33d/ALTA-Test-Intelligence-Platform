Parameter ID: PAR-001
Parameter Name:
MAP
Full Name:
Mean Arterial Pressure
Category:
Hemodynamic - Pressure
Unit:
mmHg
Clinical Purpose:
Represents the average perfusion pressure across the systemic vascular architecture throughout a complete cardiac contraction cycle.
Related Features:
• Continuous Monitoring
• ClearSight Technology
• FloTrac Sensor
• HPI
• CAI
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• Zero & Waveform Screen
• HPI Algorithm Side Panel
Related Risks:
• Hypotension Event
• Signal Artifact
Expected Value Source:
Invasive Arterial Line (Acumen IQ / FloTrac) or Noninvasive Finger Cuff (ClearSight)
Impact Keywords:
map
pressure
arterial
perfusion
hemodynamic
monitoring
systolic
diastolic
Parameter ID: PAR-002
Parameter Name:
CO
Full Name:
Cardiac Output
Category:
Hemodynamic - Flow
Unit:
L/min
Clinical Purpose:
Measures the absolute total volume of blood pumped by the heart per minute to assess global systemic blood flow delivery.
Related Features:
• FloTrac Sensor
• ClearSight Technology
• Swan-Ganz Technology
• GHI
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• Thermodilution Summary Screen
Related Risks:
• Low Flow State
• Inaccurate Measurements
Expected Value Source:
Pulse Contour Analysis (Acumen IQ / FloTrac / ClearSight) or Intermittent/Continuous Thermodilution (Swan-Ganz)
Impact Keywords:
co
flow
volume
cardiac
output
thermodilution
contour
delivery
Parameter ID: PAR-003
Parameter Name:
CI
Full Name:
Cardiac Index
Category:
Hemodynamic - Flow
Unit:
L/min/m²
Clinical Purpose:
Relates the absolute cardiac output performance directly to an individual patient's physical size by normalizing flow to body surface area.
Related Features:
• Patient Monitoring
• FloTrac Sensor
• ClearSight Technology
• Swan-Ganz Technology
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• Cockpit Screen
• Goal Positioning Screen
Related Risks:
• Hypoperfusion
• Inaccurate Demographics
Expected Value Source:
Algorithmic Calculation Normalized by Patient Body Surface Area (BSA)
Impact Keywords:
ci
index
cardiac
flow
normalized
bsa
surface
area
Parameter ID: PAR-004
Parameter Name:
SV
Full Name:
Stroke Volume
Category:
Hemodynamic - Flow
Unit:
mL/beat
Clinical Purpose:
Quantifies the discrete volume of blood ejected by the left ventricle into the systemic circulation during a single mechanical heartbeat.
Related Features:
• FloTrac Sensor
• ClearSight Technology
• AFM
• Goal Directed Therapy (GDT)
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• AFM Dashboard
• Fluid Responsiveness Test Screen
Related Risks:
• Hypovolemia
• AFM Misclassification
Expected Value Source:
Pulse Contour Waveform Integration Matrix
Impact Keywords:
sv
stroke
volume
ejection
beat
flow
systolic
contour
Parameter ID: PAR-005
Parameter Name:
SVV
Full Name:
Stroke Volume Variation
Category:
Hemodynamic - Fluid Responsiveness
Unit:
%
Clinical Purpose:
Assesses percentage variations in stroke volume across the respiratory cycle to determine fluid responsiveness criteria in mechanically ventilated patients.
Related Features:
• FloTrac Sensor
• ClearSight Technology
• AFM
• Goal Positioning Screen
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• AFM Dashboard
• Goal Positioning Screen
Related Risks:
• Inappropriate Fluid Bolus
• Mechanical Ventilation Dependence
Expected Value Source:
Beat-by-Beat Pulse Contour Respiratory Loop Analysis
Impact Keywords:
svv
variation
stroke
volume
fluid
responsiveness
respiratory
preload
Parameter ID: PAR-006
Parameter Name:
PPV
Full Name:
Pulse Pressure Variation
Category:
Hemodynamic - Fluid Responsiveness
Unit:
%
Clinical Purpose:
Measures dynamic arterial pulse pressure fluctuations across inhalation and exhalation sweeps to help identify position on the Frank-Starling curve.
Related Features:
• Acumen IQ Sensor
• FloTrac Sensor
• AFM
• HPI
Related Screens:
• Main Monitoring Screen
• AFM Dashboard
• HPI Algorithm Side Panel
Related Risks:
• Signal Artifact
• Inappropriate Fluid Bolus
Expected Value Source:
Arterial Pressure Waveform Pulse Amplitude Derivation
Impact Keywords:
ppv
pulse
pressure
variation
fluid
responsiveness
amplitude
respiratory
Parameter ID: PAR-007
Parameter Name:
HPI
Full Name:
Hypotension Prediction Index
Category:
Predictive AI Analytics
Unit:
Integer (0 - 100)
Clinical Purpose:
Provides an advanced early-warning probability metric predicting the specific likelihood that a patient will experience a hypotensive event.
Related Features:
• HPI
• HPI Smart Alerts
• Continuous Monitoring
Related Screens:
• Main Monitoring Screen
• Cockpit Screen
• HPI Secondary Screen
• HPI Algorithm Side Panel
Related Risks:
• HPI False Negative
• HPI False Positive
• Delayed Intervention
Expected Value Source:
Machine Learning Arterial Waveform Pulse Feature Extractor Engine
Impact Keywords:
hpi
hypotension
prediction
index
early
warning
proactive
instability
Parameter ID: PAR-008
Parameter Name:
StO₂
Full Name:
Tissue Oxygen Saturation
Category:
Oximetry - Tissue
Unit:
%
Clinical Purpose:
Continuously quantifies local microvascular oxygen saturation status within targeted underlying cerebral or deep somatic tissues.
Related Features:
• ForeSight Tissue Oximetry
• ForeSight IQ Sensor
• CAI
• GHI
Related Screens:
• Main Monitoring Screen
• Physiology Screen (Split Screen)
• Tissue Oximetry Physiology Screen
Related Risks:
• Cerebral Hypoxia
• Sensor Disconnect
Expected Value Source:
Multi-Wavelength Near-Infrared Spectroscopy (NIRS) Optical Return
Impact Keywords:
sto2
tissue
oxygenation
saturation
cerebral
somatic
foresight
nirs
Parameter ID: PAR-009
Parameter Name:
SvO₂
Full Name:
Mixed Venous Oxygen Saturation
Category:
Oximetry - Venous
Unit:
%
Clinical Purpose:
Monitors the global equilibrium point between systemic tissue oxygen delivery and total patient oxygen consumption.
Related Features:
• Venous Oximetry
• HemoSphere Oximetry Cable
• GHI
Related Screens:
• Main Monitoring Screen
• Physiology Screen (Split Screen)
• Zero & Waveform Screen
Related Risks:
• Severe Tissue Hypoxia
• Improper Calibration
Expected Value Source:
Invasive Spectrophotometric Catheter Insertion Assembly
Impact Keywords:
svo2
venous
oximetry
saturation
oxygen
consumption
delivery
equilibrium
Parameter ID: PAR-010
Parameter Name:
CVP
Full Name:
Central Venous Pressure
Category:
Hemodynamic - Pressure
Unit:
mmHg
Clinical Purpose:
Measures baseline static blood pressure inside the superior vena cava or right atrium to evaluate right ventricular preload status.
Related Features:
• Pressure Cable Monitoring
• Swan-Ganz Technology
• Derived Value Calculator
Related Screens:
• Main Monitoring Screen
• Physiology Screen (Split Screen)
• Zero & Waveform Screen
• Derived Value Calculator
Related Risks:
• Overhydration
• Improper Zeroing
Expected Value Source:
TruWave Transducer Fluid Column Connection
Impact Keywords:
cvp
central
venous
pressure
right
atrium
preload
transducer
Parameter ID: PAR-011
Parameter Name:
PAP
Full Name:
Pulmonary Artery Pressure (Mean, Systolic, Diastolic)
Category:
Hemodynamic - Pressure
Unit:
mmHg
Clinical Purpose:
Tracks specific systolic, diastolic, and averaged mean blood pressures within the pulmonary main branch arterial network.
Related Features:
• Swan-Ganz Technology
• Pressure Cable Monitoring
• Smart Wedge
Related Screens:
• Main Monitoring Screen
• Physiology Screen (Split Screen)
• Zero & Waveform Screen
• PAOP Measurement Screen
Related Risks:
• Pulmonary Hypertension
• Catheter Migration
Expected Value Source:
Swan-Ganz IQ Catheter Tip Pressure Sensor Channel
Impact Keywords:
pap
pulmonary
artery
pressure
systolic
diastolic
mean
lung
Parameter ID: PAR-012
Parameter Name:
PAOP
Full Name:
Pulmonary Artery Occlusion Pressure
Category:
Hemodynamic - Pressure
Unit:
mmHg
Clinical Purpose:
Indirectly measures left atrial filling pressure during temporary catheter balloon inflation to evaluate left ventricular end-diastolic preload.
Related Features:
• Swan-Ganz Technology
• Smart Wedge
Related Screens:
• PAOP Measurement Screen
• Zero & Waveform Screen
• Thermodilution Summary Screen
Related Risks:
• Pulmonary Rupture
• Inaccurate Measurements
Expected Value Source:
Transient Catheter Balloon Inflation Waveform Conversion Checking
Impact Keywords:
paop
wedge
occlusion
pressure
pulmonary
left
atrium
preload
Parameter ID: PAR-013
Parameter Name:
SVR
Full Name:
Systemic Vascular Resistance
Category:
Hemodynamic - Calculated
Unit:
dynes·sec/cm⁵
Clinical Purpose:
Determines total resistance to blood flow imposed by the systemic peripheral vascular tree layout, reflecting overall afterload.
Related Features:
• FloTrac Sensor
• ClearSight Technology
• Derived Value Calculator
Related Screens:
• Main Monitoring Screen
• Derived Value Calculator
• Goal Directed Therapy (GDT) Screen
Related Risks:
• Vasodilation
• Inaccurate Measurements
Expected Value Source:
Calculated via Transduced Pressures and Core Flow Math Integration
Impact Keywords:
svr
resistance
afterload
systemic
vascular
peripheral
vasoconstriction
Parameter ID: PAR-014
Parameter Name:
CAI
Full Name:
Cerebral Autoregulation Index
Category:
Predictive AI Analytics
Unit:
Index Coefficient (-1.0 to +1.0)
Clinical Purpose:
Tracks structural correlation between mean arterial blood pressure movements and local brain oxygenation changes to evaluate real-time autoregulation status.
Related Features:
• CAI
• Multi-Sensor Support
Related Screens:
• Main Monitoring Screen
• Cockpit Screen
• Trend Monitoring View
Related Risks:
• Autoregulation Failure
• Delay in Diagnosis
Expected Value Source:
Algorithmic Cross-Sensor Co-dependency Core Engine Processing
Impact Keywords:
cai
cerebral
autoregulation
index
correlation
brain
pressure
saturation
Parameter ID: PAR-015
Parameter Name:
GHI
Full Name:
Global Hypoperfusion Index
Category:
Predictive AI Analytics
Unit:
Composite Score Value
Clinical Purpose:
Provides a unified dashboard indicator analyzing macro-circulatory parameters alongside cellular oxygenation tracking to flag occult hypoperfusion.
Related Features:
• GHI
• Multi-Sensor Support
Related Screens:
• Main Monitoring Screen
• Cockpit Screen
• Trend Monitoring View
Related Risks:
• Shock Progression
• Inaccurate Hypoperfusion Prediction
Expected Value Source:
Multi-Sensor Statistical Aggregation Platform Engine
Impact Keywords:
ghi
global
hypoperfusion
index
oxygenation
flow
composite
metabolic
Parameter ID: PAR-016
Parameter Name:
BSA
Full Name:
Body Surface Area
Category:
Derived Demographic Base
Unit:
m²
Clinical Purpose:
Establishes the mathematical body surface area mapping constant required to resolve patient-indexed flow values.
Related Features:
• Patient Monitoring
• Data Management
Related Screens:
• Patient Data Screen
• Patient Selection Screen
Related Risks:
• Inaccurate Measurements
• Wrong Patient Context
Dependencies:
• Height, Weight Settings
Expected Value Source:
Manual Entry Demographics Formula Engine Execution
Impact Keywords:
bsa
surface
area
body
height
weight
demographics
indexing
Parameter ID: PAR-017
Parameter Name:
tHb
Full Name:
Total Hemoglobin (Tissue)
Category:
Oximetry - Tissue
Unit:
g/dL (or Relative Absolute Units)
Clinical Purpose:
Provides continuous tracking of the localized total hemoglobin volume index present under the sensor tissue field interface.
Related Features:
• ForeSight Tissue Oximetry
• ForeSight IQ Sensor
Related Screens:
• Tissue Oximetry Physiology Screen
Related Risks:
• Ischemia
• Signal Artifact
Expected Value Source:
ForeSight IQ Optical Absorptive Matrix Resolving
Impact Keywords:
thb
hemoglobin
total
tissue
oximetry
spectroscopy
volume
Parameter ID: PAR-018
Parameter Name:
ΔctHb
Full Name:
Relative Total Tissue Hemoglobin Concentration Change
Category:
Oximetry - Tissue
Unit:
% (or Baseline Delta Scale)
Clinical Purpose:
Monitors real-time percentage shifts in microvascular blood volume path density against fixed initial patient baselines.
Related Features:
• ForeSight Tissue Oximetry
• Advanced Analytics Module
Related Screens:
• Tissue Oximetry Physiology Screen
Related Risks:
• Regional Congestion
• Delayed Intervention
Expected Value Source:
Spectroscopic Baseline Difference Engine Logging
Impact Keywords:
dcthb
delta
concentration
hemoglobin
trajectory
tissue
oximetry
Parameter ID: PAR-019
Parameter Name:
Wedge Index
Full Name:
Smart Wedge Validity Score
Category:
Waveform Validation Index
Unit:
Score Boundary (0 to 1)
Clinical Purpose:
Evaluates structural dampening transitions of the pulmonary artery pressure waveform trace to confirm catheter occlusion positioning.
Related Features:
• Smart Wedge
• Swan-Ganz Technology
Related Screens:
• PAOP Measurement Screen
• Zero & Waveform Screen
Related Risks:
• Over-reliance on Algorithms
• Inaccurate Measurements
Expected Value Source:
Frequency-Domain Pattern Matching Logic
Impact Keywords:
wedge
index
smart
occlusion
dampening
validation
trace
paop
Parameter ID: PAR-020
Parameter Name:
dP/dt
Full Name:
Arterial Waveform Systolic Upslope Derivative (Contractility)
Category:
Hemodynamic - Contractility
Unit:
mmHg/sec
Clinical Purpose:
Calculates the peak velocity slope rise across early systolic pulse transitions to track left ventricular myocardial contractility forces.
Related Features:
• Acumen IQ Sensor
• HPI
Related Screens:
• Main Monitoring Screen
• HPI Secondary Screen
• Parameter Configuration Menu
Related Risks:
• Heart Failure
• Signal Artifact
Expected Value Source:
Continuous First Derivative Processing of Arterial Pressure Contours
Impact Keywords:
dp/dt
contractility
systolic
slope
velocity
myocardial
contour
force
Parameter ID: PAR-021
Parameter Name:
Ea_dyn
Full Name:
Dynamic Arterial Elastance
Category:
Hemodynamic - Afterload
Unit:
Dimensionless Ratio Value
Clinical Purpose:
Evaluates the fractional mathematical ratio of pulse pressure variation over stroke volume variation to trace functional ventricular-arterial coupling.
Related Features:
• Acumen IQ Sensor
• HPI
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• HPI Secondary Screen
Related Risks:
• Vasomotor Instability
• Algorithm Limitations
Expected Value Source:
Automated PPV / SVV Division Matrix Realization
Impact Keywords:
ea_dyn
elastance
afterload
coupling
ratio
variation
dynamic
Parameter ID: PAR-022
Parameter Name:
SQI
Full Name:
Signal Quality Indicator
Category:
Hardware Integrity Index
Unit:
% (or Quality Level Tier)
Clinical Purpose:
Validates raw signal input return integrity for oximetry and hardware streams to prevent artifact translation into clinical calculations.
Related Features:
• Venous Oximetry
• ForeSight Tissue Oximetry
Related Screens:
• Main Monitoring Screen
• Tissue Oximetry Physiology Screen
Related Risks:
• Signal Artifact
• Data Loss
Expected Value Source:
Hardware Return Diagnostics Stream Monitoring
Impact Keywords:
sqi
signal
quality
integrity
artifact
validation
hardware
diagnostics
Parameter ID: PAR-023
Parameter Name:
RVP
Full Name:
Right Ventricular Pressure (Mean, Systolic, Diastolic)
Category:
Hemodynamic - Pressure
Unit:
mmHg
Clinical Purpose:
Measures localized intracardiac blood pressure conditions within the right ventricular chamber during insertion or ongoing care path protocols.
Related Features:
• Swan-Ganz Technology
• Pressure Cable Monitoring
Related Screens:
• Main Monitoring Screen
• Zero & Waveform Screen
Related Risks:
• Ventricular Arrhythmia
• Improper Zeroing
Expected Value Source:
Swan-Ganz Catheter Right Ventricular Flow Port Connection
Impact Keywords:
rvp
right
ventricle
pressure
systolic
diastolic
intracardiac
chamber
Parameter ID: PAR-024
Parameter Name:
CO_RV
Full Name:
Right Ventricular Ejection Volume Flow Metric
Category:
Hemodynamic - Flow
Unit:
L/min
Clinical Purpose:
Isolates flow performance and output measurements traversing through the right heart chambers.
Related Features:
• Swan-Ganz Technology
• Multi-Sensor Support
Related Screens:
• Main Monitoring Screen
• Thermodilution Summary Screen
Related Risks:
• Right Heart Failure
• Catheter Migration
Expected Value Source:
Continuous Right Ventricular Thermal Dissipation Tracking
Impact Keywords:
co_rv
right
ventricular
flow
heart
output
volume
thermodilution
Parameter ID: PAR-025
Parameter Name:
EDV
Full Name:
Right Ventricular End-Diastolic Volume
Category:
Hemodynamic - Volume
Unit:
mL
Clinical Purpose:
Measures absolute blood volume status remaining inside the right ventricular cavity at the immediate conclusion of its filling phase.
Related Features:
• Swan-Ganz Technology
• Data Management
Related Screens:
• Main Monitoring Screen
• Thermodilution Summary Screen
Related Risks:
• Volume Overload
• Inaccurate Measurements
Expected Value Source:
Thermodilution Volumetric Curve Decay Extrapolation
Impact Keywords:
edv
end-diastolic
volume
right
ventricle
preload
volumetric
Parameter ID: PAR-026
Parameter Name:
RVEF
Full Name:
Right Ventricular Ejection Fraction
Category:
Hemodynamic - Fractional Performance
Unit:
%
Clinical Purpose:
Calculates the relative percentage proportion of end-diastolic right heart volume successfully cleared with each active mechanical pump cycle.
Related Features:
• Swan-Ganz Technology
• Advanced Analytics Module
Related Screens:
• Main Monitoring Screen
• Parameter Configuration Menu
Related Risks:
• Myocardial Infarction
• Low Flow State
Expected Value Source:
Volumetric Intermittent Ratio Math Calculations
Impact Keywords:
rvef
ejection
fraction
right
ventricle
percentage
efficiency
contractility
Parameter ID: PAR-027
Parameter Name:
SVRI
Full Name:
Systemic Vascular Resistance Index
Category:
Hemodynamic - Calculated
Unit:
dynes·sec/cm⁵·m²
Clinical Purpose:
Normalizes measured systemic vascular afterload directly against patient size constraints utilizing the derived Body Surface Area constant.
Related Features:
• FloTrac Sensor
• Derived Value Calculator
Related Screens:
• Main Monitoring Screen
• Derived Value Calculator
Related Risks:
• Septic Shock
• Wrong Patient Context
Expected Value Source:
SVR Math Division by Patient BSA Constant
Impact Keywords:
svri
index
resistance
afterload
systemic
vascular
normalized
bsa
Parameter ID: PAR-028
Parameter Name:
NIBP
Full Name:
Noninvasive Blood Pressure (Systolic, Diastolic, Mean)
Category:
Hemodynamic - Pressure
Unit:
mmHg
Clinical Purpose:
Provides continuous, non-surgical systemic blood pressure tracking utilizing finger-cuff technologies without requiring arterial puncture lines.
Related Features:
• ClearSight Technology
• ClearSight Finger Cuff
Related Screens:
• Main Monitoring Screen
• Zero & Waveform Screen
Related Risks:
• Numbness/Tingling
• Wrong Sensor Size
Expected Value Source:
Pneumatic Finger Cuff Volume Clamp Dynamic Tracking Loop
Impact Keywords:
nibp
noninvasive
pressure
clearsight
finger
cuff
systolic
diastolic
Parameter ID: PAR-029
Parameter Name:
HR
Full Name:
Heart Rate
Category:
Hemodynamic - Frequency
Unit:
beats/min
Clinical Purpose:
Tracks mechanical contraction cycling frequency of the heart per minute to resolve primary flow calculation algorithms.
Related Features:
• Continuous Monitoring
• Alarm Management
Related Screens:
• Main Monitoring Screen
• Trend Monitoring View
• Alarms/Targets Screen
Related Risks:
• Tachycardia
• Bradycardia
Expected Value Source:
Arterial Pulse Waveform Peak-to-Peak Frequency Timing Detection
Impact Keywords:
hr
heart
rate
frequency
beats
pulse
timing
hemodynamic
Parameter ID: PAR-030
Parameter Name:
AFM
Full Name:
Assisted Fluid Management Target Optimization Metric
Category:
Predictive AI Analytics
Unit:
Fluid Protocol Status Tracking Matrix
Clinical Purpose:
Traces institutional fluid progression steps to deliver automated decision-support data for surgical patient fluid loading.
Related Features:
• AFM
• Goal Directed Therapy (GDT)
Related Screens:
• AFM Dashboard
• Clinical Tools Panel (Overlay)
Related Risks:
• AFM Misclassification
• Over-reliance on Algorithms
Expected Value Source:
Adaptive Stroke Volume Closed-Loop Learning Framework
Impact Keywords:
afm
fluid
management
optimization
bolus
decision-support
adaptive
learning