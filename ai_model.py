from transformers import pipeline

qa_model = pipeline("question-answering")

def get_answer(question):
    context = "Artificial Intelligence helps students learn, improves accessibility, and automates tasks."

    result = qa_model(question=question, context=context)
    return result['answer']