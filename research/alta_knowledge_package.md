</think>

# BD HemoSphere Alta Monitoring Platform - Complete Knowledge Package

*Research Compiled: June 2026*  
*Source: Public BD Documentation, FDA 510(k), Operator's Manual, Product Pages*

---

## 1. Product Overview

### What BD HemoSphere Alta Is
The **HemoSphere Alta Advanced Monitoring Platform** is a next-generation hemodynamic monitoring system that leverages artificial intelligence and predictive algorithms to help clinicians anticipate hemodynamic instability before it occurs [web:1][web:3][web:7].

### Clinical Purpose
- Provide continuous hemodynamic monitoring with predictive AI-based algorithms
- Help clinicians proactively address instability in blood flow and pressure in critical situations [web:4][web:18]
- Enable individualized patient care through smart and predictive parameters [web:7]
- Predict hypotension events and optimize blood flow to avoid life-threatening situations during procedures [web:24][web:29]

### Intended Users
- Clinicians in surgical and non-surgical patient care settings
- Anesthesiologists, intensivists, and critical care providers
- Perioperative care teams [web:5]

### Intended Environment
- Operating rooms
- Critical care units (ICU)
- Perioperative care settings [web:5]

### Key Differentiators

| Feature | Differentiation |
|---------|-----------------|
| Predictive AI Algorithms | First platform with Hypotension Prediction Index (HPI), Cerebral Autoregulation Index (CAI), Global Hypoperfusion Index (GHI), and Assisted Fluid Management (AFM) [web:1][web:8] |
| Voice & Gesture Commands | Hands-free interaction for maintaining sterility (silencing alarms, switching views) [web:15][web:19] |
| High-Resolution 15" Display | Customizable touchscreen with split screen and cockpit views [web:7] |
| Multi-Sensor Support | Simultaneous monitoring with Acumen IQ, ForeSight IQ, Swan-Ganz IQ sensors [web:22][web:30] |
| Cerebral Autoregulation Index | First-of-its-kind parameter indicating brain blood flow stability [web:24] |

**Sources:** [web:1][web:3][web:4][web:7][web:18][web:19][web:24]

---

## 2. Complete Feature Inventory

### Predictive Analytics Features

| Feature Name | Description | User Value | Clinical Value | Source |
|--------------|-------------|------------|----------------|--------|
| **HPI** (Hypotension Prediction Index) | Predicts when a patient could have a low blood pressure event 15 minutes before onset | Early warning system for hypotension | Enables proactive intervention to prevent intraoperative hypotension | [web:4][web:8][web:22] |
| **AFM** (Assisted Fluid Management) | Predicts patient's responsiveness to fluid; adapts to each patient learning from each bolus | Optimizes fluid recommendations throughout procedure | Guides individualized fluid management for surgical patients | [web:22][manual:13.4] |
| **GHI** (Global Hypoperfusion Index) | Helps anticipate desaturations and global hypoperfusion events | Early detection of hypoperfusion | Enables intervention before cerebral desaturation events | [web:8][web:31][manual:13.2] |
| **CAI** (Cerebral Adaptive Index / Cerebral Autoregulation Index) | Quantifies relationship between MAP and StO₂; indicates whether brain maintains stable blood flow despite BP changes | Personalized blood pressure targets in real time | Deeper understanding of hemodynamic changes behind cerebral desaturation | [web:1][web:8][web:24][web:30] |

### Interaction Features

| Feature Name | Description | User Value | Clinical Value | Source |
|--------------|-------------|------------|----------------|--------|
| **Voice Commands** | Hands-free voice control for monitor interaction | Maintain sterility while operating monitor | Enables alarm silencing and view switching without breaking sterile field | [web:15][web:19][manual:4.5] |
| **Gesture Commands** | Hands-free gesture control for monitor navigation | Sterile operation capability | Reduces contamination risk during procedures | [web:15][manual:4.4] |
| **Smart Wedge** | Algorithm for PAOP measurement with wedge quality assessment (Wedge Index) | Automated wedge measurement with quality indicator | Ensures accurate PAOP measurements with validation | [web:9][manual:9.4.1] |

### Display & Navigation Features

| Feature Name | Description | User Value | Clinical Value | Source |
|--------------|-------------|------------|----------------|--------|
| **Clinical Tools Panel** | Access to HPI, AFM, GDT, Fluid Responsiveness Test, Derived Value Calculator, Events & Intervention | Centralized clinical decision support | Supports comprehensive hemodynamic management | [manual:4.6] |
| **Split Screen View** | Divided display showing multiple views simultaneously | Compare physiology and goal positioning | Simultaneous monitoring of multiple parameters | [manual:4.3.3] |
| **Cockpit View** | Consolidated dashboard view of key parameters | At-a-glance patient status overview | Rapid assessment of critical parameters | [manual:4.3.4] |
| **Trend View** | Graphical and tabular trend display with scroll mode | Historical parameter analysis | Identify trends and patterns in hemodynamic data | [manual:4.3.1] |
| **Parameter Tiles** | Configurable parameter display with alarm/target settings | Customizable monitoring interface | Tailor display to clinical needs | [manual:4.3.2] |

### Monitoring Technology Features

| Feature Name | Description | User Value | Clinical Value | Source |
|--------------|-------------|------------|----------------|--------|
| **Swan-Ganz Technology** | Continuous cardiac output (CCO), intermittent cardiac output (ICO), RV end diastolic volume (EDV) monitoring | Comprehensive right heart function assessment | Advanced hemodynamic monitoring with pulmonary artery catheterization | [manual:8] |
| **ClearSight Technology** | Noninvasive continuous blood pressure, cardiac output, stroke volume, SVR monitoring via finger cuff | Noninvasive hemodynamic monitoring | Avoids invasive catheterization risks | [manual:10] |
| **ForeSight Tissue Oximetry** | Cerebral and somatic tissue oxygenation (StO₂) monitoring | Continuous tissue oxygenation assessment | Early detection of cerebral desaturation | [manual:12] |
| **Venous Oximetry** | Oxygen saturation (SvO₂) monitoring via HemoSphere Oximetry Cable | Venous oxygen saturation tracking | Assess oxygen delivery/consumption balance | [manual:11] |
| **Pressure Cable Monitoring** | Vascular pressure monitoring with FloTrac, FloTrac Jr, Acumen IQ sensors, TruWave transducer | Arterial pressure monitoring | Accurate invasive blood pressure measurement | [manual:9] |
| **20-Second Flow Parameters** | Rapid cardiac output and hemodynamic parameter updates every 20 seconds | Near real-time hemodynamic data | Quick response to hemodynamic changes | [manual:8.2.6] |
| **STAT CO** | Rapid cardiac output measurement on demand | Immediate cardiac output data | Critical situation decision support | [manual:8.2.5] |
| **STAT EDV and RVEF** | Rapid right ventricular end-diastolic volume and ejection fraction | Immediate RV function assessment | Critical RV function monitoring | [manual:8.4.5] |

**Sources:** [manual:4.3-4.6][manual:8-13][web:8][web:22][web:30]

---

## 3. Complete Screen Inventory

### Main Monitoring Screens

