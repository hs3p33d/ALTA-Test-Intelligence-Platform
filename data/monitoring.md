Requirement ID: MON-001
Title:
Active Patient Session Monitoring Requirement
Category:
Monitoring
Priority:
Critical
Feature:
Patient Monitoring
Screens:
• SCR-001
• SCR-018
Parameters:
• MAP
• CO
• CI
• SV
• SVV
• PPV
• SVR
Related Risks:
• RSK-008
• RSK-001
Dependencies:
• Patient Data Storage
• Session Management
Requirement:
The system shall maintain an active patient monitoring session locally on the monitor until the patient monitoring session is explicitly ended by the user.
Verification Method:
System Test
Acceptance Criteria:
Verify that the patient session, including demographics and active tracking parameters, remains continuously open and stored locally without terminating automatically until manual termination is executed.
Impact Keywords:
patient
session
monitoring
storage
local
active
persistence
retention
Requirement ID: MON-002
Title:
Resuming Previous Patient Session
Category:
Monitoring
Priority:
High
Feature:
Patient Monitoring
Screens:
• SCR-018
Parameters:
• MAP
• CO
• CI
Related Risks:
• RSK-003
• RSK-008
Dependencies:
• Session Management
• Patient Data Storage
Requirement:
The system shall provide an option to resume a previous patient session via a "continue monitoring" selection on the Patient Data Screen.
Verification Method:
Functional Test
Acceptance Criteria:
Selecting the "continue monitoring" control successfully reloads and attaches incoming physiological data to the existing historical context of the prior session.
Impact Keywords:
continue
monitoring
resume
patient
session
historical
data
selection
Requirement ID: MON-003
Title:
Continuous Historical Trend Data Logging
Category:
Monitoring
Priority:
High
Feature:
Trend View
Screens:
• SCR-002
Parameters:
• MAP
• CO
• CI
• SV
• SVV
Related Risks:
• RSK-008
• RSK-003
Dependencies:
• Trend View
• Patient Data Storage
Requirement:
The system shall accumulate and record all monitored hemodynamic variables locally to compile continuous graphical and tabular timeline logs inside the Trend Monitoring View.
Verification Method:
System Test
Acceptance Criteria:
Opening the Trend Monitoring View reveals uninterrupted scrolling historical graphs containing every parameter tracked during the active patient record timeline.
Impact Keywords:
trend
historical
graphical
tabular
timeline
scroll
storage
logging
review
Requirement ID: MON-004
Title:
Automated Timestamp Recording of Historical Alarm Invocations
Category:
Monitoring
Priority:
Medium
Feature:
Alarm History
Screens:
• SCR-021
Parameters:
• MAP
• HPI
• GHI
Related Risks:
• RSK-008
• RSK-001
Dependencies:
• System Logger Service
• Patient Data Storage
Requirement:
The system shall automatically generate an immutable entry with a precise real-time timestamp into the local internal database whenever any physiological or technical alarm condition initializes or terminates.
Verification Method:
System Test
Acceptance Criteria:
Reviewing the compiled database output following a simulation sequence confirms exact chronological timestamp logging for every triggered high, medium, and low priority alarm event.
Impact Keywords:
timestamp
history
logging
database
immutable
chronological
export
record
Requirement ID: MON-005
Title:
Patient Demographics Verification and Association
Category:
Monitoring
Priority:
High
Feature:
Patient Monitoring
Screens:
• SCR-018
• SCR-025
Parameters:
• BSA
• CO
• CI
Related Risks:
• RSK-006
• RSK-001
Dependencies:
• Patient Data Storage
• Session Management
Requirement:
The system shall enforce verification of patient demographics, including age, weight, and height, to calculate Body Surface Area (BSA) prior to indexing flow parameters.
Verification Method:
Functional Test
Acceptance Criteria:
The system correctly computes BSA based on entered height and weight values and locks these demographics into the active patient monitoring record file.
Impact Keywords:
demographics
height
weight
bsa
patient
indexing
calculation
association
Requirement ID: MON-006
Title:
USB Flash Drive Historical Data Export Execution
Category:
Monitoring
Priority:
Medium
Feature:
Data Export
Screens:
• SCR-021
Parameters:
• MAP
• CO
• SV
Related Risks:
• RSK-008
• RSK-009
Dependencies:
• USB Interactivity Service
• Patient Data Storage
Requirement:
The system shall allow users to export compiled historical physiological data and alarm logs to an external USB flash drive via the Data Export Screen.
Verification Method:
Functional Test
Acceptance Criteria:
Inserting a compatible USB flash drive and executing the export command successfully copies the active patient session file in a standardized, uncorrupted format.
Impact Keywords:
usb
flash
drive
export
historical
logs
transfer
external
Requirement ID: MON-007
Title:
Assisted Fluid Management (AFM) Bolus Event History Storing
Category:
Monitoring
Priority:
High
Feature:
AFM
Screens:
• SCR-008
• SCR-024
Parameters:
• AFM
• SV
• SVV
Related Risks:
• RSK-008
• RSK-007
Dependencies:
• Advanced Analytics Module
• Patient Data Storage
Requirement:
The system shall commit every documented user-initiated fluid bolus event and its subsequent adaptive volume tracking metrics into the active patient historical log file.
Verification Method:
System Test
Acceptance Criteria:
Verify that each fluid bolus entered within the AFM interface registers an permanent entry in the system's local data log, paired with pre- and post-bolus stroke volume values.
Impact Keywords:
afm
bolus
fluid
history
storing
log
event
stroke
volume
Requirement ID: MON-008
Title:
Local Data Storage Capacity and Overwrite Management
Category:
Monitoring
Priority:
High
Feature:
Patient Monitoring
Screens:
• SCR-001
Parameters:
• MAP
• CO
Related Risks:
• RSK-008
• RSK-011
Dependencies:
• Patient Data Storage
• File System Service
Requirement:
The system shall manage its allocated local solid-state data storage partition to guarantee uncorrupted persistence of at least 72 hours of continuous patient monitoring data.
Verification Method:
Performance Test
Acceptance Criteria:
The platform preserves uninterrupted, high-frequency logging across a continuous 72-hour simulated operation window without experiencing file structure faults or buffer overflows.
Impact Keywords:
storage
capacity
partition
continuous
hours
persistence
logging
overflow
Requirement ID: MON-009
Title:
Spectrophotometric Oximetry In Vitro Calibration Factor Saving
Category:
Monitoring
Priority:
High
Feature:
Venous Oximetry
Screens:
• SCR-013
Parameters:
• SvO₂
• SQI
Related Risks:
• RSK-006
• RSK-005
Dependencies:
• HemoSphere Oximetry Cable
• Calibration Service
Requirement:
The system shall write and store derived in vitro spectrophotometric calibration reference coefficients into localized memory upon successful completion of the oximetry verification loop.
Verification Method:
Functional Test
Acceptance Criteria:
Completing an in vitro calibration sequence saves the unique optical reference parameters to memory, transitioning the calibration state status to verified.
Impact Keywords:
oximetry
calibration
in-vitro
spectrophotometric
coefficients
memory
saving
reference
Requirement ID: MON-010
Title:
Power Interruption Session State Data Recovery
Category:
Monitoring
Priority:
Critical
Feature:
Power Failure
Screens:
• SCR-001
Parameters:
• MAP
• CO
Related Risks:
• RSK-008
• RSK-011
Dependencies:
• Power Subsystem Monitor
• Session Management
Requirement:
The system shall automatically recover the active monitoring session state and recorded data points upon sudden loss and immediate restoration of primary AC line power.
Verification Method:
Performance Test
Acceptance Criteria:
Simulating a rapid cyclic power dropout results in the system booting straight back into the active monitoring environment, restoring the pre-failure trend line and patient identification file.
Impact Keywords:
power
interruption
dropout
recovery
session
state
restoration
persistence
Requirement ID: MON-011
Title:
Multi-Channel Bio-Sensor Disconnection Technical Alerts
Category:
Monitoring
Priority:
Critical
Feature:
Sensor Disconnect
Screens:
• SCR-001
• SCR-013
Parameters:
• MAP
• PAP
• CVP
Related Risks:
• RSK-002
• RSK-011
Dependencies:
• Technical Alert Monitor
• Sensor Connectivity Daemon
Requirement:
The system shall trigger a high-priority technical alarm sequence within 2 seconds of detecting physical link disengagement from any attached invasive pressure interface assembly.
Verification Method:
Functional Test
Acceptance Criteria:
Physically disconnecting an active monitoring cable assembly immediately prompts the display of an explicit visual disengagement string on the display bar alongside an audible warning pattern.
Impact Keywords:
disconnect
sensor
alarm
technical
latency
unplugged
hardware
alert
Requirement ID: MON-012
Title:
Touchless Voice Command Verification and Parse Logs
Category:
Monitoring
Priority:
High
Feature:
Voice Commands
Screens:
• SCR-001
• SCR-019
Parameters:
• HR
• MAP
Related Risks:
• RSK-010
• RSK-004
Dependencies:
• Voice Recognition Core
• System Logger Service
Requirement:
The system shall require multi-modal contextual parameters to be validated before executing high-impact settings adjustments requested via localized near-field voice command recognition loops.
Verification Method:
Usability Test
Acceptance Criteria:
Verifying vocal commands like alarm limit alterations demands secondary validation confirmation from the user, ensuring ambient hospital noise does not issue unintended configurations.
Impact Keywords:
voice
control
touchless
command
parsing
validation
ambient
noise
Requirement ID: MON-013
Title:
ClearSight Finger Cuff Alternate Cycling Control
Category:
Monitoring
Priority:
High
Feature:
ClearSight Technology
Screens:
• SCR-001
Parameters:
• NIBP
• MAP
Related Risks:
• RSK-013
• RSK-006
Dependencies:
• ClearSight Controller Module
• Pneumatic Valve Driver
Requirement:
The system shall automate rhythmic pressure switching cycles across a paired dual-cuff finger assembly to manage continuous noninvasive blood pressure monitoring intervals without causing local extremity congestion.
Verification Method:
Functional Test
Acceptance Criteria:
The controller seamlessly routes pressure lines back and forth across alternate digits at defined multi-hour operating boundaries without breaking active parameter calculation streams.
Impact Keywords:
clearsight
finger
cuff
cycling
pneumatic
alternating
pressure
ischemia
Requirement ID: MON-014
Title:
Customizable Parameter Tile Array Allocation
Category:
Monitoring
Priority:
Medium
Feature:
Parameter Tiles
Screens:
• SCR-001
• SCR-006
Parameters:
• MAP
• CO
• CI
• SV
• SVV
• PPV
Related Risks:
• RSK-004
• RSK-003
Dependencies:
• Display & Navigation Features
Requirement:
The system shall permit clinicians to select, swap, and configure specific individual physiological metrics within dedicated display tiles via the Parameter Configuration Menu.
Verification Method:
Usability Test
Acceptance Criteria:
The user can successfully add, remove, or rearrange parameter metrics on the active dashboard panel using direct tap actions on individual tiles.
Impact Keywords:
parameter
tile
customization
dashboard
display
layout
configuration
tile
Requirement ID: MON-015
Title:
Continuous Local Volumetric Trend Graphing
Category:
Monitoring
Priority:
High
Feature:
Trend View
Screens:
• SCR-002
Parameters:
• MAP
• CO
• CI
• SV
• SVV
Related Risks:
• RSK-008
• RSK-003
Dependencies:
• Trend View
• Patient Data Storage
Requirement:
The system shall accumulate and record all monitored hemodynamic variables locally to compile continuous graphical and tabular timeline logs inside the Trend Monitoring View.
Verification Method:
System Test
Acceptance Criteria:
Opening the Trend Monitoring View reveals uninterrupted scrolling historical graphs containing every parameter tracked during the active patient record timeline.
Impact Keywords:
trend
historical
graphical
tabular
timeline
scroll
storage
logging
review
Validation Report
Requirements Processed: 15
Screens Mapped: 21
Risks Mapped: 25
Missing Screen References: 0
Missing Risk References: 0
Duplicate IDs: 0