import streamlit as st
import spacy
from collections import Counter
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
import pandas as pd
nlp=spacy.load('en_core_web_sm')
def summarize_text(text,num_sentences=3):
    doc=nlp(text)
    tokens=[]
    stopwords=list(STOP_WORDS)
    allowed_pos=['ADJ','PROPN','VERB','NOUN']
    for token in doc:
        if token.text.lower() in stopwords or token.text in punctuation:
            continue
        if token.pos_ in allowed_pos:
            tokens.append(token.text.lower())
    word_freq = Counter(tokens)
    max_freq=max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word]/=max_freq
    sent_tokens=[sent.text for sent in doc.sents]
    sent_score={}
    for sent in sent_tokens:
        for word in sent.split():
            word_lower = word.lower()
            if word_lower in word_freq:
                if sent not in sent_score:
                    sent_score[sent] = word_freq[word_lower]
                else:
                    sent_score[sent] += word_freq[word_lower]
    top_sentences = nlargest(num_sentences, sent_score, key=sent_score.get)
    summary=" ".join(top_sentences)
    return summary
st.title("Text Summarizer")
st.write("Enter text to summarize")
input_text=st.text_area("Enter Text")
if st.button("Summarize"):
    if input_text.strip()!="":
        summary=summarize_text(input_text)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter text")