| Screen Name | Purpose | Navigation Path | Key Controls | Data Displayed | User Actions | Source |
|-------------|---------|-----------------|--------------|----------------|--------------|--------|
| **Main Monitoring Screen** | Primary patient monitoring display | Default after patient selection | Parameter tiles, navigation bar, status bar | Vital parameters, waveforms, alarms | View parameters, configure alarms, navigate views | [manual:4.1-4.2] |
| **Trend Monitoring View** | Graphical and tabular historical data display | Menu → Trend View | Trend selection, scroll mode, graphical scales | Parameter trends over time, live BP waveform | Select trends, scroll, analyze patterns | [manual:4.3.1] |
| **Physiology Screen** (Split Screen) | Display physiological parameters in split view | Split Screen → Physiology | Split configuration | Hemodynamic parameters, waveforms | Configure split view, compare parameters | [manual:4.3.3.1] |
| **Goal Positioning Screen** | Goal-directed therapy target positioning | Split Screen → Goal Positioning | Goal targets, positioning controls | Target values, current values, deviation | Set goals, monitor progress | [manual:4.3.3.2] |
| **Cockpit Screen** | Consolidated dashboard view | Menu → Cockpit | Quick access controls | Key parameters at-a-glance | Rapid assessment, quick navigation | [manual:4.3.4] |
| **Parameter Configuration Menu** | Configure displayed parameters | Parameter tile → Change Parameters | Parameter selection, alarm settings | Available parameters list | Add/remove parameters, configure alarms | [manual:4.3.2] |

### Clinical Tools Screens

| Screen Name | Purpose | Navigation Path | Key Controls | Data Displayed | User Actions | Source |
|--------------|---------|-----------------|--------------|----------------|--------------|--------|
| **HPI Secondary Screen** | Detailed Hypotension Prediction Index analysis | Clinical Tools → HPI | HPI targets, smart alerts, smart trends | HPI value, relationship view, trends | Review HPI, configure alerts, analyze trends | [manual:4.6.1][manual:13.1] |
| **AFM Dashboard** | Assisted Fluid Management interface | Clinical Tools → AFM | Fluid tracking, bolus recommendations | Fluid responsiveness, recommendations | Track fluids, review recommendations | [manual:4.6.2][manual:13.4] |
| **Goal Directed Therapy (GDT)** | GDT protocol support screen | Clinical Tools → GDT | GDT targets, protocol steps | GDT parameters, protocol progress | Follow protocol, monitor progress | [manual:4.6.3] |
| **Fluid Responsiveness Test** | Test patient fluid responsiveness | Clinical Tools → Fluid Test | Test initiation, results display | Fluid responsiveness results | Conduct test, review results | [manual:4.6.4] |
| **Derived Value Calculator** | Calculate derived hemodynamic values | Clinical Tools → Calculator | Input values, calculation triggers | Calculated SVR, SVRI, etc. | Enter values, calculate derivatives | [manual:4.6.5] |
| **Events & Intervention** | Log events and interventions | Clinical Tools → Events | Event scrolling, intervention entry | Event history, intervention log | Add events, log interventions, scroll history | [manual:4.6.6] |

### Specialized Monitoring Screens

| Screen Name | Purpose | Navigation Path | Key Controls | Data Displayed | User Actions | Source |
|--------------|---------|-----------------|--------------|----------------|--------------|--------|
| **Zero & Waveform Screen** | Pressure zeroing and waveform confirmation | Pressure Monitoring → Zero | Zero sensor selection, waveform view | Pressure waveform, zero status | Zero sensor, confirm waveform | [manual:9.5] |
| **Thermodilution Summary Screen** | Intermittent CO thermodilution results | Swan-Ganz → ICO → Summary | Injectate volume, computation constant | CO values, thermodilution curves | Review CO, enter bolus data | [manual:8.3.4] |
| **Tissue Oximetry Physiology Screen** | ForeSight StO₂ monitoring display | Tissue Oximetry → Physiology | Averaging time, SQI display | StO₂ values, tHb, ΔctHb | Monitor tissue oximetry, calibrate | [manual:12.3.8] |
| **HPI Algorithm Side Panel** | HPI side panel with relationship view | HPI → Side Panel | Smart alerts, smart trends toggle | HPI trends, parameter relationships | Review HPI relationships, alerts | [manual:13.1.11] |

### Settings & Configuration Screens

| Screen Name | Purpose | Navigation Path | Key Controls | Data Displayed | User Actions | Source |
|--------------|---------|-----------------|--------------|----------------|--------------|--------|
| **Settings Menu** | User interface settings | Menu → Settings | Password protection, navigation | Display settings, patient data | Change settings, configure UI | [manual:5.1] |
| **Patient Data Screen** | Patient information management | Settings → Patient Data | New patient, continue monitoring | Patient ID, demographics | Enter/modify patient data | [manual:5.2] |
| **Alarms/Targets Screen** | Alarm and target configuration | Advanced Settings → Alarms | Silence alarms, set volume, targets | Alarm limits, target values | Configure alarms, set targets | [manual:6.1] |
| **Advanced Settings** | Advanced monitor configuration | Menu → Advanced Settings | Alarm targets, graphical scales, demo mode | System configurations | Configure advanced options | [manual:6] |
| **Data Export Screen** | Export monitoring data | Menu → Export Data | Export type selection (monitoring, case report, GDT, diagnostic) | Export options | Export data to external media | [manual:7.1] |

**Sources:** [manual:4][manual:5][manual:6][manual:7][manual:8-13]

---

## 4. Navigation Flow

### Main Navigation Structure

Login / Start Up
↓
Select Device ID
↓
New Patient / Continue Monitoring
↓
Patient Data Entry
↓
Main Monitoring Dashboard
├── → Trend View (graphical/tabular trends)
├── → Clinical Tools Panel
│   ├── → HPI Secondary Screen
│   ├── → AFM Dashboard
│   ├── → Goal Directed Therapy
│   ├── → Fluid Responsiveness Test
│   ├── → Derived Value Calculator
│   └── → Events & Intervention
├── → Split Screen (Physiology / Goal Positioning)
├── → Cockpit View
├── → Settings Menu
│   ├── → Patient Data
│   ├── → General Monitor Settings
│   ├── → Alarm/Targets Configuration
│   └── → Advanced Settings
└── → Data Export
├── → Monitoring Data
├── → Case Report
├── → GDT Report
└── → Diagnostic Export


### User Workflow for New Patient Monitoring

1. **Initial Start Up** - Power on monitor, select Device ID [manual:3.4]
2. **New Patient** - Enter patient data in Settings → Patient Data → New Patient [manual:5.2.1]
3. **Sensor Setup** - Connect appropriate sensor (Acumen IQ, ForeSight IQ, Swan-Ganz IQ, etc.) [manual:3.3.4][manual:8-12]
4. **Zero Calibration** - Zero pressure sensors if required [manual:9.2.3][manual:9.3.2]
5. **Begin Monitoring** - Main dashboard displays parameters [manual:4.1]
6. **Configure Parameters** - Use Parameter Tiles → Change Parameters [manual:4.3.2]
7. **Set Alarms/Targets** - Advanced Settings → Alarms/Targets → Configure Targets [manual:6.1]
8. **Review Trends** - Navigate to Trend View for historical analysis [manual:4.3.1]
9. **Use Clinical Tools** - Access HPI, AFM, GDT via Clinical Tools Panel [manual:4.6]
10. **Export Data** - Menu → Export Data → Select export type [manual:7.1]

### Screen Transitions

| From Screen | To Screen | Trigger | Source |
|-------------|-----------|---------|--------|
| Start Up | Device ID Selection | Power on | [manual:3.4.2] |
| Device ID | Patient Data | New Patient selection | [manual:5.2.1] |
| Patient Data | Main Dashboard | Patient data saved | [manual:5.2] |
| Main Dashboard | Trend View | Trend View button | [manual:4.3.1] |
| Main Dashboard | Clinical Tools | Clinical Tools button | [manual:4.6] |
| Main Dashboard | Settings | Settings button | [manual:5.1] |
| Any Screen | HPI Side Panel | HPI button | [manual:13.1.11] |
| Any Screen | Alarm Silence | Voice/gesture command or button | [manual:4.4][manual:4.5][manual:6.1.1] |

**Sources:** [manual:3.4][manual:4][manual:5][manual:6][manual:7]

---

## 5. Parameters Inventory

### Hemodynamic Parameters

