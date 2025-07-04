import streamlit as st
from transformers import pipeline, GPT2Tokenizer
import textwrap

# -------------------------
# Load model and tokenizer
# -------------------------
@st.cache_resource
def load_pipeline():
    generator = pipeline("text-generation", model="gpt2-medium")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return generator, tokenizer.eos_token_id

generator, eos_token_id = load_pipeline()

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(page_title="🧙‍♂️ GPT-2 Story Generator", layout="centered")

st.title("📖 GPT-2 Story Generator")
st.markdown("Craft compelling short stories with a fine-tuned GPT-2 model.")

# -------------------------
# Prompt Input
# -------------------------
prompt = st.text_area("📝 Start your story here:", "Once upon a time, in a magical forest,", height=120)

# -------------------------
# Generation Settings
# -------------------------
with st.expander("⚙️ Advanced Generation Settings"):
    max_new_tokens = st.slider("Max New Tokens", 50, 300, 120, step=10)
    temperature = st.slider("Temperature", 0.1, 2.0, 0.9, step=0.1)
    top_k = st.slider("Top-k Sampling", 0, 100, 70, step=5)
    top_p = st.slider("Top-p (Nucleus Sampling)", 0.1, 1.0, 0.95, step=0.05)
    repetition_penalty = st.slider("Repetition Penalty", 1.0, 2.0, 1.2, step=0.1)

# -------------------------
# Generate Button
# -------------------------
if st.button("✨ Generate Story"):
    with st.spinner("Generating..."):
        output = generator(
            prompt,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
            eos_token_id=eos_token_id
        )

        generated_text = output[0]["generated_text"]
        wrapped_text = textwrap.fill(generated_text, width=100)

    st.markdown("### Generated Story")
    st.code(wrapped_text)
