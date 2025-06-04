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

generate = st.button("Generate summary SOTA report")

if generate and product_name:
    st.subheader(f"Report for {product_name}")

    # Define dynamic content based on known product types
    if "hip" in product_name.lower():
        alternatives = [
            "Cemented hip arthroplasty",
            "Uncemented hip arthroplasty",
            "Hip resurfacing",
            "Conservative treatment (pain management, physiotherapy)"
        ]
        outcomes = {
            "Primary": [
                "Implant survivorship > 95% at 10 years",
                "Postoperative complication rate < 5%"
            ],
            "Secondary": [
                "Improvement in range of motion by 40%",
                "Pain reduction (VAS score improvement >3 points)"
            ]
        }
        requirements = {
            "Safety": ["Biocompatibility of implant materials", "Minimal risk of dislocation or loosening"],
            "Performance": ["Durability to 10 years under normal loading", "Stable fixation within 3 months"]
        }
        references = [
            "- [Registry data on hip implants](https://www.njrcentre.org.uk/)",
            "- [Hip arthroplasty outcomes meta-analysis](https://pubmed.ncbi.nlm.nih.gov/28320167/)"
        ]

    else:
        alternatives = [
            "Standard hydrofiber dressings (non-silver)",
            "Silver sulfadiazine cream",
            "Iodine-based dressings",
            "Negative pressure wound therapy"
        ]
        outcomes = {
            "Primary": [
                "Reduction in wound size (>50% reduction in 4 weeks)",
                "Resolution of infection (no signs of local infection in 2 weeks)"
            ],
            "Secondary": [
                "Pain reduction (VAS score improvement >2 points)",
                "Reduced dressing changes (from daily to every 3 days)"
            ]
        }
        requirements = {
            "Safety": ["Non-toxic silver release", "Biocompatibility"],
            "Performance": ["Effective exudate absorption for 72 hours", "Antimicrobial effect verified by lab testing"]
        }
        references = [
            "- [Meta-analysis on silver dressings](https://pubmed.ncbi.nlm.nih.gov/20361810/)",
            "- [Clinical efficacy review](https://pubmed.ncbi.nlm.nih.gov/17353833/)",
            "- [FDA Guidance](https://www.fda.gov/media/74063/download)"
        ]

    st.markdown("### Therapeutic Alternatives")
    st.write(alternatives)

    st.markdown("### Clinical Outcome Parameters and Acceptance Criteria")
    st.write(outcomes)

    st.markdown("### Safety and Performance Requirements")
    st.write(requirements)

    st.markdown("### References")
    for ref in references:
        st.markdown(ref)

    st.markdown("---")
    st.markdown("### Ask a Follow-up Question")
    user_query = st.text_input("What would you like to refine or ask about this output?")
    if user_query:
        st.markdown(f"*You asked:* {user_query}")
        st.info("(This is a placeholder — in a future version, this would trigger a real-time response or refinement based on your query.)")

elif generate:
    st.warning("Please provide at least the Device Name or Product Type.")