| Parameter Name | Full Name | Unit | Clinical Purpose | Source |
|----------------|-----------|------|------------------|--------|
| **MAP** | Mean Arterial Pressure | mmHg | Average arterial pressure during cardiac cycle | [manual:1.8][web:22] |
| **CO** | Cardiac Output | L/min | Volume of blood pumped by heart per minute | [manual:1.8][manual:8] |
| **CI** | Cardiac Index | L/min/m² | Cardiac output normalized to body surface area | [manual:1.8][web:22] |
| **SV** | Stroke Volume | mL | Volume of blood pumped per heartbeat | [manual:1.8][web:22] |
| **SVV** | Stroke Volume Variation | % | Variation in stroke volume during respiratory cycle | [manual:1.8][web:22] |
| **PPV** | Pulse Pressure Variation | % | Variation in pulse pressure during respiratory cycle | [manual:1.8][web:22] |
| **SVR** | Systemic Vascular Resistance | dyn·s·cm⁻⁵ | Total resistance to blood flow in systemic circulation | [manual:1.8][web:22] |
| **SVRI** | Systemic Vascular Resistance Index | dyn·s·cm⁻⁵·m² | SVR normalized to body surface area | [manual:4.3.2.4] |
| **PAP** | Pulmonary Artery Pressure | mmHg | Pressure in pulmonary artery | [manual:1.8][manual:8] |
| **PAP_Sys** | Pulmonary Artery Pressure Systolic | mmHg | Systolic PAP | [manual:8] |
| **PAP_Dia** | Pulmonary Artery Pressure Diastolic | mmHg | Diastolic PAP | [manual:8] |
| **PAP_Mean** | Pulmonary Artery Pressure Mean | mmHg | Mean PAP | [manual:8] |
| **CVP** | Central Venous Pressure | mmHg | Pressure in central veins/right atrium | [manual:1.8][manual:4.3.2.4] |
| **RVP** | Right Ventricular Pressure | mmHg | Pressure in right ventricle | [manual:1.8] |
| **CO_RV** | Cardiac Output Right Ventricular | L/min | Right ventricular cardiac output | [manual:1.8][web:27] |
| **EDV** | End Diastolic Volume | mL | Right ventricular volume at end diastole | [manual:8.4] |
| **RVEF** | Right Ventricular Ejection Fraction | % | Right ventricular ejection fraction | [manual:8.4] |
| **PAOP** | Pulmonary Artery Occlusion Pressure | mmHg | Left atrial pressure estimate (wedge pressure) | [manual:9.4.1] |

### Predictive Analytics Parameters

| Parameter Name | Full Name | Unit | Clinical Purpose | Source |
|----------------|-----------|------|------------------|--------|
| **HPI** | Hypotension Prediction Index | 0-100 | Predicts hypotension 15 minutes before onset | [manual:13.1][web:22] |
| **AFM** | Assisted Fluid Management | Responsive/Non-responsive | Predicts fluid responsiveness | [manual:13.4][web:22] |
| **GHI** | Global Hypoperfusion Index | 0-100 | Predicts global hypoperfusion events | [manual:13.2][web:8] |
| **CAI** | Cerebral Adaptive Index (Cerebral Autoregulation Index) | 0-1 (or -1 to +1) | Quantifies cerebral autoregulation (MAP vs StO₂ relationship) | [manual:13.3][web:8][web:24] |

### Oximetry Parameters

| Parameter Name | Full Name | Unit | Clinical Purpose | Source |
|----------------|-----------|------|------------------|--------|
| **SpO₂** | Peripheral Oxygen Saturation | % | Peripheral arterial oxygen saturation | [manual:1.8] |
| **StO₂** | Tissue Oxygen Saturation | % | Cerebral/somatic tissue oxygen saturation | [manual:12][web:24] |
| **SvO₂** | Venous Oxygen Saturation | % | Mixed venous oxygen saturation | [manual:11] |
| **tHb** | Total Hemoglobin | g/dL | Calibrated systemic hemoglobin (continuous) | [manual:12.4][web:30] |
| **ΔctHb** | Relative Change in Total Hemoglobin | % | Change from baseline total hemoglobin | [manual:12.3.7] |

### Additional Parameters

| Parameter Name | Full Name | Unit | Clinical Purpose | Source |
|----------------|-----------|------|------------------|--------|
| **dP/dt** | Systolic Slope (Contractility) | mmHg/s | Measure of myocardial contractility | [web:22] |
| **Ea_dyn** | Dynamic Arterial Elastance (Afterload) | mmHg/mL | Measure of arterial afterload | [web:22] |
| **NIBP** | Non-Invasive Blood Pressure | mmHg | Noninvasive blood pressure (ClearSight) | [manual:10] |
| **HR** | Heart Rate | bpm | Heart beats per minute | [manual:1.8] |
| **Wedge Index** | Wedge Quality Index | 0-1 | Quality assessment of PAOP measurement | [manual:9.4.1.4] |
| **SQI** | Signal Quality Indicator | % | Signal quality for oximetry sensors | [manual:11.6][manual:12.3.6] |

**Sources:** [manual:1.8][manual:4.3.2][manual:8-13][web:22][web:24][web:30]

---

## 6. Sensors Inventory

### Smart Sensors (IQ Family)

| Sensor Name | Sensor Type | Clinical Purpose | Connected Parameters | Workflow | Source |
|-------------|-------------|------------------|---------------------|----------|--------|
| **Acumen IQ Sensor** | Arterial line smart sensor | Predictive hemodynamic monitoring with arterial line | HPI, AFM, MAP, CI, SV, SVV, PPV, SVR, dP/dt, Ea_dyn | Attaches to any existing arterial line; automatically calculates parameters every 20 seconds | [web:9][web:22][manual:9.2] |
| **ForeSight IQ Sensor** | Cerebral tissue oximetry sensor (forehead) | Cerebral and somatic tissue oxygenation monitoring | StO₂, tHb, ΔctHb, CAI | Placed on patient's forehead; enables CAI algorithm when combined with Acumen IQ | [web:9][web:24][web:30][manual:12] |
| **Swan-Ganz IQ Catheter** | Pulmonary artery catheter | Continuous cardiac output, right ventricular monitoring, wedge quality | CO, CI, PAP, CVP, RVP, CO_RV, EDV, RVEF, GHI, PAOP | Connects to Swan-Ganz technology; provides faster CO data, RV insights, wedge quality assessment | [web:16][web:31][web:33][manual:8] |

### Standard Sensors

| Sensor Name | Sensor Type | Clinical Purpose | Connected Parameters | Workflow | Source |
|-------------|-------------|------------------|---------------------|----------|--------|
| **FloTrac Sensor** | Arterial pressure sensor | Minimally-invasive cardiac output monitoring | CO, CI, SV, SVV, PPV, SVR, MAP | Connects to arterial line; set averaging time | [manual:9.2][web:16] |
| **FloTrac Jr Sensor** | Pediatric arterial pressure sensor | Pediatric cardiac output monitoring | CO, CI, SV, SVV, PPV, SVR, MAP | Pediatric version of FloTrac | [web:22][manual:9.2] |
| **TruWave Disposable Pressure Transducer (DPT)** | Pressure transducer | Invasive blood pressure monitoring | Arterial pressure, MAP | Connect to pressure cable; zero before use | [manual:9.3][web:22] |
| **VAMP Adult System** | Pressure monitoring system | Invasive blood pressure monitoring | Arterial pressure, MAP | Connect to pressure cable | [web:22] |
| **ClearSight Finger Cuff** | Noninvasive blood pressure cuff | Continuous noninvasive BP, CO monitoring | NIBP (continuous), CO, CI, SV, SVV, SVR, MAP | Apply to finger; select cuff size (single or double cuff) | [manual:10] |
| **ClearSight Heart Reference Sensor (HRS)** | Heart position sensor | Compensates for blood pressure changes due to heart position | BP accuracy correction | Apply to chest; calibrate before monitoring | [manual:10.1.4][manual:10.3] |
| **HemoSphere Oximetry Cable** | Venous oximetry sensor | Mixed venous oxygen saturation monitoring | SvO₂, tHb | In vitro and in vivo calibration required | [manual:11] |
| **ForeSight Oximeter Cable** | Tissue oximetry sensor | Cerebral/somatic tissue oximetry | StO₂, tHb, ΔctHb | Apply sensor to forehead; set averaging time | [manual:12] |
| **Alta Swan-Ganz Patient Cable** | Swan-Ganz catheter cable | Swan-Ganz technology monitoring | CO, CI, PAP, CVP, PAOP, EDV, RVEF | Connect Swan-Ganz catheter; zero and confirm waveform | [manual:8][manual:9.4] |

