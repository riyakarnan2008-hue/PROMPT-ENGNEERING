
"""Prompting techniques: Zero-shot, One-shot, Few-shot, CoT, ToT."""

TECHNIQUES = {
    "Zero-Shot": {
        "icon": "🎯",
        "desc": "No examples. Direct question only.",
    },
    "One-Shot": {
        "icon": "1️⃣",
        "desc": "One example is given before the task.",
    },
    "Few-Shot": {
        "icon": "📚",
        "desc": "Multiple examples guide the model.",
    },
    "Chain-of-Thought": {
        "icon": "🧠",
        "desc": "Breaks a problem into logical steps.",
    },
    "Tree-of-Thought": {
        "icon": "🌳",
        "desc": "Explores multiple possible approaches.",
    },
}


def build_prompt(technique, task, examples=None):
    """Build a prompt based on the selected prompting technique."""

    examples = examples or []

    if technique == "Zero-Shot":
        return f"""
Answer the following task clearly and accurately.

Task:
{task}
"""

    elif technique == "One-Shot":
        example = examples[0] if examples else {
            "input": "What is AI?",
            "output": "AI is the simulation of human intelligence by machines."
        }

        return f"""
Learn from this example.

Example:
Input: {example.get('input', '')}
Output: {example.get('output', '')}

Now complete the following task.

Task:
{task}
"""

    elif technique == "Few-Shot":
        if not examples:
            examples = [
                {
                    "input": "2 + 2",
                    "output": "4"
                },
                {
                    "input": "3 + 5",
                    "output": "8"
                }
            ]

        examples_text = "\n".join(
            f"Input: {ex.get('input', '')}\n"
            f"Output: {ex.get('output', '')}"
            for ex in examples
        )

        return f"""
Follow the patterns shown in these examples.

{examples_text}

Now complete this task:
{task}
"""

    elif technique == "Chain-of-Thought":
        return f"""
Analyze the task carefully.
Work through the important logical steps internally,
verify your conclusion, and provide a clear explanation
with the final answer.

Task:
{task}
"""

    elif technique == "Tree-of-Thought":
        return f"""
Explore multiple possible approaches to solve the task.
Compare their advantages and disadvantages.
Choose the most suitable approach and provide the final answer
with a concise explanation.

Task:
{task}
"""

    else:
        raise ValueError(
            f"Unknown prompting technique: {technique}"
        )
