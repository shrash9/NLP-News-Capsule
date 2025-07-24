from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_abstractive(text, max_length=100, lang="en"):
    if lang != "en":
        return "Abstractive summarization for this language is not yet supported."
    summary = summarizer(text, max_length=max_length, min_length=25, do_sample=False)
    return summary[0]['summary_text']