### Sensor Model Numbers (Acumen IQ)

| Model Number | Description | Length | Unit |
|--------------|-------------|--------|------|
| AIQS85 | Acumen IQ Sensor Standalone (5-Pack) | 84 in/213 cm | 5 |
| AIQS8C503 | Acumen IQ Sensor With TruWave DPT (5-Pack) | 84 in/213 cm | 5 |
| AIQS65 | Acumen IQ Sensor Standalone (5-Pack) | 60 in/152 cm | 5 |
| AIQS6AZ5 | Acumen IQ Sensor With VAMP Adult System | 60 in/152 cm | 5 |
| AIQS6C502 | Acumen IQ Sensor With TruWave DPT + VAMP Adult (5-Pack) | 60 in/152 cm | 5 |

**Sources:** [manual:8][manual:9][manual:10][manual:11][manual:12][web:16][web:22][web:30]

---

## 7. Analytics Inventory

### HPI (Hypotension Prediction Index)

| Attribute | Details |
|-----------|---------|
| **Purpose** | Predict hypotension event 15 minutes before it occurs |
| **Inputs** | Arterial waveform data (from Acumen IQ or FloTrac sensor), MAP, CI, SVV, PPV |
| **Outputs** | HPI value (0-100), HPI alarm, smart alerts, smart trends, relationship view |
| **User Workflow** | 1. Acumen IQ sensor connected to arterial line<br>2. HPI activates automatically<br>3. Review HPI value on main screen<br>4. Access HPI Secondary Screen for trends<br>5. Review HPI side panel with parameter relationships<br>6. Configure HPI alarm thresholds |
| **Screens** | Main Monitoring Screen, HPI Secondary Screen, HPI Algorithm Side Panel, Trend View |
| **Alarm** | Configurable HPI alarm threshold (default: 84); high alert notification available |
| **Source** | [manual:13.1][web:4][web:8][web:22] |

### AFM (Assisted Fluid Management)

| Attribute | Details |
|-----------|---------|
| **Purpose** | Predict patient's fluid responsiveness; adapt recommendations based on bolus responses |
| **Inputs** | Hemodynamic parameters (SV, CI, SVV, PPV), fluid bolus administration data |
| **Outputs** | Fluid responsiveness prediction (Responsive/Non-responsive), fluid tracking, bolus recommendations |
| **User Workflow** | 1. Acumen IQ sensor connected<br>2. Navigate to Clinical Tools → AFM<br>3. Enable fluid tracking (automatic with Acumen IQ Fluid meter)<br>4. Review AFM Dashboard for recommendations<br>5. System learns from each bolus to optimize future recommendations |
| **Screens** | AFM Dashboard, Clinical Tools Panel |
| **Indication** | Surgical patients only (not indicated for non-surgical) |
| **Source** | [manual:13.4][web:22] |

### GHI (Global Hypoperfusion Index)

| Attribute | Details |
|-----------|---------|
| **Purpose** | Anticipate global hypoperfusion events and cerebral desaturation |
| **Inputs** | SvO₂ (venous oximetry), StO₂ (tissue oximetry), hemodynamic parameters |
| **Outputs** | GHI value (0-100), GHI alarm, trend data |
| **User Workflow** | 1. Connect venous oximetry and/or tissue oximetry sensors<br>2. GHI calculates automatically<br>3. Review GHI value on main screen<br>4. Access GHI trends in Trend View<br>5. Configure GHI alarm threshold |
| **Screens** | Main Monitoring Screen, Trend View |
| **Alarm** | Configurable GHI alarm |
| **Sensor** | Swan-Ganz IQ catheter enables GHI with RV monitoring |
| **Source** | [manual:13.2][web:8][web:31] |

### CAI (Cerebral Adaptive Index / Cerebral Autoregulation Index)

| Attribute | Details |
|-----------|---------|
| **Purpose** | Quantify relationship between MAP and StO₂; indicate whether brain maintains stable blood flow despite BP changes |
| **Inputs** | MAP (from Acumen IQ), StO₂ (from ForeSight IQ sensor) |
| **Outputs** | CAI value (indicator of autoregulation status), personalized BP targets |
| **User Workflow** | 1. Connect ForeSight IQ sensor to patient's forehead<br>2. Connect Acumen IQ sensor to arterial line<br>3. CAI calculates automatically<br>4. Review CAI value on main screen<br>5. Use CAI for individualized BP target settings |
| **Screens** | Main Monitoring Screen, Trend View |
| **Differentiation** | First-of-its-kind parameter for cerebral autoregulation |
| **Source** | [manual:13.3][web:1][web:8][web:24][web:30] |

**Sources:** [manual:13.1][manual:13.2][manual:13.3][manual:13.4][web:1][web:4][web:8][web:22][web:24][web:30]

---

## 8. Alarm Management

### Alarm Types

| Alarm Type | Description | Examples | Source |
|------------|-------------|----------|--------|
| **Physiological Alarms** | Triggered by patient parameter values outside limits | HPI alarm, GHI alarm, MAP high/low, HR high/low, SpO₂ low, CAI alarm | [manual:6.1.1.1][manual:13.1.6] |
| **Technical Alarms** | Triggered by device/sensor issues | Sensor disconnect, cable disconnected, signal loss, calibration failure, battery low | [manual:6.1.1.2][manual:14] |

### Alarm Priorities

| Priority Level | Description | Indication |
|----------------|-------------|------------|
| **High Priority** | Critical conditions requiring immediate intervention | Life-threatening parameter values |
| **Medium Priority** | Conditions requiring prompt attention | Parameter values outside acceptable range |
| **Low Priority** | Advisory or informational alerts | Technical issues, calibration reminders |

**Source:** [manual:6.1] - *Note: Specific priority classifications referenced in alarm configuration*

### Alarm Behaviors

| Behavior | Description | How to Control | Source |
|----------|-------------|----------------|--------|
| **Alarm Acknowledgement** | User must acknowledge alarm to confirm awareness | Tap alarm on screen or use voice/gesture command | [manual:6.1.1] |
| **Alarm Silence** | Temporarily silence alarm audio | Voice command ("silence alarm"), gesture command, or Silence Alarms button | [manual:4.4][manual:4.5][manual:6.1.1] |
| **Alarm Persistence** | Visual alarm indicator persists until acknowledged | Visual indicator remains on screen | [manual:6.1] |
| **Alarm Volume Control** | Adjustable alarm audio volume | Settings → Alarms → Set Alarm Volume | [manual:6.1.2] |
| **Alarm Target Configuration** | Set upper/lower limits for each parameter | Advanced Settings → Alarms/Targets → Configure Targets | [manual:6.1.3][manual:6.1.5] |
| **Alarm History** | Log of past alarms with timestamps | Accessible via data export or alarm review screen | [manual:7.1] |

### Specific Alarm Features

