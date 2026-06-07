Requirement ID: LOG-001
Title:
Clinical Intervention Event Logging
Category:
Audit and Logging
Priority:
High
Feature:
Voice Commands
Screens:
• SCR-005
Parameters:
• MAP
• CO
• CI
Related Risks:
• RSK-008
• RSK-001
Dependencies:
• System Logger Service
• Patient Data Storage
Requirement:
The system shall record user-entered physiological interventions and clinical events to an internal, non-volatile log file mapped directly to the open patient session.
Verification Method:
Functional Test
Acceptance Criteria:
Entering an intervention via the Events & Intervention screen generates a permanent, chronological log entry containing the event description and the active session ID.
Impact Keywords:
intervention
events
logging
history
chronological
clinical
entry
session
Requirement ID: LOG-002
Title:
Patient Data Modification Audit Trail Generation
Category:
Audit and Logging
Priority:
High
Feature:
Patient Monitoring
Screens:
• SCR-003
Parameters:
• BSA
Related Risks:
• RSK-006
• RSK-001
Dependencies:
• Patient Data Storage
• System Logger Service
Requirement:
The system shall log an audit trail entry within the internal system memory whenever patient identification profiles or physiological parameters (age, height, weight) are overwritten or updated.
Verification Method:
Security Test
Acceptance Criteria:
Modifying patient details on the Patient Data Screen captures the preceding values and new values inside the baseline logging partition.
Impact Keywords:
modification
audit
trail
demographics
overwrite
update
profile
history
Requirement ID: LOG-003
Title:
System Component Calibration Event Auditing
Category:
Audit and Logging
Priority:
High
Feature:
FloTrac Sensor
Screens:
• SCR-013
Parameters:
• MAP
• PAP
• CVP
Related Risks:
• RSK-006
• RSK-002
Dependencies:
• Calibration Service
• System Logger Service
Requirement:
The system shall capture all user-initiated sensor zeroing operations and multi-point oximetry calibration validation sequences within the active system operational history.
Verification Method:
Functional Test
Acceptance Criteria:
Completing an atmospheric pressure zero sequence or optical calibration process generates a system log detailing the target device identity, calibration status, and baseline adjustments.
Impact Keywords:
calibration
zeroing
auditing
sensor
validation
history
operational
adjustments
Requirement ID: LOG-004
Title:
Voice Control Event Transcription Logging
Category:
Audit and Logging
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
• System Logger Service
Requirement:
The system shall log the detected command phrase and execution success metrics within the active tracking log files whenever a touchless vocal utterance is registered.
Verification Method:
System Test
Acceptance Criteria:
Confirm that speaking the string "silence alarm" creates an explicit audit entry mapping the parsed vocal string pattern against the resultant action of pausing the audio transducer.
Impact Keywords:
voice
command
transcription
logging
touchless
utterance
parsed
action
Requirement ID: LOG-005
Title:
Gesture Recognition Interaction Tracking Audit
Category:
Audit and Logging
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
• Gesture Recognition Pipeline
• System Logger Service
Requirement:
The system shall generate a tracking entry within the internal communication logs specifying the context, gesture vector type, and dismissal confirmation parameters whenever a hand wave gesture alters screen configurations.
Verification Method:
Usability Test
Acceptance Criteria:
Executing an open-palm horizontal swipe path over low/medium alert banners creates a discrete chronological entry logging touchless banner interaction completion.
Impact Keywords:
gesture
interaction
tracking
audit
hand
wave
dismissal
vector
Requirement ID: LOG-006
Title:
ClearSight Alternate Cuff Switch Cycling Logging
Category:
Audit and Logging
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
• RSK-011
Dependencies:
• ClearSight Controller Module
• System Logger Service
Requirement:
The system shall log the automated or manual toggle actions switching pneumatic pressure routing paths between alternate dual-finger tracking rings.
Verification Method:
Functional Test
Acceptance Criteria:
The software logging service writes an explicit transition timestamp record confirming the valve line shift from primary to secondary cuff channels without missing continuous pressure outputs.
Impact Keywords:
clearsight
alternating
cuff
switch
cycling
pneumatic
valve
transition
Requirement ID: LOG-007
Title:
HPI Smart Alerts Configuration Modifiers Record
Category:
Audit and Logging
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
• System Logger Service
Requirement:
The system shall write an explicit audit marker tracing velocity changes and trend trajectory limits whenever a predictive configuration parameter is modulated.
Verification Method:
System Test
Acceptance Criteria:
Altering rate-of-change trend parameters triggers the generation of a specialized log packet recording algorithmic boundary settings inside non-volatile partitions.
Impact Keywords:
smart
alerts
configuration
modifiers
predictive
trajectory
algorithmic
boundary
Requirement ID: LOG-008
Title:
External USB Media Mount and Export Event Audit
Category:
Audit and Logging
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
• System Logger Service
Requirement:
The system shall record file system mount activities, target folder routing data, and file transmission quantities whenever case reports are targeted for external storage.
Verification Method:
Functional Test
Acceptance Criteria:
Inserting a flash disk accessory and triggering a case logging transfer generates immediate diagnostic entries confirming file system validation and media connectivity.
Impact Keywords:
usb
mount
export
audit
media
transmission
connectivity
transfer
Requirement ID: LOG-009
Title:
Swan-Ganz Smart Wedge Algorithmic Parsing Procedure Log
Category:
Audit and Logging
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
• PAP
Related Risks:
• RSK-012
• RSK-003
Dependencies:
• Smart Wedge Algorithm
• System Logger Service
Requirement:
The system shall write a comprehensive audit entry capturing the calculated Wedge Index score and the specific algorithm processing steps taken during a pulmonary artery occlusion pressure procedure.
Verification Method:
System Test
Acceptance Criteria:
Executing a PAOP wedge assessment generates a specialized database object logging the physical trace conversion metrics, final pressure calculations, and structural dampening criteria scores.
Impact Keywords:
wedge
index
paop
occlusion
dampening
procedure
algorithm
trace
Requirement ID: LOG-010
Title:
Target Alarm Boundary Adjustment Logging
Category:
Audit and Logging
Priority:
High
Feature:
Parameter Tiles
Screens:
• SCR-004
• SCR-001
Parameters:
• HPI
• MAP
• GHI
Related Risks:
• RSK-006
• RSK-006
Dependencies:
• Configuration Manager
• System Logger Service
Requirement:
The system shall log an audit log message within the patient session context whenever a physiological or predictive alarm threshold limit is modified by a clinician.
Verification Method:
Functional Test
Acceptance Criteria:
Altering an upper or lower boundary value for parameters like HPI or MAP creates an immediate chronological log documenting the prior threshold value, new threshold value, and parameter tile position.
Impact Keywords:
boundary
threshold
alarm
target
limit
modification
chronological
parameter
Validation Report
Requirements Processed: 10
Screens Mapped: 13
Risks Mapped: 16
Missing Screen References: 0
Missing Risk References: 0
Duplicate IDs: 0