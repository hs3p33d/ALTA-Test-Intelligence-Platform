Requirement ID: ALM-001
Title:
HPI Alarm Generation Threshold
Category:
Alarm Management
Priority:
Critical
Feature:
HPI (Hypotension Prediction Index)
Screens:
• SCR-001
• SCR-007
• SCR-016
Parameters:
• HPI
• MAP
Related Risks:
• RSK-003
• RSK-003
Dependencies:
• Acumen IQ Sensor
• HPI Algorithm Engine
Requirement:
The system shall automatically trigger a physiological alarm when the calculated Hypotension Prediction Index (HPI) value exceeds the factory default threshold of 84.
Verification Method:
Functional Test
Acceptance Criteria:
Verify that a physiological alarm condition initiates precisely when the real-time HPI parameter value steps above 84.
Impact Keywords:
hypotension
prediction
index
threshold
physiological
alarm
alert
trigger
default
Requirement ID: ALM-002
Title:
Hands-Free Voice Control Alarm Silencing
Category:
Alarm Management
Priority:
High
Feature:
Voice Commands
Screens:
• SCR-001
• SCR-002
• SCR-005
Parameters:
• HPI
• MAP
• CO
Related Risks:
• RSK-010
• RSK-004
Dependencies:
• Voice Recognition Module
• Audio Processing Hardware
Requirement:
The system shall temporarily silence active audible alarm indicators upon receiving the explicit hands-free verbal utterance command "silence alarm".
Verification Method:
Usability Test
Acceptance Criteria:
Verify that speaking the exact string "silence alarm" immediately pauses the audible transducer alarm sound pattern without stopping the flashing visual target alerts on screen.
Impact Keywords:
voice
control
touchless
silence
audio
command
hands-free
verbal
Requirement ID: ALM-003
Title:
Gesture-Driven Remote Alarm Acknowledgment
Category:
Alarm Management
Priority:
High
Feature:
Gesture Commands
Screens:
• SCR-001
• SCR-003
Parameters:
• MAP
• CO
Related Risks:
• RSK-010
• RSK-004
Dependencies:
• Optical Hand Tracking Camera
• Gesture Recognition Pipeline
Requirement:
The system shall recognize a horizontal hand wave gesture performed within a 1.5-meter distance to dismiss a currently active medium or low priority alarm banner overlay.
Verification Method:
Usability Test
Acceptance Criteria:
Confirm that executing a standardized open-palm horizontal swipe path reliably acknowledges and dismisses low/medium level alerts from the screen view layout.
Impact Keywords:
gesture
control
hand
wave
dismiss
acknowledgment
touchless
optical
Requirement ID: ALM-004
Title:
Fluid Responsiveness Test Diagnostic Verification Alarm
Category:
Alarm Management
Priority:
Medium
Feature:
Fluid Responsiveness Test
Screens:
• SCR-010
• SCR-024
Parameters:
• SV
• CO
• MAP
Related Risks:
• RSK-007
• RSK-004
Dependencies:
• Fluid Responsiveness Logic Engine
Requirement:
The system shall flash a high-visibility information advisory alert box when a user-initiated Passive Leg Raise (PLR) challenge registers a dynamic Stroke Volume (SV) jump higher than 10%.
Verification Method:
Functional Test
Acceptance Criteria:
Simulating a fluid responsiveness stroke volume change step of 12% triggers an explicit validation indicator alerting the clinician that the target patient profile is responsive to volume expansion.
Impact Keywords:
fluid
responsiveness
passive
leg
raise
challenge
stroke
volume
advisory
Requirement ID: ALM-005
Title:
Continuous ClearSight Finger Cuff Under-Pressure Safety Shut-Off
Category:
Alarm Management
Priority:
Critical
Feature:
ClearSight Technology
Screens:
• SCR-001
• SCR-013
Parameters:
• NIBP
• MAP
Related Risks:
• RSK-013
• RSK-002
Dependencies:
• Pneumatic Valve Safety Assembly
• Pressure Safety Interlocks
Requirement:
The system shall automatically release internal cuff air expansion channels and issue a critical alarm sequence if a continuous ClearSight finger tracking ring maintains localized inflation above 200 mmHg for more than 5 minutes.
Verification Method:
Safety Test
Acceptance Criteria:
Artificially locking down the inflation valve pathway during active operations causes the hardware to vent the line instantly upon crossing the 5-minute timeline marker, throwing an over-pressure safety alarm.
Impact Keywords:
clearsight
finger
cuff
overpressure
safety
vent
pneumatic
timer
Requirement ID: ALM-006
Title:
ClearSight Heart Reference Sensor Spatial Misalignment Alarm
Category:
Alarm Management
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
• Differential Hydrostatic Calculator
Requirement:
The system shall produce an immediate audio-visual alert message when the vertical physical offset between the ClearSight finger assembly and the reference level of the patient's heart causes a hydrostatic pressure variance tracking shift greater than 5 mmHg.
Verification Method:
Functional Test
Acceptance Criteria:
Displacing the reference transducer sensor tip above or below the plane baseline triggers a spatial warning prompt on screen, demanding recalibration alignment confirmation.
Impact Keywords:
clearsight
heart
reference
sensor
hydrostatic
misalignment
elevation
variance
Requirement ID: ALM-007
Title:
Assisted Fluid Management (AFM) Learning Protocol Disconnect Alarm
Category:
Alarm Management
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
• RSK-003
Dependencies:
• AFM Control Framework
• Machine Learning Interactivity Subsystem
Requirement:
The system shall generate a medium-priority auditory alert chime within 3 consecutive respiratory cycles if raw parameters fluctuate outside bounded data limits expected by the adaptive fluid recommendations matrix.
Verification Method:
System Test
Acceptance Criteria:
Injecting random dynamic cardiac arrhythmia cycles into an active AFM execution flow triggers an explicit data-instability technical alert, putting bolus learning tracking on a safe standby pause status.
Impact Keywords:
afm
fluid
learning
arrhythmia
instability
standby
alert
interruption
Requirement ID: ALM-008
Title:
ForeSight IQ Tissue Oximetry Sensor Signal Degradation Advisory
Category:
Alarm Management
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
• ForeSight IQ Sensor Interface
• Signal Quality Matrix Processor
Requirement:
The system shall display a continuous yellow advisory warning text prompt within the affected tracking tile if the internal Signal Quality Indicator (SQI) for an attached tissue spectroscopy sensor falls below the minimum 35% threshold.
Verification Method:
Functional Test
Acceptance Criteria:
Dimming the return light flux levels on a validation channel to mock skin coupling issues drops the SQI score below 35%, which immediately triggers an explicit low-signal toast notification box.
Impact Keywords:
foresight
tissue
oximetry
signal
quality
sqi
degradation
coupling
Requirement ID: ALM-009
Title:
Cerebral Autoregulation Index (CAI) Co-Dependency Data Sync Failure Alert
Category:
Alarm Management
Priority:
High
Feature:
CAI
Screens:
• SCR-001
• SCR-005
Parameters:
• CAI
• MAP
• StO₂
Related Risks:
• RSK-015
• RSK-008
Dependencies:
• Multi-Sensor Data Hub
• Cross-Sensor Clock Correlator
Requirement:
The system shall issue a high-visibility technical sync alarm when data frames coming from the invasive arterial line pressure cable and the ForeSight spectroscopy module diverge by more than 150 milliseconds.
Verification Method:
Performance Test
Acceptance Criteria:
Inducing a network transmission buffering freeze delay on one of the incoming interface channels triggers a structural correlation failure alert, suspending active CAI calculation outputs to prevent old data mapping.
Impact Keywords:
cai
synchronization
latency
cross-sensor
delay
buffering
correlation
failure
Requirement ID: ALM-010
Title:
Swan-Ganz Smart Wedge Algorithmic Over-Inflation Warning
Category:
Alarm Management
Priority:
Critical
Feature:
Smart Wedge
Screens:
• SCR-023
• SCR-013
Parameters:
• PAOP
• Wedge Index
• PAP
Related Risks:
• RSK-012
• RSK-003
Dependencies:
• Smart Wedge Frequency Extraction Engine
• Balloon Inflation Sensor Line
Requirement:
The system shall sound an explicit high-frequency safety warning alarm if the automated Smart Wedge analysis algorithm detects continuous flatlined dampening configurations indicating a wedge occlusion path for over 15 seconds.
Verification Method:
Safety Test
Acceptance Criteria:
Simulating a prolonged catheter balloon inflation scenario across a 15-second timeline trigger locks an audio-visual error bar overlay to prevent microvascular pulmonary artery tissue necrosis or wall rupture.
Impact Keywords:
smart
wedge
over-inflation
balloon
occlusion
timer
safety
rupture
Requirement ID: ALM-011
Title:
Pulmonary Artery Catheter Spatial Migration Detection Alert
Category:
Alarm Management
Priority:
High
Feature:
Swan-Ganz Technology
Screens:
• SCR-001
• SCR-013
Parameters:
• PAP
• RVP
Related Risks:
• RSK-012
• RSK-006
Dependencies:
• Waveform Pattern Evaluator
• Pressure Cable Interface
Requirement:
The system shall trigger a medium priority alert pattern if the continuous pressure trace baseline changes profile types from normal pulmonary artery curves into high-amplitude right ventricular curves without user interaction.
Verification Method:
Functional Test
Acceptance Criteria:
Feeding an input morphing sequence that represents mechanical catheter slippage or displacement into the monitoring module triggers a catheter displacement alert banner overlay.
Impact Keywords:
migration
catheter
displacement
pulmonary
ventricular
waveform
morphology
slippage
Requirement ID: ALM-012
Title:
Non-Volatile Solid-State Partition Full Overwrite Alert
Category:
Alarm Management
Priority:
Medium
Feature:
Data Management
Screens:
• SCR-001
• SCR-021
Parameters:
• MAP
• CO
Related Risks:
• RSK-008
• RSK-008
Dependencies:
• Storage File Management System
• Local Health Monitoring Daemon
Requirement:
The system shall trigger a low-priority technical warning flag on the system status bar when available non-volatile local disk storage capacity drops below 5% of maximum allocation size boundaries.
Verification Method:
System Test
Acceptance Criteria:
Artificially filling the local directory partition limits to 96% verification capacity prompts the immediate launch of a storage allocation caution message advising data clearance workflows.
Impact Keywords:
storage
partition
capacity
overwrite
disk
warning
technical
directory
Requirement ID: ALM-013
Title:
External USB File System Write Execution Failure Alert
Category:
Alarm Management
Priority:
Medium
Feature:
Data Export
Screens:
• SCR-021
Parameters:
• MAP
• CO
Related Risks:
• RSK-009
• RSK-008
Dependencies:
• USB Communication Mount Handler
Requirement:
The system shall throw an explicit data-export error toast confirmation window if a case logging transmission fails due to mid-stream media removal or bad sector allocation targets.
Verification Method:
Functional Test
Acceptance Criteria:
Yanking out an un-mounted USB flash disk accessory mid-way through a live data packet export routine aborts writing and displays a clear interface write failure warning.
Impact Keywords:
usb
export
write
failure
media
unplugged
toast
aborted
Requirement ID: ALM-014
Title:
HPI Smart Alerts Iterative Trend Prediction Validation
Category:
Alarm Management
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
• HPI Algorithm Engine
• Notification Service
Requirement:
The system shall process trending dynamics across consecutive algorithmic update cycles to generate intelligent HPI Smart Alerts regarding patient deterioration trajectories.
Verification Method:
System Test
Acceptance Criteria:
Feeding an unstable arterial waveform simulation into the monitor triggers predictive HPI Smart Alerts based on directional rate-of-change trend matching rules rather than static limits alone.
Impact Keywords:
smart
alerts
predictive
trending
trajectory
deterioration
rate
change
Requirement ID: ALM-015
Title:
Oximetry Cable Calibration Failure Warning
Category:
Alarm Management
Priority:
High
Feature:
Calibration Failure
Screens:
• SCR-015
• SCR-001
Parameters:
• StO₂
• SvO₂
• SQI
Related Risks:
• RSK-006
• RSK-005
Dependencies:
• HemoSphere Oximetry Cable
• ForeSight Oximeter Cable
Requirement:
The system shall immediately generate a low priority technical advisory error alert message if an in vitro or in vivo oximetry calibration check loop fails to validate successfully.
Verification Method:
Functional Test
Acceptance Criteria:
Simulating an optical calibration block fault or an unstable tissue measurement baseline during initialization triggers an explicit calibration failure error toast message on screen.
Impact Keywords:
calibration
failure
oximetry
cable
advisory
technical
validation
error
Validation Report
Requirements Processed: 15
Screens Mapped: 25
Risks Mapped: 23
Missing Screen References: 0
Missing Risk References: 0
Duplicate IDs: 0