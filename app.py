import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# --- CONFIGURATION ---
# This is your specific Hugging Face model repository ID
MODEL_ID = "Nomi78600/gpt2-finetuned-articles"

# --- MODEL LOADING ---
@st.cache_resource
def load_model_and_tokenizer():
    """Load the tokenizer and model from Hugging Face."""
    try:
        tokenizer = GPT2Tokenizer.from_pretrained(MODEL_ID)
        model = GPT2LMHeadModel.from_pretrained(MODEL_ID)
        return tokenizer, model
    except Exception as e:
        st.error(f"Error loading model: {e}. Please ensure the repository ID '{MODEL_ID}' is correct and the model is public.")
        return None, None

tokenizer, model = load_model_and_tokenizer()

# --- STREAMLIT UI ---
st.set_page_config(page_title="GPT-2 Text Generator", layout="centered")

st.title("📝 Fine-Tuned GPT-2 Text Generator")
st.markdown(
    "This app uses a fine-tuned GPT-2 model to generate text based on the style of news articles. "
    "Enter a starting phrase below and see what the model comes up with!"
)

if model is not None and tokenizer is not None:
    with st.form("text_generation_form"):
        prompt_text = st.text_area("Enter your starting text (prompt):", "The price of oil", height=100)
        max_length = st.slider("Maximum length of generated text:", min_value=20, max_value=250, value=70)
        
        submitted = st.form_submit_button("Generate Text")

        if submitted:
            with st.spinner("Generating text..."):
                # Encode the prompt
                ids = tokenizer.encode(f'{prompt_text}', return_tensors='pt')

                # Generate text
                final_outputs = model.generate(
                    ids,
                    do_sample=True,
                    max_length=max_length,
                    pad_token_id=model.config.eos_token_id,
                    top_k=50,
                    top_p=0.95,
                )

                # Decode and display the output
                generated_text = tokenizer.decode(final_outputs[0], skip_special_tokens=True)
                
                st.subheader("Generated Text:")
                st.write(generated_text)
else:
    st.warning("Model could not be loaded. Please check the repository ID and application logs.")