| Feature | Description | Source |
|---------|-------------|--------|
| **HPI Alarm** | Configurable threshold (default 84); high alert notification available | [manual:13.1.6][manual:13.1.9] |
| **GHI Alarm** | Configurable threshold for global hypoperfusion | [manual:13.2.4] |
| **HPI Information Bar** | HPI indicator on information bar; can be disabled | [manual:13.1.7][manual:13.1.8] |
| **HPI Smart Alerts** | Intelligent alerting based on HPI trends | [manual:13.1.11.3] |
| **Alarm/Targets for One Parameter** | Configure individual parameter alarms | [manual:6.1.6] |
| **Configure All Targets** | Set all alarm targets simultaneously | [manual:6.1.5] |

**Sources:** [manual:4.4][manual:4.5][manual:6.1][manual:7.1][manual:13.1][manual:13.2]

---

## 9. User Workflows

### New Patient Monitoring Workflow

1. **Power On** - Press power button on monitor
2. **Select Device ID** - Choose device identifier from list [manual:3.4.2]
3. **New Patient** - Navigate to Settings → Patient Data → New Patient [manual:5.2.1]
4. **Enter Patient Data** - Input patient ID, demographics, height, weight, BSA
5. **Save Patient Data** - Confirm and save
6. **Connect Sensor** - Connect appropriate sensor (Acumen IQ, FloTrac, Swan-Ganz IQ, etc.) [manual:3.3.4]
7. **Zero Sensor** (if required) - Navigate to Zero & Waveform Screen → Zero Sensor [manual:9.5]
8. **Confirm Waveform** - Verify proper waveform display [manual:9.5.2]
9. **Begin Monitoring** - Main dashboard displays real-time parameters [manual:4.1]
10. **Configure Parameters** - Use Parameter Tiles → Change Parameters to customize display [manual:4.3.2]
11. **Set Alarm Limits** - Advanced Settings → Alarms/Targets → Configure All Targets [manual:6.1.5]
12. **Monitor Patient** - Review parameters, trends, and clinical tools

### Sensor Setup Workflow (Acumen IQ)

1. **Verify Arterial Line** - Ensure arterial line is properly placed and functioning [web:22]
2. **Connect Acumen IQ Sensor** - Attach to arterial line [manual:9.2.1]
3. **Connect to Monitor** - Plug sensor cable into HemoSphere Alta monitor [manual:3.3.4]
4. **Zero Arterial Pressure** - Navigate to Zero & Waveform Screen → Zero Sensor [manual:9.2.3]
5. **Verify Parameters** - Confirm HPI, MAP, CI, SV, SVV, PPV, SVR appear on screen [web:22]
6. **Set Averaging Time** (if needed) - Configure CO/Pressure averaging time [manual:5.5.0.2]
7. **Begin Monitoring** - HPI and AFM activate automatically [web:22]

### Sensor Replacement Workflow

1. **Prepare New Sensor** - Verify new sensor is compatible and undamaged
2. **Alert Team** - Notify care team of sensor change
3. **Disconnect Old Sensor** - Carefully disconnect from patient and monitor [manual:3.3.4]
4. **Connect New Sensor** - Attach new sensor to patient and monitor [manual:3.3.4]
5. **Zero New Sensor** - Zero pressure sensor if applicable [manual:9.2.3]
6. **Confirm Waveform** - Verify waveform appears correctly [manual:9.5.2]
7. **Verify Parameters** - Confirm all expected parameters are displaying
8. **Check Calibration** - Verify calibration status if applicable [manual:11.3][manual:12.4.5]

### Alarm Handling Workflow

1. **Alarm Sounds** - Audio and visual alarm activates [manual:6.1]
2. **Assess Patient** - Immediately assess patient condition
3. **Silence Alarm** (if appropriate) - Voice command ("silence alarm"), gesture, or button [manual:4.5]
4. **Acknowledge Alarm** - Tap alarm on screen to acknowledge [manual:6.1.1]
5. **Identify Cause** - Review parameter causing alarm, check sensor/cable
6. **Take Action** - Correct underlying issue (reposition sensor, treat patient, adjust limits)
7. **Document Event** - Use Events & Intervention tool to log alarm event [manual:4.6.6]
8. **Review Alarm History** - Access via data export if needed [manual:7.1.1]

### Trend Analysis Workflow

1. **Navigate to Trend View** - Menu → Trend View [manual:4.3.1]
2. **Select Parameters** - Trend Selection → Choose parameters to view [manual:4.3.1.3]
3. **Choose Time Range** - Select delta interval/averaging time [manual:5.5]
4. **Review Graphical Trend** - Analyze parameter trends over time [manual:4.3.1.1]
5. **Switch to Tabular** - Toggle between graphical/tabular scroll mode [manual:4.3.1.2]
6. **View Live BP Waveform** - Access live waveform display [manual:4.3.1.4]
7. **Identify Patterns** - Look for trends indicating hemodynamic changes
8. **Export Trend Data** - Menu → Export Data → Monitoring Data [manual:7.1.1]

### Analytics Review Workflow (HPI)

1. **Observe HPI Value** - Main screen displays HPI (0-100) [manual:13.1.4]
2. **Assess HPI Level** - High HPI (>84) indicates hypotension risk [manual:13.1.6]
3. **Navigate to HPI Secondary Screen** - Clinical Tools → HPI [manual:4.6.1]
4. **Review HPI Trends** - Analyze HPI trend over time [manual:13.1.11.3]
5. **Access Side Panel** - HPI Algorithm Side Panel → Relationship View [manual:13.1.11.1]
6. **Review Parameter Relationships** - Examine how MAP, SV, CI relate to HPI [manual:13.1.11.2]
7. **Check Smart Alerts** - Review smart alerts and smart trends [manual:13.1.11.3]
8. **Take Action** - Implement interventions to reduce hypotension risk
9. **Document** - Log intervention in Events & Intervention [manual:4.6.6.2]

### Data Export Workflow

1. **Navigate to Export** - Menu → Export Data [manual:7.1]
2. **Select Export Type**:
   - Monitoring Data (continuous monitoring data) [manual:7.1.1]
   - Case Report (comprehensive case summary) [manual:7.1.2]
   - GDT Report (Goal Directed Therapy data) [manual:7.1.3]
   - Diagnostic Export (device diagnostics) [manual:7.1.4]
3. **Insert Media** - Insert USB drive or connect network destination
4. **Configure Export Settings** - Select time range, parameters
5. **Initiate Export** - Start export process
6. **Verify Export** - Confirm data successfully exported
7. **Secure Data** - Remove media securely per HIPAA requirements [manual:7.4.4]

### System Recovery Workflow

1. **Power Failure** - Monitor switches to battery power automatically [manual:3.3.2]
2. **Software Restart** - Navigate to Settings → General → Restart (if available)
3. **Sensor Disconnect** - Technical alarm sounds; reconnect sensor and zero [manual:14]
4. **Network Failure** - Monitor continues local operation; data stored locally [manual:7.3]
5. **Invalid Data** - Check sensor connection, recalibrate if needed [manual:14]
6. **Calibration Failure** - Retry calibration; if persistent, replace sensor [manual:11.3.1][manual:12.4.7]

**Sources:** [manual:3][manual:4][manual:5][manual:6][manual:7][manual:9][manual:11][manual:12][manual:14][web:22]

---

## 10. Data Management

### Patient Data Storage

| Aspect | Description | Source |
|--------|-------------|--------|
| **Storage Location** | Patient data stored locally on monitor | [manual:5.2] |
| **Data Types** | Patient demographics, monitoring data, alarm history, events/interventions | [manual:5.2][manual:7.1] |
| **Session Management** | Active patient session maintained until patient monitoring ended | [manual:5.2.2] |
| **Continue Monitoring** | Option to resume previous patient session | [manual:5.2.2] |
| **View Patient Data** | Access stored patient information via Settings → Patient Data → View | [manual:5.2.3] |

