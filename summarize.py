from transformers import pipeline

def get_summary(text):
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )
    
    result = summarizer(text, max_length=50, min_length=20, do_sample=False)
    return result[0]['summary_text']