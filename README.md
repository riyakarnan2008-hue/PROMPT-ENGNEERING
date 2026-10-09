# Prompt AI Master

## Overview

Prompt AI Master is an AI-powered prompt engineering application built using Python and Streamlit. It helps users create effective prompts, explore different prompting techniques, and compare AI-generated responses through an interactive dashboard.

## Features

- Interactive dashboard with a modern user interface
- Multiple prompt engineering strategies
- Zero-Shot Prompting
- One-Shot Prompting
- Few-Shot Prompting
- Chain of Thought (CoT)
- Tree of Thought (ToT)
- Single Strategy Analysis
- Compare Strategies mode
- Adjustable creativity and response detail
- View generated prompts
- AI-generated responses with execution time
- Groq API integration through a configurable LLM module

## Technologies Used

- Python
- Streamlit
- Groq API
- Python-dotenv

## Project Structure

```text
Prompt-AI-Master/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Prompt-AI-Master
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API Key

Create a `.env` file in the project directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own API key. Never upload your API key to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Usage

1. Enter the task you want the AI to perform.
2. Select Single Strategy or Compare Strategies.
3. Choose one or more prompting techniques.
4. Adjust creativity and response detail in the sidebar.
5. Enable Show Generated Prompt if you want to inspect the prompt.
6. Click Run Prompt Analysis.
7. Review the generated responses.

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to authenticate with Groq |

## Security

- Keep API keys private.
- Store credentials in the `.env` file.
- Add `.env` and `.venv/` to `.gitignore`.
- Do not commit secrets or credentials to version control.

## Future Enhancements

- Prompt history and saved prompts
- Export responses as text or PDF
- Additional AI models
- Prompt quality evaluation
- User-defined prompt templates

## Author

**Riyavalli**

## License

This project is intended for educational and learning purposes. Add an appropriate open-source license if you plan to distribute it publicly.