### Data Export

| Export Type | Description | Format/Content | Source |
|-------------|-------------|----------------|--------|
| **Monitoring Data** | Continuous monitoring data export | Parameter values, timestamps, waveforms | [manual:7.1.1] |
| **Case Report** | Comprehensive case summary | Complete case data including parameters, events, alarm history | [manual:7.1.2] |
| **GDT Report** | Goal Directed Therapy report | GDT-specific data, targets, achievements | [manual:7.1.3] |
| **Diagnostic Export** | Device diagnostics data | System performance, error logs, calibration data | [manual:7.1.4] |

### Historical Data

| Aspect | Description | Source |
|--------|-------------|--------|
| **Trend Storage** | Historical parameter trends available in Trend View | [manual:4.3.1] |
| **Trend Display** | Graphical and tabular trend views with scroll mode | [manual:4.3.1.1][manual:4.3.1.2] |
| **Delta Intervals** | Configurable averaging time for CO/Pressure parameters | [manual:5.5][manual:5.5.0.2] |
| **Alarm History** | Log of all alarms with timestamps | [manual:7.1.1] |
| **Event History** | Events and interventions logged by user | [manual:4.6.6.1] |

### Data Retention

| Aspect | Description | Source |
|--------|-------------|--------|
| **Local Storage Duration** | Data retained on monitor until exported or storage full | [manual:7.1] |
| **Audit Logging** | System events, configuration changes, user actions logged | [manual:7.4] |
| **HIPAA Compliance** | Data handling compliant with HIPAA requirements | [manual:7.4.4] |

### Connectivity

| Feature | Description | Source |
|---------|-------------|--------|
| **HemoSphere Remote** | Web application for remote connectivity | [manual:7.3.1] |
| **Remote Pairing** | Pair monitor with HemoSphere Remote system | [manual:7.3.2] |
| **Wireless Settings** | Configure wireless network connectivity | [manual:7.2] |
| **Serial Port** | Serial port configuration for external devices | [manual:6.2] |

**Sources:** [manual:4.3.1][manual:5.2][manual:6.2][manual:7][manual:7.4.4]

---

## 11. Security

### Authentication

| Aspect | Description | Source |
|--------|-------------|--------|
| **Password Protection** | Settings menu password protected | [manual:5.1.1] |
| **Password Change** | Users can change passwords via Settings | [manual:5.1.1] |

### User Roles & Access Control

| Aspect | Description | Source |
|--------|-------------|--------|
| **User Roles** | Reference to user roles implied via password protection | [manual:5.1] |
| **Access Control** | Settings access restricted via password | [manual:5.1] |
| **Demo Mode** | Separate demo mode for training (password protected) | [manual:5.4] |

### Session Handling

| Aspect | Description | Source |
|--------|-------------|--------|
| **Session Persistence** | Patient session maintained until explicitly ended | [manual:5.2.2] |
| **Demo Mode Session** | Demo mode can be ended via Settings → Demo Mode → End | [manual:5.4.1] |

### Audit Trail

| Aspect | Description | Source |
|--------|-------------|--------|
| **Audit Logging** | System events and configuration changes logged | [manual:7.4] |
| **Diagnostic Export** | Audit data available via diagnostic export | [manual:7.1.4] |

### Cyber Security

| Aspect | Description | Source |
|--------|-------------|--------|
| **Cybersecurity Updates** | Regular security updates maintained | [manual:7.4.1] |
| **Vulnerability Management** | Vulnerability management program in place | [manual:7.4.2] |
| **Incident Response** | Cybersecurity incident response procedure | [manual:7.4.3] |
| **HIPAA Compliance** | Data handling compliant with HIPAA requirements | [manual:7.4.4] |

**Note:** Detailed security specifications (encryption methods, authentication protocols, specific user role definitions) were not found in publicly available documentation.

**Sources:** [manual:5.1][manual:5.4][manual:7.1.4][manual:7.4]

---

## 12. Recovery and Failure Handling

### Power Failure

| Scenario | System Behavior | Source |
|----------|-----------------|--------|
| **Main Power Loss** | Monitor automatically switches to battery power | [manual:3.3.2] |
| **Battery Indicator** | Battery status displayed in status bar | [manual:4.8.3] |
| **Low Battery Alarm** | Technical alarm triggers when battery low | [manual:14] |

### Software Restart

| Scenario | System Behavior | Source |
|----------|-----------------|--------|
| **Software Restart** | Available via Settings menu (if implemented) | [manual:5] |
| **Demo Mode Restart** | Demo mode can be ended via Settings → Demo Mode → End Demo | [manual:5.4.1] |

### Sensor Disconnect

| Scenario | System Behavior | Source |
|----------|-----------------|--------|
| **Sensor Disconnect** | Technical alarm sounds immediately | [manual:14] |
| **Reconnection** | User reconnects sensor and zeroes if required | [manual:9.2.3] |
| **Waveform Loss** | Waveform display shows loss of signal | [manual:9.5.2] |

### Network Failure

| Scenario | System Behavior | Source |
|----------|-----------------|--------|
| **Network Disconnection** | Monitor continues local operation | [manual:7.3] |
| **HemoSphere Remote Loss** | Remote connectivity lost; local monitoring continues | [manual:7.3.3] |
| **Data Queueing** | Data stored locally for later export | [manual:7.1] |

### Invalid Data

| Scenario | System Behavior | Source |
|----------|-----------------|--------|
| **Invalid Signal** | Signal Quality Indicator (SQI) shows poor quality | [manual:11.6][manual:12.3.6] |
| **Artifact Detection** | System may flag artifact in waveform | [manual:9.4.1.1] |
| **User Action** | Check sensor placement, rezero if needed | [manual:14] |

### Calibration Failure

| Scenario | System Behavior | Source |
|----------|-----------------|--------|
| **In Vitro Calibration Error** | Error message displayed; retry calibration | [manual:11.3.1] |
| **In Vivo Calibration Failure** | Error message; check sensor placement | [manual:11.4] |
| **tHb Calibration Failure** | Troubleshooting steps available; may require new sensor | [manual:12.4.7] |
| **Physiocal Method Display** | Shows calibration status for ClearSight | [manual:10.5] |

### Common Faults & Messages

| Fault Type | Description | Source |
|------------|-------------|--------|
| **Technical Faults** | Cable disconnected, sensor error, battery issues | [manual:14] |
| **Physiological Faults** | Parameter out of range, signal loss | [manual:14] |
| **Alerts** | Advisory messages for user attention | [manual:14] |
| **Troubleshooting** | Help menu with causes and suggested actions | [manual:14] |

**Sources:** [manual:3.3.2][manual:4.8.3][manual:5.4.1][manual:7.3][manual:9.5.2][manual:11.3.1][manual:12.4.7][manual:14]

---

## 13. Risks and Hazards

### Monitoring Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **Inaccurate Measurements** | Damaged or non-compatible accessories may cause inaccurate measurements | [manual:2.2] |
| **Delay in Diagnosis** | Misinterpretation of parameters may delay appropriate treatment | [manual:2.2] |
| **Signal Artifact** | Motion artifact or interference may cause inaccurate readings | [manual:12.3.3.2] |

### Sensor Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **Skin Damage** | ForeSight sensor may cause skin irritation at application site | [manual:12.3.1.1] |
| **Numbness/Tingling** | ClearSight finger cuff may cause discoloration, numbness, or tingling | [manual:10.1.5] |
| **Sensor Disconnect** | Disconnected sensor leads to loss of monitoring | [manual:2.2] |
| **Damaged Sensor** | Using damaged sensor may cause injury or inaccurate measurements | [manual:2.2] |

