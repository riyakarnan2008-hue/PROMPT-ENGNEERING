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
