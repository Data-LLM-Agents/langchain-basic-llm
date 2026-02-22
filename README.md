# LangChain Basic LLM Tutorial

This repository contains a simple implementation of a LangChain application as part of Lab 4. It demonstrates how to use `ChatOpenAI`, `ChatPromptTemplate`, and LCEL (LangChain Expression Language) to create a basic LLM chain.

## Prerequisites

- Python 3.8+
- OpenAI API Key

## Installation

1.  **Clone the repository** (if not already cloned):
    ```bash
    git clone <repository_url>
    cd langchain-basic-llm
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API Key:
    ```
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

Run the tutorial script:

```bash
python llm_tutorial.py
```

You will be prompted to enter a question. The application will send your question to the LLM and print the response.

### Sample Interaction

```text
Enter your question: What is LangChain?

Response:
LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). It provides tools and abstractions to chain different components together, such as prompts, models, and output parsers.
```

### Interactive Notebook (The "Book")

We have also provided a Jupyter Notebook that explains the steps in detail, like a book. To use it:

1.  Ensure you have `notebook` installed (included in requirements).
2.  Run:
    ```bash
    jupyter notebook tutorial.ipynb
    ```


## Architecture

The application uses a simple LCEL chain:

`PromptTemplate` -> `ChatOpenAI` -> `StrOutputParser`

-   **PromptTemplate**: Formats the user input into a message for the LLM.
-   **ChatOpenAI**: The LLM model (gpt-3.5-turbo).
-   **StrOutputParser**: Parses the output message content into a string.