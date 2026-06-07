Requirement ID: ANA-001
Title:
HPI 15-Minute Hypotension Event Prediction
Category:
Analytics
Priority:
Critical
Feature:
HPI
Screens:
• SCR-001
• SCR-007
• SCR-016
Parameters:
• HPI
• MAP
• CI
• SVV
• PPV
Related Risks:
• RSK-003
• RSK-004
Dependencies:
• Acumen IQ Sensor
• Advanced Analytics Module
Requirement:
The system shall execute the Hypotension Prediction Index (HPI) predictive algorithm to detect and output an early warning scoring value representing an impending low blood pressure event 15 minutes before the physical onset of hypotension.
Verification Method:
Performance Test
Acceptance Criteria:
Verify that the analytical engine calculates and returns an updated HPI metric (0-100) reflecting hemodynamic decay trends exactly 15 minutes prior to a simulated threshold violation event.
Impact Keywords:
hypotension
prediction
index
early
warning
proactive
instability
arterial
waveform
Requirement ID: ANA-002
Title:
Real-Time Update Interval for HPI Calculations
Category:
Analytics
Priority:
Critical
Feature:
HPI
Screens:
• SCR-001
• SCR-007
Parameters:
• HPI
• MAP
Related Risks:
• RSK-003
• RSK-004
Dependencies:
• Data Acquisition Pipeline
• Acumen IQ Sensor
Requirement:
The system shall recompute and refresh the calculated HPI parameter value automatically every 20 seconds using the incoming arterial waveform data streams.
Verification Method:
Performance Test
Acceptance Criteria:
Verify that the calculated HPI tracking value is rewritten precisely at 20-second boundaries when driven by active real-time input pipelines.
Impact Keywords:
update
interval
seconds
recompute
refresh
real-time
hpi
calculation
Requirement ID: ANA-003
Title:
Global Hypoperfusion Index (GHI) Advanced Multi-Parametric Calculation
Category:
Analytics
Priority:
Critical
Feature:
Global Hypoperfusion Index (GHI)
Screens:
• SCR-001
• SCR-005
Parameters:
• GHI
• MAP
• SvO₂
• StO₂
• CO
Related Risks:
• RSK-003
• RSK-005
Dependencies:
• Multi-Sensor Support
• Advanced Analytics Module
Requirement:
The system shall continuously execute multi-parametric mathematical risk modeling that correlates macro-hemodynamic parameters with tissue perfusion indexes to derive a comprehensive Global Hypoperfusion Index (GHI).
Verification Method:
System Test
Acceptance Criteria:
Verify that the platform calculates an uncorrupted GHI score across the specified validation matrix to accurately reveal underlying systemic oxygenation debt states.
Impact Keywords:
ghi
global
hypoperfusion
index
multi-parametric
oxygenation
debt
perfusion
Requirement ID: ANA-004
Title:
Cerebral Autoregulation Index (CAI) Phase-Shift Derivation
Category:
Analytics
Priority:
High
Feature:
CAI
Screens:
• SCR-001
• SCR-002
Parameters:
• CAI
• MAP
• StO₂
Related Risks:
• RSK-015
• RSK-005
Dependencies:
• ForeSight Tissue Oximetry
• Acumen IQ Sensor
Requirement:
The system shall perform automated phase-shift frequency analysis between mean arterial pressure wave changes and tissue oximetry fluctuations to calculate a continuous Cerebral Autoregulation Index (CAI).
Verification Method:
Functional Test
Acceptance Criteria:
Verify that introducing a simulated phase shift across independent pressure and near-infrared inputs returns an accurate, synchronized CAI correlation coefficient.
Impact Keywords:
cai
cerebral
autoregulation
phase-shift
frequency
correlation
coefficient
spectroscopy
Requirement ID: ANA-005
Title:
Assisted Fluid Management (AFM) Patient Optimization Recommendation
Category:
Analytics
Priority:
High
Feature:
AFM
Screens:
• SCR-008
Parameters:
• AFM
• SV
• SVV
Related Risks:
• RSK-007
• RSK-004
Dependencies:
• Advanced Analytics Module
• Goal Directed Therapy (GDT)
Requirement:
The system shall utilize stroke volume tracking matrices and mechanical respiratory interaction filters to calculate customized fluid responsiveness volume guidance profiles.
Verification Method:
Integration Test
Acceptance Criteria:
Verify that the analytical pipeline generates a precise fluid loading or restriction recommendation box that accurately guides targeted volume optimization algorithms.
Impact Keywords:
afm
fluid
management
recommendation
volume
optimization
responsiveness
guidance
Requirement ID: ANA-006
Title:
Continuous Thermodilution Cardiac Output Curve Modeling
Category:
Analytics
Priority:
High
Feature:
Swan-Ganz Technology
Screens:
• SCR-001
• SCR-011
Parameters:
• CO
• CCI
Related Risks:
• RSK-012
• RSK-006
Dependencies:
• Swan-Ganz IQ Catheter
• Advanced Analytics Module
Requirement:
The system shall process thermal wash-out dissipation curves received from the physical catheter thermistor array to compute a continuous, real-time Cardiac Output (CO) estimation profile.
Verification Method:
Functional Test
Acceptance Criteria:
Verify that inputting a simulated thermal dissipation wash-out waveform properly models the down-slope geometry to execute standard continuous flow index updates.
Impact Keywords:
thermodilution
cardiac
output
co
thermal
wash-out
curve
dissipation
Requirement ID: ANA-007
Title:
Stroke Volume Variation (SVV) Respiratory Integration Parsing
Category:
Analytics
Priority:
High
Feature:
FloTrac Sensor
Screens:
• SCR-001
Parameters:
• SVV
• SV
Related Risks:
• RSK-007
• RSK-004
Dependencies:
• Acumen IQ Sensor
• FloTrac Sensor
Requirement:
The system shall apply statistical maximum-to-minimum stroke volume distribution analytics across active positive-pressure ventilation breath cycles to automatically calculate the Stroke Volume Variation (SVV) percentage.
Verification Method:
System Test
Acceptance Criteria:
Verify that the mathematical parsing loop returns a correct dynamic SVV percentage index corresponding to the calculated respirator-driven variation bounds.
Impact Keywords:
svv
stroke
volume
variation
respiratory
cycle
ventilation
percentage
Requirement ID: ANA-008
Title:
Arterial Pressure Maximum Derivative (dP/dt) Calculation
Category:
Analytics
Priority:
High
Feature:
HPI
Screens:
• SCR-001
• SCR-007
Parameters:
• dP/dt
Related Risks:
• RSK-004
• RSK-003
Dependencies:
• Acumen IQ Sensor
• Advanced Analytics Module
Requirement:
The system shall run a real-time mathematical differentiation pass on the upstroke inflection segment of the arterial pressure wave profile to track the continuous cardiac contractility index dP/dt.
Verification Method:
System Test
Acceptance Criteria:
Verify that the analytical engine tracks the peak pressure slope trajectory accurately to yield continuous dP/dt parameters on the user display grid.
Impact Keywords:
dp/dt
derivative
upstroke
contractility
differentiation
slope
inflection
Requirement ID: ANA-009
Title:
Dynamic Elastance (Ea_dyn) Ventricular-Arterial Coupling Analysis
Category:
Analytics
Priority:
High
Feature:
HPI
Screens:
• SCR-001
• SCR-007
Parameters:
• Ea_dyn
• PPV
• SVV
Related Risks:
• RSK-007
• RSK-003
Dependencies:
• HPI Algorithm Engine
Requirement:
The system shall compute the dimensionless ventricular-arterial coupling factor (Ea_dyn) by processing the real-time mathematical ratio between pulse pressure variation (PPV) and stroke volume variation (SVV).
Verification Method:
Integration Test
Acceptance Criteria:
Verify that synchronized changes in the underlying PPV and SVV variance profiles return a mathematically correct Ea_dyn ratio matching the validation scenario data points.
Impact Keywords:
elastance
ea_dyn
coupling
ratio
ventricular-arterial
pulse
pressure
variation
Requirement ID: ANA-010
Title:
ClearSight Finger Cuff Hydrostatic Calibration Adjustment Calculation
Category:
Analytics
Priority:
High
Feature:
ClearSight Technology
Screens:
• SCR-001
• SCR-013
Parameters:
• NIBP
• MAP
Related Risks:
• RSK-014
• RSK-006
Dependencies:
• Heart Reference Sensor (HRS)
• Calibration Service
Requirement:
The system shall automatically subtract or add derived fluid column pressure offsets from noninvasive finger measurements based on relative vertical height readings reported by the Heart Reference Sensor.
Verification Method:
Functional Test
Acceptance Criteria:
Verify that moving the reference physical sensor interface above or below the monitoring baseline plane calculates corresponding hydrostatic pressure adjustment factors.
Impact Keywords:
hydrostatic
offset
compensation
hrs
clearsight
elevation
height
calibration
Requirement ID: ANA-011
Title:
ForeSight IQ Spectroscopy Artifact Rejection Filter
Category:
Analytics
Priority:
High
Feature:
ForeSight Tissue Oximetry
Screens:
• SCR-015
• SCR-001
Parameters:
• StO₂
• SQI
Related Risks:
• RSK-005
• RSK-002
Dependencies:
• Advanced Analytics Module
• ForeSight IQ Sensor
Requirement:
The system shall apply real-time ambient lighting and motion-artifact subtraction algorithms to isolate true tissue spectroscopic backscatter arrays from external signal contamination.
Verification Method:
Functional Test
Acceptance Criteria:
Verify that introducing high-intensity ambient optical contamination changes does not compromise the calculated StO₂ calculation, due to active rejection filtration.
Impact Keywords:
artifact
rejection
filter
spectroscopy
ambient
light
motion
subtraction
Requirement ID: ANA-012
Title:
Swan-Ganz Smart Wedge Pressure Curve Frequency Analysis
Category:
Analytics
Priority:
High
Feature:
Smart Wedge
Screens:
• SCR-023
• SCR-013
Parameters:
• PAOP
• Wedge Index
Related Risks:
• RSK-012
• RSK-003
Dependencies:
• Smart Wedge Frequency Extraction Engine
• Distal Transducer Line
Requirement:
The system shall execute automated fast Fourier transform (FFT) parsing loops on distal catheter waveforms to determine when true vascular trace dampening corresponds to an active balloon wedge occlusion state.
Verification Method:
Functional Test
Acceptance Criteria:
Verify that the analysis framework correctly resolves dampening frequencies to calculate a Wedge Index score, safely confirming baseline pulmonary artery occlusion pressure parameters.
Impact Keywords:
smart
wedge
fft
frequency
dampening
occlusion
paop
waveform
Requirement ID: ANA-013
Title:
Continuous Systemic Vascular Resistance (SVR) Multi-Parameter Mapping
Category:
Analytics
Priority:
High
Feature:
FloTrac Sensor
Screens:
• SCR-001
Parameters:
• SVR
• MAP
• CVP
• CO
Related Risks:
• RSK-006
• RSK-004
Dependencies:
• FloTrac Sensor
• Advanced Analytics Module
Requirement:
The system shall evaluate mean arterial pressure, cardiac output, and central venous pressure data continuously to calculate and update the derived Systemic Vascular Resistance (SVR) metric.
Verification Method:
System Test
Acceptance Criteria:
Verify that changing independent continuous baseline inputs calculates a corresponding, mathematically correct SVR value that maps precisely to standard hemodynamic laws.
Impact Keywords:
svr
vascular
resistance
hemodynamic
derived
calculation
map
cvp
co
Requirement ID: ANA-014
Title:
HPI Velocity Acceleration Rate-of-Change Monitoring
Category:
Analytics
Priority:
High
Feature:
HPI Smart Alerts
Screens:
• SCR-001
• SCR-007
Parameters:
• HPI
• MAP
Related Risks:
• RSK-003
• RSK-004
Dependencies:
• Advanced Analytics Module
• HPI Algorithm Engine
Requirement:
The system shall monitor sequential velocity changes across historical HPI scores to trigger a "Smart Alert" notification if the acceleration rate toward instability threatens safe operational baselines.
Verification Method:
System Test
Acceptance Criteria:
Verify that if a simulated patient's HPI score accelerates upwards rapidly over consecutive 20-second blocks, the system issues a predictive Smart Alert notice before a static boundary limit is cracked.
Impact Keywords:
smart
alerts
acceleration
velocity
predictive
trajectory
rate
instability
Requirement ID: ANA-015
Title:
Tissue Oximetry Total Hemoglobin (tHb) Continuous Algorithmic Calculation
Category:
Analytics
Priority:
High
Feature:
ForeSight Tissue Oximetry
Screens:
• SCR-015
Parameters:
• tHb
• ΔctHb
• StO₂
Related Risks:
• RSK-006
• RSK-005
Dependencies:
• ForeSight IQ Sensor
• Advanced Analytics Module
Requirement:
The system shall utilize multi-wavelength near-infrared spectroscopy absorption models to compute and display a continuous estimation of total tissue hemoglobin content (tHb).
Verification Method:
Functional Test
Acceptance Criteria:
Verify that passing simulated optical spectroscopic density variations into the tissue oximetry analytics layer successfully resolves and updates continuous local tHb and relative percentage metrics.
Impact Keywords:
spectroscopy
hemoglobin
absorption
wavelength
continuous
oximetry
tissue
estimation
Validation Report
Requirements Processed: 15
Screens Mapped: 21
Risks Mapped: 23
Missing Screen References: 0
Missing Risk References: 0
Duplicate IDs: 0