import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.email_generator import generate_email
from backend.auth import sign_up, log_in

st.set_page_config(page_title="AI Personalized Email Generator", layout="centered")

# --- SESSION STATE FOR LOGIN ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- LOGIN / SIGN-UP PAGE ---
def authentication_page():
    st.title("🔐 Login / Sign-Up")

    choice = st.radio("Select an option:", ["Log In", "Sign Up"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if choice == "Sign Up":
        if st.button("Sign Up"):
            success, message = sign_up(username, password)
            st.success(message) if success else st.error(message)

    elif choice == "Log In":
        if st.button("Log In"):
            success, message = log_in(username, password)
            if success:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(message)
                st.rerun()  # ✅ Fixed: Use st.rerun() instead of experimental_rerun()
            else:
                st.error(message)

# --- EMAIL GENERATOR PAGE ---
def email_generator_page():
    st.title("📧 AI Personalized Email Generator")
    st.write(f"Welcome, {st.session_state.username}! Generate professional emails effortlessly.")

    # --- LOGOUT BUTTON ---
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()  # ✅ Fixed: Use st.rerun()

    # --- EMAIL GENERATION FORM ---
    email_type = st.selectbox(
        "Select Email Type:", 
        [
            "job_application", "meeting_request", "leave_request", "follow_up",
            "thank_you", "apology", "introduction", "invitation", "recommendation", "friendly"
        ]
    )

    # Basic Inputs
    recipient = st.text_input("Recipient's Name:")
    sender = st.text_input("Your Name:")
    extra_inputs = {}

    if email_type == "job_application":
        extra_inputs["position"] = st.text_input("Job Position:")
        extra_inputs["company"] = st.text_input("Company Name:")
        extra_inputs["skills"] = st.text_input("Your Skills (comma-separated):")

    elif email_type == "meeting_request":
        extra_inputs["topic"] = st.text_input("Meeting Topic:")

    elif email_type == "leave_request":
        extra_inputs["date"] = st.text_input("Leave Date:")
        extra_inputs["reason"] = st.text_area("Reason for Leave:")

    elif email_type == "follow_up":
        extra_inputs["topic"] = st.text_input("Topic to Follow Up On:")

    elif email_type == "thank_you":
        extra_inputs["topic"] = st.text_input("Reason for Thank You:")

    elif email_type == "apology":
        extra_inputs["reason"] = st.text_area("Reason for Apology:")

    elif email_type == "introduction":
        extra_inputs["role"] = st.text_input("Your Role:")
        extra_inputs["company"] = st.text_input("Company Name:")
        extra_inputs["skills"] = st.text_input("Your Skills (comma-separated):")

    elif email_type == "invitation":
        extra_inputs["event"] = st.text_input("Event Name:")
        extra_inputs["date"] = st.text_input("Event Date:")
        extra_inputs["location"] = st.text_input("Event Location:")

    elif email_type == "recommendation":
        extra_inputs["person"] = st.text_input("Person Being Recommended:")
        extra_inputs["opportunity"] = st.text_input("Opportunity Name:")

    # Generate Email
    if st.button("Generate Email"):
        if recipient and sender and all(extra_inputs.values()):
            email = generate_email(email_type, recipient, sender, **extra_inputs)
            st.subheader("📩 Generated Email")
            st.write(f"**Subject:** {email['subject']}")
            st.text_area("Email Body", email["body"], height=250)
        else:
            st.warning("⚠️ Please fill in all fields.")

# --- DISPLAY LOGIN PAGE OR EMAIL GENERATOR ---
if not st.session_state.logged_in:
    authentication_page()
else:
    email_generator_page()

