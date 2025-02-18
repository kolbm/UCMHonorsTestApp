import streamlit as st
import numpy as np

def calculate_period_frequency(rotations, time):
    T = time / rotations  # Period (s)
    f = 1 / T  # Frequency (Hz)
    return T, f

def calculate_angular_velocity(frequency):
    return 2 * np.pi * frequency  # Angular velocity (rad/s)

def calculate_tangential_velocity(radius, angular_velocity):
    return radius * angular_velocity  # Tangential velocity (m/s)

def calculate_centripetal_acceleration(velocity, radius):
    return velocity**2 / radius  # Centripetal acceleration (m/s²)

def calculate_centripetal_force(mass, acceleration):
    return mass * acceleration  # Centripetal force (N)

def calculate_max_speed_flat_curve(mu, radius, g=10):
    return np.sqrt(mu * g * radius)  # Max speed on a flat curve (m/s)

def calculate_bank_angle_velocity(radius, angle, g=10):
    return np.sqrt(radius * g * np.tan(np.radians(angle)))  # Safe speed on banked curve (m/s)

def calculate_apparent_weight_top_bottom(mass, velocity, radius, g=10):
    weight_top = mass * g - (mass * velocity**2 / radius)  # Apparent weight at top of hill (N)
    weight_bottom = mass * g + (mass * velocity**2 / radius)  # Apparent weight at bottom of dip (N)
    return weight_top, weight_bottom

# Streamlit UI
st.image("https://raw.githubusercontent.com/kolbm/UCMHonorsTestApp/main/Image%20Edits%20(1).png")
st.sidebar.header("Exam Sections")
section = st.sidebar.radio("Select a Topic", [
    "Period & Frequency",
    "Angular & Tangential Velocity",
    "Centripetal Acceleration & Force",
    "Flat & Banked Curve Motion",
    "Apparent Weight on Hills & Dips"
])

if section == "Apparent Weight on Hills & Dips":
    st.header("Calculate Apparent Weight on Hills & Dips")
    st.latex(r"W_{top} = mg - rac{m v^2}{r}")
    st.latex(r"W_{bottom} = mg + rac{m v^2}{r}")
    mass = st.number_input("Mass (kg)", min_value=0.01, step=0.01)
    velocity = st.number_input("Velocity (m/s)", min_value=0.01, step=0.01)
    radius = st.number_input("Radius (m)", min_value=0.01, step=0.01)
    if st.button("Calculate"):
        weight_top, weight_bottom = calculate_apparent_weight_top_bottom(mass, velocity, radius)
        st.write(f"**Apparent Weight at Top:** {weight_top:.3f} N")
        st.write(f"**Apparent Weight at Bottom:** {weight_bottom:.3f} N")
