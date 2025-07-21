# GPT-2 Story Generator

Generate magical, coherent stories using the GPT-2 Medium language model with fine control over temperature, top-k, top-p, and repetition settings.

---

## Features

- **Text Generation** using GPT-2 Medium
-  Customizable generation controls:
  - `temperature` – creativity of the output
  - `top_k` / `top_p` – randomness control via sampling strategies
  - `max_new_tokens` – controls story length
- Clean UI with Streamlit
- Automatically adds natural ending using GPT-2's EOS token

---

## Tech Stack

- **Model**: [`gpt2-medium`](https://huggingface.co/gpt2-medium)
- **Frontend**: Streamlit
- **Backend**: Transformers by Hugging Face
- **Deployment**: Hugging Face Spaces (Streamlit SDK)

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/satyamkurum/gpt2-textgen/
cd gpt2-textgen
pip install -r requirements.txt
streamlit run app.py
```
## About Me
  Satyam Kurum
- Data Scientist | ML Developer | 2025 NITK Surathkal Graduate
- Passionate about GenAI, NLP, and creative machine learning apps

- You are free to use, modify, and distribute it with attribution.
