
# PromptAI Master — Prompt Engineering Comparison Lab

## Overview

**PromptAI Master** is an interactive Prompt Engineering Lab developed using Python and Streamlit. It helps users explore, test, and compare different prompting techniques using a Large Language Model (LLM).

The application allows users to submit a task, select multiple prompting techniques, generate responses, and evaluate the outputs based on clarity, relevance, and formatting.

The AI assistant in this project is named **TOM**.

## Objectives

- Understand the fundamentals of prompt engineering.
- Implement and compare different prompting techniques.
- Analyze how prompt structure influences AI-generated responses.
- Evaluate response quality using a simple scoring system.
- Provide an interactive interface for prompt experimentation.

## Features

- **Zero-shot Prompting:** Generates a response without providing examples.
- **One-shot Prompting:** Uses one example to guide the expected response.
- **Few-shot Prompting:** Uses multiple examples to guide the model.
- **Chain-of-Thought (CoT):** Encourages structured problem-solving and concise explanations.
- **Manual CoT:** Uses an explicit sequence of task-solving instructions.
- **Tree of Thoughts (ToT):** Encourages comparison of multiple candidate approaches.
- **Response Comparison:** Displays outputs from selected techniques.
- **Evaluation System:** Scores responses based on clarity, relevance, and format.
- **Adjustable Parameters:** Allows users to configure temperature and maximum output tokens.
- **Interactive Interface:** Built with Streamlit for easy experimentation.

## Technology Stack

- **Programming Language:** Python
- **Frontend and UI:** Streamlit
- **LLM Integration:** Hugging Face Inference Providers
- **API Client:** Hugging Face Hub
- **Environment Configuration:** python-dotenv
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## Project Workflow

1. User enters a task.
2. User selects one or more prompting techniques.
3. The application builds the corresponding prompts.
4. Prompts are sent to the configured language model.
5. TOM generates responses.
6. The application displays the responses for comparison.
7. Users evaluate each response.
8. The results help identify a suitable prompting technique for the task.

## Project Structure

```
PromptAI_Master/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── screenshots/
```

Note: If `build_prompt()` is defined directly inside `app.py`, the separate `prompt_templates.py` file is optional.

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- Visual Studio Code
- Git
- A Hugging Face account
- An access token with the required Inference Providers permission

### Step 1: Clone the Repository

```
git clone https://github.com/YOUR-USERNAME/PromptAI_Master.git
cd PromptAI_Master
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Create a Virtual Environment

```
python -m venv .venv
```

Activate it on Windows PowerShell:

```
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

### Step 4: Configure the API Token

Create a `.env` file in the project root directory:

```
HF_TOKEN=your_hugging_face_token
```

Replace the placeholder with your own token.

**Security:** Never upload your `.env` file or expose your API token in a public repository.

### Step 5: Run the Application

```
streamlit run app.py
```

Open the local URL displayed in your terminal to use PromptAI Master.

## Evaluation Method

Each generated response is evaluated using three criteria:

| Criterion | Purpose                                                        |
| --------- | -------------------------------------------------------------- |
| Clarity   | Measures how clearly the response communicates the answer.     |
| Relevance | Measures how closely the response addresses the task.          |
| Format    | Measures how well the response follows the expected structure. |

Each criterion is rated on a scale of 1 to 5.

**Average Score = (Clarity + Relevance + Format) / 3**

The scores help users compare the selected prompting techniques. Results may vary depending on the task, prompt design, model, and generation settings.

## Applications

- Prompt engineering education
- AI response quality analysis
- Structured problem-solving experiments
- Text classification and summarization
- SQL query generation experiments
- Basic mathematical problem-solving
- Information extraction tasks

## Future Enhancements

- Automatic evaluation of generated responses
- Export comparison results to CSV or PDF
- Response history and experiment tracking
- Side-by-side comparison charts
- Support for additional language models
- Improved error handling and API status indicators
- Downloadable experiment reports

## Conclusion

PromptAI Master provides a practical environment for learning and experimenting with prompt engineering. By comparing different prompting techniques through a single interactive application, users can better understand how prompt design affects AI-generated outputs.

## Author

**Project:** PromptAI Master\
**Category:** Artificial Intelligence | Prompt Engineering | Python\
**Interface:** Streamlit\
**AI Assistant:** TOM

## License

This project is intended for educational and learning purposes. Add an appropriate open-source license, such as the MIT License, if you wish to permit others to reuse and modify the code.