### Analytics Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **HPI False Positive** | HPI may predict hypotension that does not occur | [manual:13.1] |
| **HPI False Negative** | HPI may fail to predict actual hypotension event | [manual:13.1] |
| **AFM Misclassification** | AFM may incorrectly classify fluid responsiveness | [manual:13.4] |
| **Algorithm Limitations** | Algorithms validated for specific patient populations only | [manual:13.1.14][manual:13.1.15] |

### Alarm Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **Alarm Fatigue** | Excessive alarms may cause clinician desensitization | [manual:6.1] |
| **Alarm Silence Abuse** | Excessive alarm silencing may delay response to critical events | [manual:6.1.1] |
| **Incorrect Limits** | Improperly configured alarm limits may miss critical events | [manual:6.1.3] |

### User Action Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **Improper Zeroing** | Incorrect zeroing leads to inaccurate pressure measurements | [manual:9.2.3][manual:9.3.2] |
| **Wrong Sensor Size** | Incorrect cuff/sensor size causes inaccurate readings | [manual:10.2.2] |
| **Improper Calibration** | Incorrect calibration leads to unreliable data | [manual:11.3][manual:12.4.5] |
| **Delayed Intervention** | Relying solely on algorithms without clinical judgment | [manual:1.5] |

### Data Integrity Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **Data Loss** | Power failure before data export may result in data loss | [manual:7.1] |
| **Data Corruption** | Improper export may corrupt data | [manual:7.1] |
| **Privacy Breach** | Improper data handling may violate HIPAA | [manual:7.4.4] |

### Residual Risks

| Risk Description | Potential Impact | Source |
|------------------|------------------|--------|
| **Device Malfunction** | Despite testing, device may malfunction during use | [manual:2] |
| **Unforeseen Interference** | Unforeseen electromagnetic interference may affect readings | [manual:2.7] |

**Sources:** [manual:1.5][manual:2][manual:6.1][manual:7.1][manual:7.4.4][manual:9.2.3][manual:10.1.5][manual:11.3][manual:12.3.3.2][manual:12.4.5][manual:13.1][manual:13.4]

---

## 14. Testable Behaviors

### Functional Behaviors

| Feature | Testable Behavior | Category |
|---------|-------------------|----------|
| **HPI** | Calculates HPI value (0-100) from arterial waveform | Analytics |
| **HPI** | Triggers alarm when HPI exceeds configured threshold | Alarm |
| **HPI** | Updates HPI value in real-time (every 20 seconds) | Analytics |
| **AFM** | Predicts fluid responsiveness (Responsive/Non-responsive) | Analytics |
| **AFM** | Learns from each bolus to optimize recommendations | Analytics |
| **GHI** | Calculates GHI value from SvO₂/StO₂ data | Analytics |
| **CAI** | Calculates CAI from MAP and StO₂ relationship | Analytics |
| **Voice Commands** | Responds to voice command "silence alarm" | UI/Interaction |
| **Gesture Commands** | Responds to gesture for view switching | UI/Interaction |
| **Smart Wedge** | Measures PAOP automatically with wedge quality assessment | Monitoring |
| **20-Second Flow** | Updates CO/CI/SV/SVV/PPV every 20 seconds | Monitoring |
| **STAT CO** | Provides rapid CO measurement on demand | Monitoring |
| **Zero Pressure** | Successfully zeroes pressure sensor | Calibration |
| **Waveform Display** | Displays live BP waveform correctly | UI |
| **Trend View** | Displays parameter trends over selected time range | UI |

### UI Behaviors

| Feature | Testable Behavior | Category |
|---------|-------------------|----------|
| **Parameter Tiles** | Display configurable parameters correctly | UI |
| **Split Screen** | Divides screen correctly between two views | UI |
| **Cockpit View** | Displays consolidated key parameters | UI |
| **Clinical Tools Panel** | Opens and displays all clinical tool options | UI |
| **HPI Side Panel** | Opens with relationship view and trends | UI |
| **Navigation Bar** | Shows all navigation options correctly | UI |
| **Status Bar** | Displays Device ID, battery, notifications | UI |
| **Alarm Indicators** | Visual alarm indicator appears and persists | UI/Alarm |
| **Settings Menu** | Opens with password protection | UI/Security |
| **Export Menu** | Shows all export type options | UI |

### Workflow Behaviors

| Feature | Testable Behavior | Category |
|---------|-------------------|----------|
| **New Patient** | Patient data entry and save workflow completes | Workflow |
| **Sensor Connect** | Sensor recognized and parameters appear | Workflow |
| **Alarm Silence** | Alarm silences via voice/gesture/button | Workflow/Alarm |
| **Alarm Acknowledge** | Alarm acknowledged and visual indicator clears | Workflow/Alarm |
| **Trend Selection** | User can select and view parameter trends | Workflow |
| **Data Export** | Data exports successfully to USB/network | Workflow |
| **Continue Monitoring** | Previous patient session resumes correctly | Workflow |
| **Demo Mode** | Demo mode activates and deactivates correctly | Workflow |

### Error Handling Behaviors

| Feature | Testable Behavior | Category |
|---------|-------------------|----------|
| **Sensor Disconnect** | Technical alarm sounds on sensor disconnect | Error/Alarm |
| **Invalid Signal** | SQI shows poor quality on invalid signal | Error |
| **Calibration Failure** | Error message displayed on calibration failure | Error |
| **Low Battery** | Technical alarm and visual indicator on low battery | Error/Alarm |
| **Cable Disconnected** | Technical alarm on cable disconnection | Error/Alarm |
| **Invalid Data** | System flags artifact or invalid data | Error |
| **Network Failure** | Monitor continues local operation on network loss | Error |

### Alarm Behaviors

| Feature | Testable Behavior | Category |
|---------|-------------------|----------|
| **Physiological Alarm** | Triggers on parameter outside limits | Alarm |
| **Technical Alarm** | Triggers on device/sensor issue | Alarm |
| **Alarm Volume** | Adjustable via settings | Alarm |
| **Alarm Persistence** | Visual indicator persists until acknowledged | Alarm |
| **HPI Alarm** | Triggers at configured threshold (default 84) | Alarm |
| **GHI Alarm** | Triggers at configured threshold | Alarm |
| **Alarm History** | Records all alarms with timestamps | Alarm |

### Analytics Behaviors

| Feature | Testable Behavior | Category |
|---------|-------------------|----------|
| **HPI Smart Alerts** | Generates intelligent alerts based on trends | Analytics |
| **HPI Smart Trends** | Displays smart trend visualization | Analytics |
| **HPI Relationship View** | Shows parameter relationships in side panel | Analytics |
| **AFM Fluid Tracking** | Automatically tracks volume and flow rate | Analytics |
| **GHI Calculation** | Calculates from SvO₂/StO₂ inputs | Analytics |
| **CAI Calculation** | Calculates from MAP/StO₂ inputs | Analytics |

**Sources:** [manual:4][manual:5][manual:6][manual:7][manual:9][manual:11][manual:12][manual:13][manual:14]

---

## 15. Traceability Foundation

### Feature → Screen Mapping

| Feature | Primary Screen | Secondary Screens |
|---------|---------------|-------------------|
| HPI | Main Monitoring Screen | HPI Secondary Screen, HPI Side Panel, Trend View |
| AFM | Clinical Tools Panel | AFM Dashboard |
| GHI | Main Monitoring Screen | Trend View |
| CAI | Main Monitoring Screen | Trend View |
| Voice Commands | All screens (global) | - |
| Gesture Commands | All screens (global) | - |
| Smart Wedge | Zero & Waveform Screen | PAOP Measurement Screen |
| Split Screen | Split Screen View | Physiology Screen, Goal Positioning Screen |
| Cockpit View | Cockpit Screen | - |
| Trend View | Trend Monitoring View | - |
| Clinical Tools | Clinical Tools Panel | All clinical tool screens |

