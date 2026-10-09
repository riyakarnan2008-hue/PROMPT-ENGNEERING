import streamlit as st
from llm import generate_response

st.set_page_config(
    page_title="PromptAI Master",
    page_icon="🤖",
    layout="wide"
)


def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer the following task directly and accurately.

Task:
{task}
""".strip()

    elif technique == "One-shot":
        return f"""
Use the example below to understand the expected answer style.

Example:
Task: Explain Python.
Answer: Python is a high-level programming language used to
build applications, automate tasks, and analyze data.

Now answer this task:
{task}
""".strip()

    elif technique == "Few-shot":
        return f"""
Study the examples and follow their answer pattern.

Example 1:
Task: What is AI?
Answer: AI is technology that enables computers to perform
tasks that normally require human intelligence.

Example 2:
Task: What is ML?
Answer: Machine learning is a part of AI where systems learn
patterns from data to make predictions or decisions.

Example 3:
Task: What is NLP?
Answer: NLP enables computers to process and understand
human language.

Now answer this task:
{task}
""".strip()

    elif technique == "CoT":
        return f"""
Solve the following task carefully.

1. Understand the task.
2. Identify the important information.
3. Apply the appropriate method.
4. Verify the result.
5. Give a concise final answer.

Provide only a short explanation of the key steps.
Do not reveal private or hidden chain-of-thought.

Task:
{task}
""".strip()

    elif technique == "Manual CoT":
        return f"""
Use the following explicit reasoning structure.

Step 1 - Understand the task:
Identify what is being asked.

Step 2 - Identify information:
List the important facts, inputs, or constraints.

Step 3 - Apply the method:
Describe the main rule, calculation, or approach.

Step 4 - Verify:
Check whether the result is reasonable.

Step 5 - Final answer:
Give the final answer clearly.

Task:
{task}
""".strip()

    elif technique == "ToT":
        return f"""
Solve the task by considering multiple possible approaches.

Approach A:
Suggest one possible solution and briefly evaluate it.

Approach B:
Suggest a second possible solution and briefly evaluate it.

Approach C:
Suggest a third possible solution when useful.

Selection:
Compare the approaches and select the most suitable one.

Final answer:
Provide the selected answer with a concise explanation.

Do not reveal private or hidden chain-of-thought.

Task:
{task}
""".strip()

    else:
        raise ValueError("Unknown prompting technique")


st.title("🤖 PromptAI Master")

st.write(
    "An interactive Prompt Engineering Lab to compare "
    "different prompting techniques using TOM."
)

st.divider()

task = st.text_area(
    "Enter your task",
    placeholder=(
        "Example: Explain Artificial Intelligence "
        "to a first-year student."
    ),
    height=120
)

techniques = st.multiselect(
    "Select Prompting Techniques",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ],
    default=[
        "Zero-shot",
        "Few-shot"
    ]
)

col1, col2 = st.columns(2)

with col1:
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.1
    )

with col2:
    max_tokens = st.slider(
        "Maximum Tokens",
        min_value=100,
        max_value=1000,
        value=500,
        step=100
    )

st.divider()

if st.button("Generate Comparison", type="primary"):

    if task.strip() == "":
        st.warning("Please enter a task.")

    elif not techniques:
        st.warning("Please select at least one prompting technique.")

    else:

        responses = {}

        progress = st.progress(0)

        for index, technique in enumerate(techniques):

            try:
                final_prompt = build_prompt(
                    technique,
                    task
                )

                answer = generate_response(
                    final_prompt,
                    temperature,
                    max_tokens
                )

                responses[technique] = answer

            except Exception as e:
                responses[technique] = f"Error: {e}"

            progress.progress(
                (index + 1) / len(techniques)
            )

        st.success("TOM generated all selected responses.")

        st.subheader("Prompt Comparison")

        columns = st.columns(len(techniques))

        for index, technique in enumerate(techniques):

            with columns[index]:

                st.markdown(
                    f"### {technique}"
                )

                st.write(
                    responses[technique]
                )

                st.markdown("**Evaluation**")

                clarity = st.slider(
                    "Clarity",
                    1,
                    5,
                    3,
                    key=f"clarity_{technique}"
                )

                relevance = st.slider(
                    "Relevance",
                    1,
                    5,
                    3,
                    key=f"relevance_{technique}"
                )

                format_score = st.slider(
                    "Format",
                    1,
                    5,
                    3,
                    key=f"format_{technique}"
                )

                average = (
                    clarity +
                    relevance +
                    format_score
                ) / 3

                st.metric(
                    "Average Score",
                    f"{average:.1f}/5"
                )

        st.divider()

        st.subheader("Conclusion")

        st.write(
            "Compare the generated responses based on clarity, "
            "relevance, structure, and usefulness. The technique "
            "with the highest evaluation score can be considered "
            "the most suitable technique for the selected task."
        )