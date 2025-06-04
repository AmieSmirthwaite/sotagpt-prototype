import streamlit as st

st.title("SotaGPT: Medical Device Intelligence Tool")

st.sidebar.header("Enter Device Details")

device_name = st.sidebar.text_input("Device Name")
intended_purpose = st.sidebar.text_area("Intended Purpose")
therapeutic_target = st.sidebar.text_input("Therapeutic Target")
treatment_indication = st.sidebar.text_input("Treatment Indication")
patient_population = st.sidebar.text_input("Patient Population")
disease_severity = st.sidebar.text_input("Disease Severity or Stage")

if st.sidebar.button("Generate Clinical Intelligence Report"):
    st.subheader(f"Report for {device_name}")

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

    st.markdown("### References")
    st.markdown("- [Meta-analysis on silver dressings](https://pubmed.ncbi.nlm.nih.gov/20361810/)")
    st.markdown("- [Clinical efficacy review](https://pubmed.ncbi.nlm.nih.gov/17353833/)")
    st.markdown("- [FDA Guidance](https://www.fda.gov/media/74063/download)")
