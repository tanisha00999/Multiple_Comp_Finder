import streamlit as st
from collections import Counter

# Dictionary containing project names and required components
projects= {
    "Smart Security Alarm System": ["PIR", "Diode(IN4007)", "Transistor(BC547)", "Resistor_10k", "Battery", "Switch", "Buzzer", "Snap", "LED"],
    "Fire alarm (without Arduino)": ["Flame_Sensor", "Diode(IN4007)", "Resistor_10k", "Battery", "Switch", "Buzzer"],
    "Laser Security Alarm": ["BC547", "Laser Module", "LDR Module", "Buzzer", "Battery", "Snap", "LED", "Resistor_10k", "Switch"],
    "Climate Monitoring System": ["Arduino", "DHT11", "Lcd Display W/I2C 16*2", "Uno Cable"],
    "Fire Alarm System": ["Arduino", "Flame_Sensor", "Buzzer", "Battery", "DC Snap"],
    "Rain alarm system": ["Rain drop sensor", "Buzzer", "Arduino", "Battery", "DC Snap"],
    "Smart Dustbin": ["Arduino", "Uno Cable", "Ultrasonic", "Dustbin", "Servo"],
    "Ultrasonic Distance Monitoring": ["Arduino", "Ultrasonic", "Lcd Display W/I2C 16*2", "Uno Cable"],
    "Water Level Indicator": ["Arduino", "Lcd Display W/I2C 16*2", "Uno Cable", "Ultrasonic"],
    "Light Sensitive Bulb": ["Arduino", "LDR", "Relay", "Bulb", "Wire", "Plug", "Bulb_Holder", "Battery", "DC Snap"],
    "Missile Radar System": ["Arduino", "Servo", "Ultrasonic", "Ultrasonic_Holder", "Arduino_Cable"],
    "Motion-Based Light System": ["Arduino", "Ultrasonic", "Relay", "Bulb", "Wire", "Plug", "Battery", "DC Snap", "Bulb_Holder"],
    "Smart Blind Stick": ["Arduino", "Wire2m", "Ultrasonic", "Pipe", "Buzzer", "Battery", "DC Snap"],
    "IR-Based Automatic Toll Gate": ["Arduino", "Uno Cable", "IR_Sensor", "IR_Sensor", "Servo"],
    "Light-Based Security Box": ["Arduino", "LDR", "Buzzer", "Battery", "DC Snap"],
    "Self-Watering Plant System": ["Arduino", "Soil_Moisture Sensor", "Relay", "Pump", "Diode(IN4007)", "Battery", "Switch", "Snap", "Uno Cable"],
    "Temperature-Controlled Fan": ["Arduino", "DHT11", "Relay", "DC Fan", "Diode(IN4007)", "Battery", "Switch", "Snap", "Uno Cable"],
    "Attendance system without Excel Sheet": ["Arduino", "Rfid_Card", "Lcd Display W/I2C 16*2", "Uno Cable"],
    "RFID-based smart door lock (Servo)": ["Arduino", "Rfid_Card", "Lcd Display W/I2C 16*2", "Uno Cable", "Servo"],
    "Smart bike parking system": ["Arduino", "Uno Cable", "IR_Sensor", "IR_Sensor", "Servo"],
    "Smart car parking system": ["Arduino", "Uno Cable", "IR_Sensor", "IR_Sensor", "Servo"],
    "Smart Fire Extinguisher": ["Arduino", "Flame_Sensor", "Relay", "Pump", "Diode(IN4007)", "Battery", "Switch", "Snap", "Uno Cable"],
    "ECG Health Monitor": ["Arduino", "Uno Cable", "ECG_Sensor(Ad8232)"],
    "Automatic Street Light": ["LDR", "IR_Sensor", "LED", "Arduino", "Wire", "Battery", "DC Snap"],
    "Bluetooth Controlled Fan": ["DC_Fan", "Relay", "Arduino", "HC-05", "Uno Cable"],
    "Bluetooth controlled Light Bulb": ["Bulb", "Wire", "Bulb_Holder", "Plug", "Relay", "Arduino", "HC-05", "Uno Cable"],
    "Wifi control door lock (Servo)": ["Servo", "Dual_Channel Relay", "ESP8266", "Breadboard", "Breadboard", "Micro-USB"],
    "Passcode based lock(Servo)": ["Servo", "Arduino", "Uno Cable", "Keypad"],
    "Smart IoT Security System": ["ESP8266", "Breadboard", "Breadboard", "Micro-USB", "Ultrasonic", "Buzzer"],
    "Attendance system with Excel Sheet": ["Arduino", "Rfid_Card", "Lcd Display W/I2C 16*2", "Uno Cable"],
    "Weather Monitoring Station": ["DHT11", "MQ135", "LDR", "ESP8266", "Breadboard", "Breadboard", "Micro-USB"],
    "Automated Irrigation System": ["Soil_Moisture Sensor", "Pump", "Diode(IN4007)", "ESP8266", "Breadboard", "Breadboard", "Micro-USB", "Dual_Channel Relay", "Switch", "Battery", "Snap"],
    "Fingerprint Door Lock": [],
    "Wifi control door lock (Solenoid)": ["Solenoid Lock", "12V adapter", "DC jack female", "Dual_Channel Relay", "ESP8266", "Breadboard", "Breadboard", "Micro-USB"],
    "Passcode based lock (Solenoid)": ["Solenoid Lock", "12V adapter", "DC jack female", "Relay", "Arduino", "Uno Cable", "Keypad"],
    "Home Automation using IoT": ["Bulb", "Wire", "Bulb_Holder", "DC_Fan", "Dual_Channel Relay", "Switch", "ESP8266", "Breadboard", "Breadboard", "Micro-USB", "Snap", "Battery","DHT11"],
    "IoT Smart Farming System": ["DHT11", "Soil_Moisture Sensor", "LDR", "Pump", "Diode(IN4007)", "ESP8266", "Breadboard", "Breadboard", "Micro-USB", "Dual_Channel Relay", "Switch", "Snap", "Battery"],
    "Edge Avoider Bot": ["Arduino Original", "IR_Sensor", "IR_Sensor", "Chassis", "Wheels", "DCmotor", "L298n", "18650", "Battery Holder W/Switch", "Castor Wheel"],
    "Digital Compass": ["Arduino", "Uno Cable", "Lcd Display W/I2C 16*2", "HMC5883L"]
}