### Feature → Parameter Mapping

| Feature | Parameters |
|---------|------------|
| HPI | HPI, MAP, CI, SV, SVV, PPV, SVR, dP/dt, Ea_dyn |
| AFM | SV, CI, SVV, PPV, fluid bolus data |
| GHI | GHI, SvO₂, StO₂, CO, CI |
| CAI | CAI, MAP, StO₂ |
| Swan-Ganz | CO, CI, PAP, CVP, RVP, CO_RV, EDV, RVEF, PAOP |
| ForeSight | StO₂, tHb, ΔctHb |
| ClearSight | NIBP, CO, CI, SV, SVV, SVR, MAP |
| FloTrac | CO, CI, SV, SVV, PPV, SVR, MAP |

### Feature → Sensor Mapping

| Feature | Sensor(s) |
|---------|-----------|
| HPI | Acumen IQ Sensor, FloTrac Sensor, FloTrac Jr Sensor |
| AFM | Acumen IQ Sensor |
| GHI | Swan-Ganz IQ Catheter, HemoSphere Oximetry Cable |
| CAI | ForeSight IQ Sensor + Acumen IQ Sensor |
| Swan-Ganz Monitoring | Swan-Ganz IQ Catheter, Alta Swan-Ganz Patient Cable |
| Tissue Oximetry | ForeSight IQ Sensor, ForeSight Oximeter Cable |
| ClearSight | ClearSight Finger Cuff, ClearSight Heart Reference Sensor |
| Arterial Pressure | Acumen IQ Sensor, FloTrac Sensor, TruWave DPT |

### Feature → Workflow Mapping

| Feature | Workflow(s) |
|---------|-------------|
| New Patient Monitoring | New Patient, Sensor Setup, Alarm Configuration |
| Sensor Setup | Sensor Setup Workflow (Acumen IQ, FloTrac, Swan-Ganz, ForeSight, ClearSight) |
| Sensor Replacement | Sensor Replacement Workflow |
| Alarm Handling | Alarm Handling Workflow |
| Trend Analysis | Trend Analysis Workflow |
| Analytics Review | HPI Review Workflow, AFM Review Workflow |
| Data Export | Data Export Workflow |
| System Recovery | Power Failure, Software Restart, Sensor Disconnect workflows |

### Feature → Risk Mapping

| Feature | Associated Risk(s) |
|---------|-------------------|
| HPI | False positive/negative predictions, algorithm limitations |
| AFM | Misclassification of fluid responsiveness, surgical patient limitation |
| GHI | Inaccurate hypoperfusion prediction |
| CAI | Limited validation population |
| Voice Commands | False recognition, sterility breach |
| Smart Wedge | Inaccurate PAOP if wedge quality poor |
| ClearSight | Numbness/tingling, discoloration of fingertip |
| All Analytics | Over-reliance on algorithms without clinical judgment |

### Feature → Alarm Mapping

| Feature | Alarm Type(s) |
|---------|--------------|
| HPI | HPI alarm (configurable threshold), high alert notification |
| GHI | GHI alarm (configurable threshold) |
| CAI | CAI alarm (if configured) |
| All Parameters | Physiological alarms (high/low limits) |
| Sensor Disconnect | Technical alarm |
| Low Battery | Technical alarm |
| Calibration Failure | Technical alarm |
| Signal Loss | Technical alarm |

### Feature → Analytics Mapping

| Feature | Analytics Type |
|---------|--------------|
| HPI | Predictive algorithm (15-min hypotension prediction) |
| AFM | Predictive algorithm (fluid responsiveness) |
| GHI | Predictive algorithm (hypoperfusion prediction) |
| CAI | Analytical algorithm (autoregulation quantification) |
| Smart Wedge | Analytical algorithm (wedge quality assessment) |
| tHb | Analytical algorithm (continuous hemoglobin) |

**Sources:** [manual:4][manual:8][manual:9][manual:10][manual:11][manual:12][manual:13][web:22][web:24][web:30]

---

## 16. Source Library

### Primary Documentation

| Source Type | Title/Description | URL |
|-------------|-------------------|-----|
| **Operator's Manual** | HemoSphere Alta Advanced Monitoring Platform Operator's Manual (v2.1, September 2024) | https://eifu.edwards.com/eifu/5970f1b346e0fb00015e5f4d/DOC-0251933A.pdf [manual] |
| **FDA 510(k)** | FDA 510(k) K252533 - HemoSphere Alta Advanced Monitoring Platform | https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252533.pdf [web:2] |

### BD Product Pages

| Source Type | Title | URL |
|-------------|-------|-----|
| Product Page | HemoSphere Alta™ Monitor (US) | https://www.bd.com/en-us/products-and-solutions/products/product-families/hemosphere-alta-monitor [web:3][web:7] |
| Product Page | HemoSphere Alta™ Monitor (UK) | https://www.bd.com/en-uk/products-and-solutions/products/product-families/hemosphere-alta-monitor [web:6] |
| Product Page | HemoSphere Alta™ Monitor (South Africa) | https://www.bd.com/en-za/products-and-solutions/products/product-families/hemosphere-alta-monitor [web:3] |
| Product Page | Acumen IQ™ Sensor | https://www.bd.com/en-us/products-and-solutions/products/product-families/acumen-iq-sensor [web:22] |
| Solution Page | Advanced Hemodynamic Monitoring Solutions | https://www.bd.com/en-us/products-and-solutions/solutions/advanced-hemodynamic-monitoring-solutions [web:30] |

### Clinical Education Resources

| Source Type | Title | URL |
|-------------|-------|-----|
| Clinical Education | Advanced Monitoring Clinical Education | https://www.bd.com/en-us/products-and-solutions/solutions/clinical-education [web:5] |

### Press Releases & News Articles

| Source Type | Title | URL | Publish Date |
|-------------|-------|-----|--------------|
| Press Release | BD Launches Next Generation Hemodynamic Monitoring Solution | https://investors.bd.com/news-events/press-releases/detail/881 | 2025-04-20 [web:18] |
| Press Release | BD Launches Next Generation Hemodynamic Monitoring Solution (PR Newswire) | https://www.prnewswire.com/news-releases/bd-launches-next-generation-hemodynamic-monitoring-solution | 2025-04-21 [web:19] |
| Press Release | BD Unveils HemoSphere Alta Advanced Monitoring Platform With Predictive, AI Based Algorithms | https://news.futunn.com/en/post/55743308/bd-unveils-hemosphere-alta-advanced-monitoring-platform-with-predictive-ai [web:4] | 2025-04-20 |
| Article | BD Launches HemoSphere Alta: AI-Powered System Redefines Hemodynamic Monitoring | https://patrickwareing.com/news/bd-launches-hemosphere-alta-ai-powered-system-redefines-hemodynamic-monitoring/ | 2025-05-22 [web:1] |
| Article | BD launches next-gen AI-powered hemodynamic monitoring tech | https://www.massdevice.com/bd-launches-next-gen-ai-hemodynamic-monitoring/ | 2025-04-20 [web:9] |
| Article | HemoSphere Alta by BD Brings AI-Driven Hemodynamic Monitoring | https://xtalks.com/hemosphere-alta-by-bd-brings-ai-driven-hemodynamic-monitoring-4205/ | 2025-04-23 [web:8] |
| Article | Exploring AI-Powered Hemodynamic Monitoring with BD's HemoSphere Alta | https://www.mpo-mag.com/exclusives/exploring-ai-powered-hemodynamic-monitoring-with-bds-hemosphere-alta/ | 2025-08-18 [web:15] |
| Article | BD Unveils HemoSphere Alta Advanced Monitoring Platform (German) | https://www.finanznachrichten.de/nachrichten-2025-04/65163603-bd-unveils-hemosphere-alta-advanced-monitoring-platform-020.htm | 2
