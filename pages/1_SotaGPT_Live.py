import streamlit as st
import openai

st.set_page_config(page_title="SotaGPT: Real-Time SOTA Generator", layout="centered")

st.title("SotaGPT Live: Real-Time SOTA Summary Generator")

st.markdown("Enter a device or product type to retrieve a plausible SOTA report based on live medical knowledge.")

# User Input
device_query = st.text_input("Device Type or Product Name", placeholder="e.g., radiotherapy bead")

if st.button("Generate Live SOTA Report") and device_query:
    # Simulated real-time synthesis using GPT (for prototype purposes)
    prompt = f"""
    You are a clinical evidence analyst. Based on the device: '{device_query}', provide a plausible summary of:
    1. Therapeutic alternatives
    2. Clinical outcome parameters and typical acceptance criteria
    3. Safety and performance requirements
    4. Guidelines or regulatory references (fictional but plausible)
    Present results in clear bullet points for each section.
    """

    # Simulate AI generation
    with st.spinner("Generating plausible SOTA summary..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You summarize clinical device evidence."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        result = response.choices[0].message.content
        st.markdown("---")
        st.markdown("### Generated SOTA Report")
        st.markdown(result)

elif st.button("Generate Live SOTA Report"):
    st.warning("Please enter a device type or name first.")
