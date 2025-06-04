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

    st.markdown("### Clinical Outcome Parameters and Acceptance Criteria")
    st.write({
        "Primary": [
            "Reduction in wound size (>50% reduction in 4 weeks)",
            "Resolution of infection (no signs of local infection in 2 weeks)"
        ],
        "Secondary": [
            "Pain reduction (VAS score improvement >2 points)",
            "Reduced dressing changes (from daily to every 3 days)"
        ]
    })

    st.markdown("### Safety and Performance Requirements")
    st.write({
        "Safety": ["Non-toxic silver release", "Biocompatibility"],
        "Performance": ["Effective exudate absorption for 72 hours", "Antimicrobial effect verified by lab testing"]
    })

    st.markdown("### References")
    st.markdown("- [Meta-analysis on silver dressings](https://pubmed.ncbi.nlm.nih.gov/20361810/)")
    st.markdown("- [Clinical efficacy review](https://pubmed.ncbi.nlm.nih.gov/17353833/)")
    st.markdown("- [FDA Guidance](https://www.fda.gov/media/74063/download)")

    st.markdown("---")
    st.markdown("### Ask a Follow-up Question")
    user_query = st.text_input("What would you like to refine or ask about this output?")
    if user_query:
        st.markdown(f"*You asked:* {user_query}")
        st.info("(This is a placeholder — in a future version, this would trigger a real-time response or refinement based on your query.)")

elif generate:
    st.warning("Please provide at least the Device Name or Product Type.")
