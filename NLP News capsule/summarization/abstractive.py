from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_abstractive(text, max_length=100, lang="en"):
    print(">>> Called summarize_abstractive with text:", text)
    if lang != "en":
        return "Abstractive summarization for this language is not yet supported."
    result = summarizer(text, max_length=max_length, min_length=5, do_sample=False)
    summary = result[0]['summary_text']
    print(">>> Summary returned:", summary)
    return summary
