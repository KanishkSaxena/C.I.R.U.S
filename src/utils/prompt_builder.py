def make_prompt(context, question_text):
    return (f"{context}\n\nPlease answer a question using this "
          + f"text. "
          + f"Give descriptive answers. If the question is unanswerable, say \"I apologise but this is not in my knowledge store. I will learn more and soon will be able to tell you about it."
          + f"Question: {question_text}")
