import streamlit as st

st.set_page_config(page_title="SotaGPT: Clinical Intelligence Tool", layout="centered")

st.title("SotaGPT: Medical Device Intelligence Tool")

st.markdown("### Start with Basic Details")

product_name = st.text_input("Device Name or Product Type")

# Expandable refinement section
with st.expander("Optional: Refine by Clinical Context"):
    intended_purpose = st.text_area("Intended Purpose")
    therapeutic_target = st.text_input("Therapeutic Target")
    treatment_indication = st.text_input("Treatment Indication")
    patient_population = st.text_input("Patient Population")
    disease_severity = st.text_input("Disease Severity or Stage")

generate = st.button("Generate Clinical Intelligence Report")

if generate and product_name:
    st.subheader(f"Report for {product_name}")

    st.markdown("### Therapeutic Alternatives")
    st.write([
        "Standard hydrofiber dressings (non-silver)",
        "Silver sulfadiazine cream",
        "Iodine-based dressings",
        "Negative pressure wound therapy"
    ])

    st.markdown("### Clinical Outcome Parameters
