# Text-Summarizer

This project is a text summarizer that shortens long text by picking the most important sentences. It helps you quickly read the main points without going through the whole text.

Link- https://text-summarizer-mayank.streamlit.app/

I have made and test this on jupyter notebook and then used the code to make streamlit app.
I have also uploaded the jupyter notebook file on which I have made this project and test on dummy data. Please check that also, file name- jupyter_text_summarizer

## Step-1: Used Spacy library to tokenize the text, removing stopwords and punctuations. And converted into lower case.
## Step-2: And I also used POS tagging to filter tokens.
## Step-3: Extracted the words from each sentences and find the frequency.USed a dictionary to store the scores and normalize the scores.
## Step-4: Sentence is scored based on the word frequencies
## Step-5: Join all the summarized text.
