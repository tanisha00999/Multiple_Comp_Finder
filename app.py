import streamlit as st
from collections import Counter

# Dictionary containing project names and required components
projects = {
    "Smart Dustbin": ["Arduino", "Uno Cable", "Ultrasonic", "Dustbin", "Servo"],
    "Smart Blind Stick": ["Arduino", "Wire 2m", "Ultrasonic", "Pipe", "Buzzer", "Battery", "DC Snap"],
    "Automatic Toll Gate (IR based)": ["Arduino", "Uno Cable", "IR Sensor", "IR Sensor", "Servo"],
    "Light Sensitive Bulb": ["Arduino", "LDR", "Relay", "Bulb", "Wire", "Plug", "Bulb Holder"],
    "Missile Radar System": ["Arduino", "Servo", "Ultrasonic", "Ultrasonic Holder", "Arduino Cable"],
    "ECG Monitoring System": ["Arduino", "Arduino Cable", "ECG Sensor (AD8232)"],
    "Automatic House Light Bulb": ["Arduino", "Ultrasonic", "Relay", "Bulb", "Wire", "Plug", "Battery", "DC Snap", "Bulb Holder"],
    "Fingerprint Based Solenoid Lock": ["Arduino", "Fingerprint Sensor", "Relay", "Solenoid Lock", "12V Adapter", "Uno Cable"],
    "Ultrasonic Distance Monitoring": ["Arduino", "Ultrasonic", "LCD Display w/I2C 16x2", "Uno Cable"],
    "Automated Plant Watering System": ["Arduino", "Soil Moisture Sensor", "Relay", "Pump", "Diode (IN4007)", "Battery", "Switch"],
    "Automated Fan based Temperature Control": ["Arduino", "DHT11", "Relay", "DC Fan", "Diode (IN4007)", "Battery", "Switch"],
    "Humidity and Temperature Monitoring System": ["Arduino", "DHT11", "LCD Display w/I2C 16x2", "Uno Cable"],
    "Attendance System with Excel Sheet": ["Arduino", "RFID Card", "LCD Display w/I2C 16x2", "Uno Cable"],
    "Attendance System without Excel Sheet": ["Arduino", "RFID Card", "LCD Display w/I2C 16x2", "Uno Cable"],
    "Fire Alarm System": ["Arduino", "Flame Sensor", "Buzzer"],
    "LDR Based Security Box": ["Arduino", "LDR", "Buzzer", "Battery", "DC Snap"],
    "Smart Fire Extinguisher": ["Arduino", "Flame Sensor", "Relay", "Pump", "Diode (IN4007)", "Battery", "Switch"],
    "Smart Security Alarm System": ["PIR", "Diode (IN4007)", "Resistor 10k", "Battery", "Switch", "Buzzer"],
    "Edge Avoider Bot": ["Arduino Original", "IR Sensor", "Chassis", "Wheels", "DC Motor", "L298N", "Battery", "Battery Holder w/Switch", "Castor Wheel"],
    "Front Obstacle Avoider Bot": ["Arduino Original", "Ultrasonic", "Ultrasonic Holder", "Chassis", "Wheels", "DC Motor", "L298N", "Battery", "Battery Holder w/Switch"],
    "Bluetooth Controlled Bot": ["Arduino Original", "HC-05", "Chassis", "Wheels", "DC Motor", "L298N", "Battery", "Battery Holder w/Switch", "Castor Wheel"],
    "IoT in Agriculture": ["DHT11", "Soil Moisture Sensor", "LDR", "Pump", "Diode (IN4007)", "ESP8266", "Breadboard", "Micro-USB", "Dual Channel Relay", "Switch"],
    "Irrigation System": ["Soil Moisture Sensor", "Pump", "Diode (IN4007)", "ESP8266", "Breadboard", "Micro-USB", "Dual Channel Relay", "Switch"],
    "Home Automation using IoT": ["Bulb", "Wire", "Bulb Holder", "DC Fan", "Dual Channel Relay", "Switch", "ESP8266", "Breadboard", "Micro-USB"],
    "Weather Monitoring System": ["DHT11", "MQ135", "ESP8266", "Breadboard", "Micro-USB"],
    "Bluetooth Controlled Fan": ["DC Fan", "Relay", "Arduino", "HC-05", "Uno Cable"],
    "Bluetooth Controlled Light Bulb": ["Bulb", "Wire", "Bulb Holder", "Plug", "Relay", "Arduino", "HC-05", "Uno Cable"],
    "Laser Security System": ["Arduino", "Laser Module", "LDR", "Buzzer", "Battery", "DC Snap"],
    "Water Level Indicator": ["Arduino", "LCD Display w/I2C 16x2", "Uno Cable", "Water Level Sensor"],
    "Rain Alarm System": ["Rain Drop Sensor", "Buzzer", "Arduino", "Battery", "DC Snap"],
    "RFID Based Smart Door Lock": ["Arduino", "RFID Card", "LCD Display w/I2C 16x2", "Uno Cable", "Servo"],
    "Automatic Street Light": ["LDR", "IR Sensor", "LED", "Arduino", "Wire", "Battery", "DC Snap"],
    "Smart Car Parking System": ["Arduino", "Uno Cable", "IR Sensor", "Servo"],
    "Smart Bike Parking System": ["Arduino", "Uno Cable", "IR Sensor", "Servo"],
    "WiFi Control Door Lock (Solenoid)": ["Solenoid Lock", "12V Adapter", "Dual Channel Relay", "ESP8266", "Breadboard", "Micro-USB"],
    "WiFi Control Door Lock (Servo)": ["Servo", "Dual Channel Relay", "ESP8266", "Breadboard", "Micro-USB"],
    "Fire Alarm (without Arduino)": ["IR Receiver", "Diode (IN4007)", "Resistor 10k", "Battery", "Switch", "Buzzer"],
    "Passcode Based Lock (Solenoid)": ["Solenoid Lock", "12V Adapter", "Relay", "Arduino", "Uno Cable", "Keypad"],
    "Passcode Based Lock (Servo)": ["Servo", "Arduino", "Uno Cable", "Keypad"]
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
