import streamlit as st

st.set_page_config(page_title="SotaGPT: Clinical Intelligence Tool", layout="centered")

st.title("SotaGPT: Medical Device Intelligence Tool")

st.markdown("### Start with Basic Details")

product_name = st.text_input("Device Name or Product Type")
intended_purpose = st.text_area("Intended Purpose")

# Expandable refinement section
with st.expander("Optional: Refine by Clinical Context"):
    therapeutic_target = st.text_input("Therapeutic Target")
    treatment_indication = st.text_input("Treatment Indication")
    patient_population = st.text_input("Patient Population")
    disease_severity = st.text_input("Disease Severity or Stage")

if st.button("Generate Clinical Intelligence Report") and product_name and intended_purpose:
    st.subheader(f"Report for {product_name}")

    st.markdown("### Therapeutic Alternatives")
    st.write([
        "Standard hydrofiber dressings (non-silver)",
        "Silver sulfadiazine cream",
        "Iodine-based dressings",
        "Negative pressure wound therapy"
    ])

    st.markdown("### Clinical Outcome Parameters")
    st.write({
        "Primary": ["Reduction in wound size", "Resolution of infection"],
        "Secondary": ["Pain reduction", "Less frequent dressing changes"]
    })

    st.markdown("### Safety and Performance Requirements")
    st.write({
        "Safety": ["Non-toxic silver release", "Biocompatibility"],
        "Performance": ["Effective exudate absorption", "Antimicrobial effect"]
    })

    st.markdown(
