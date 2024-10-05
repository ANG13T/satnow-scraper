from rich import print
from rich.tree import Tree

subsystems = {
    "COMMAND & DATA HANDLING SYSTEMS": [
        "Atomic Clocks",
        "FPGAs",
        "Memory",
        "Microcontrollers",
        "On-Board Computers"
    ],
    "COMMUNICATIONS SYSTEMS": [
        "GNSS Receivers",
        "Satellite Antenna Systems",
        "Satellite Antennas",
        "Satellite Cameras",
        "Software Defined Radios",
        "Solid State Recorders",
        "Space Qualified Crystals",
        "Space Reflectors",
        "Space Transmitters",
        "Satellite Transponders"
    ],
    "LASER AND PHOTONICS": [
        "Laser Communication Terminals",
        "Optocoupler"
    ],
    "POWER SYSTEMS": [
        "Batteries",
        "Cryocoolers",
        "Power Conditioning and Distribution Units",
        "Power Processing Unit for Thrusters",
        "Satellite Electrical Power Systems",
        "Solar Cells",
        "Solar Panels"
    ],
    "SENSORS & ACTUATORS": [
        "Accelerometers",
        "Inertial Measurement Units",
        "Space Actuators",
        "Temperature Sensors"
    ],
    "SPACE MECHANISMS": [
        "Antenna Positioning Mechanisms",
        "Attach and Release Mechanisms",
        "Solar Array Drive Mechanisms"
    ],
    "SPACE SIMULATORS": [
        "ADCS Simulators",
        "GNSS Simulators",
        "Magnetic Field Simulators",
        "Star Tracker Simulators",
        "Sun Sensor Simulators"
    ],
    "THERMAL STRAPS": [
        "Thermal Straps"
    ],
    "PROPULSION SYSTEMS": [
        "Gimbals",
        "Propellant Tanks",
        "Spacecraft Valves",
        "Thrusters",
        "Bipropellant Thrusters",
        "Cold Gas Thrusters",
        "Electric Propulsion Thrusters",
        "Electrospray Thrusters",
        "Electrothermal Thruster",
        "Fiber-fed Pulsed Plasma Thrusters",
        "Gridded Ion Thrusters",
        "Hall Effect Thrusters",
        "HPGP Thrusters",
        "Hydrazine Thrusters",
        "RF Ion Thrusters",
        "Vacuum Arc Thrusters",
        "Warm Gas Thruster",
        "Water Resistojet"
    ],
    "BUS AND PLATFORMS": [
        "CubeSat Platforms",
        "MicroSat Platforms",
        "NanoSat Platforms",
        "Satellite Bus & Platforms",
        "SmallSat Platforms"
    ],
    "ELECTRICAL / ELECTRONIC COMPONENTS": [
        "Amplifiers",
        "Analog Phase Shifters",
        "Analog to Digital Converters",
        "Baluns",
        "Cable Assemblies",
        "Capacitors",
        "Circulators",
        "Comparators",
        "Couplers",
        "DC to DC Converters",
        "Digital Phase Shifters",
        "Diodes",
        "Diplexers",
        "Fixed Attenuators",
        "Frequency Synthesizers",
        "GaN Transistors",
        "Inductors",
        "Isolators",
        "LDO Voltage Regulators",
        "Log Detectors",
        "Mixers",
        "MOSFETs",
        "Multipliers",
        "Oscillators",
        "Power Dividers",
        "Power Transformers",
        "Resistors",
        "RF Connectors",
        "RF Filters",
        "Solid State Relays",
        "Switches",
        "Terminations",
        "Transistors",
        "Variable Attenuators"
    ],
    "ATTITUDE CONTROL & DETERMINATION SYSTEMS": [
        "ADCS Systems",
        "Control Moment Gyroscopes",
        "Earth/Horizon Sensors",
        "Magnetometers",
        "Magnetorquers",
        "Reaction Wheels",
        "Star Trackers",
        "Sun Sensors"
    ]
}

tree = Tree("[bold white]🛰️  SATELLITE SUBSYSTEMS", guide_style="bold #5f00ff")
# Iterate through the subsystems dictionary to add categories and components to the tree
for category, components in subsystems.items():
    # Add a branch for each category with a galaxy-like color
    category_branch = tree.add(f"[bold #a500ff]{category}")  # Neon purple for category

    # Add each component as a leaf under the category branch with cosmic hues
    for component in components:
        # Use a mix of cyan, magenta, and space-gray colors for components
        category_branch.add(f"[#00d7ff]{component}")  # Bright cyan for components (star-like glow)

# Display the tree using Rich's print function
print(tree)