# Set Page Configuration
st.set_page_config(page_title="Multi-Project Component Finder", layout="centered")

# Custom CSS for UI Enhancements
st.markdown("""
    <style>
    .title { text-align: center; font-size: 36px; font-weight: bold; color: #4CAF50; }
    .subheader { text-align: center; font-size: 24px; font-weight: bold; color: #333; }
    .stButton button { background-color: #007BFF; color: white; font-size: 16px; }
    .stNumberInput { width: 80px; }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="title">Multi-Project Component Finder</p>', unsafe_allow_html=True)
st.write("### Select projects and specify the quantity for each")

# Select multiple projects
selected_projects = st.multiselect("Choose Projects", list(projects.keys()), help="Select one or more projects")

# Dictionary to store project quantities
project_quantities = {}

if selected_projects:
    st.write("### Specify Quantity for Each Selected Project")
    for project in selected_projects:
        project_quantities[project] = st.number_input(f"Quantity for {project}", min_value=1, value=1, step=1, key=project)

# Button to find components
if st.button("Find Required Components"):
    if not selected_projects:
        st.warning("⚠️ Please select at least one project.")
    else:
        # Collect components considering the quantity
        total_components = Counter()
        for project, quantity in project_quantities.items():
            for _ in range(quantity):  # Add components multiple times based on quantity
                total_components.update(projects[project])

        # Display results
        st.markdown('<p class="subheader">Total Components Required:</p>', unsafe_allow_html=True)
        
        # Display components in a table format
        component_list = [{"Component": component, "Quantity": count} for component, count in total_components.items()]
        st.table(component_list)

        # Success message
        st.success("✅ Component list generated successfully!")
