# Fine-Tuned GPT-2 News Article Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR_STREAMLIT_APP_URL_HERE)

A web application built with Streamlit that uses a fine-tuned GPT-2 model to generate text in the style of news articles.

## 🚀 Live Demo

Once deployed, you can access the live application at your Streamlit Cloud URL.

## 📖 Description

This project demonstrates the end-to-end process of fine-tuning a GPT-2 language model on a custom dataset of news articles. The fine-tuned model is then deployed as an interactive web application using Streamlit Cloud, allowing users to input a prompt and receive a uniquely generated text passage.

The core of the project is the fine-tuned model, which has learned the vocabulary, tone, and structure of news writing from the training data.

## ✨ Features

- **Interactive UI:** A simple and intuitive web interface powered by Streamlit.
- **Custom Text Generation:** Generates text based on user-provided prompts.
- **Adjustable Length:** Users can control the maximum length of the generated text.
- **Fine-Tuned Model:** Utilizes a GPT-2 model specifically adapted for generating news-style content.
- **Cloud-Native:** Deployed on Streamlit Cloud for easy public access.

## 🛠️ Tech Stack

- **Model:** GPT-2 (Generative Pre-trained Transformer 2)
- **Framework:** PyTorch
- **MLOps & Hosting:** Hugging Face (Model Hub), Streamlit (Web Framework & Cloud Deployment)
- **Core Libraries:** `transformers`, `torch`, `streamlit`

## 🧠 The Model

The base model is `gpt2`, which has been fine-tuned on a dataset of news articles. The fine-tuning process adapted the model to better predict text sequences that mimic the style of journalism.

The model is hosted on the Hugging Face Hub and can be found here:
- **[Nomi78600/gpt2-finetuned-articles](https://huggingface.co/Nomi78600/gpt2-finetuned-articles)**

## ⚙️ Setup and Deployment

To deploy your own instance of this application, follow these steps:

### Prerequisites

- A [GitHub](https://github.com/) account.
- A [Hugging Face](https://huggingface.co/) account.
- A [Streamlit Cloud](https://share.streamlit.io/) account.
- A Hugging Face Access Token with at least `read` permissions.

### Deployment Steps

1.  **Push to GitHub:**
    - Create a new repository on your GitHub account.
    - Upload the following three files to it:
      - `app.py`
      - `requirements.txt`
      - `.gitignore`

2.  **Deploy on Streamlit Cloud:**
    - Log in to your Streamlit Cloud account.
    - Click **"New app"** and select the GitHub repository you just created.
    - Ensure the main file path is set to `app.py`.

3.  **Add Secrets:**
    - In your app's settings on Streamlit Cloud, navigate to the **"Secrets"** tab.
    - Add your Hugging Face Access Token as a secret:
      ```toml
      HUGGING_FACE_TOKEN = "hf_YourHuggingFaceTokenHere"
      ```
    - Click **"Save"**. Streamlit will reboot the app with the secret, and it will become operational.

## ✍️ Author

This project was created by **Noman**.
