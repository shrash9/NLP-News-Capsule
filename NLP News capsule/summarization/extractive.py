import spacy
import heapq

nlp = spacy.blank("en")
nlp.add_pipe('sentencizer')


def summarize_extractive(text, num_sentences=3, lang="en"):
   
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    if not sentences:
        return ""
    if len(sentences) <= num_sentences:
        return text
    ranked = heapq.nlargest(num_sentences, sentences, key=len)
    return " ".join(ranked)
