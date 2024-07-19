import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
from PyPDF2 import PdfReader
import docx
import io
import chardet

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def read_text_file(file):
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']
    return raw_data.decode(encoding)

def preprocess_text(text):
    #remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # convert to lowercase
    text = text.lower()
    # split into words
    words = text.split()
    # remove short words (less than 3 characters)
    words = [word for word in words if len(word) > 2]
    return words

def generate_wordcloud(words):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
    return wordcloud

def main():
    st.title("Document Word Cloud Generator")
    st.markdown("*Made by Pranav Verma*")

    supported_extensions = [
        "pdf", "docx", "txt", "c", "cpp", "cs", "java", "py", "js", "html", "css", "php", "rb", "pl", "sh", "swift",
        "go", "rs", "lua", "json", "xml", "yaml", "yml", "ini", "conf", "cfg", "env", "md", "rst", "log", "csv",
        "tsv", "sql", "bat", "ps1", "rtf", "tex", "tpl", "xslt", "asciidoc", "vbs"
    ]

    uploaded_file = st.file_uploader("Choose a file", type=supported_extensions)

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        try:
            if file_extension == 'pdf':
                text = read_pdf(uploaded_file)
            elif file_extension == 'docx':
                text = read_docx(uploaded_file)
            else:
                text = read_text_file(uploaded_file)

            words = preprocess_text(text)

            #generate word cloud
            wordcloud = generate_wordcloud(words)

            #display word cloud
            st.subheader("Word Cloud")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)

            #count word frequencies
            word_freq = Counter(words)
            most_common = word_freq.most_common(20)

            #display table of most common words
            st.subheader("Most Common Words")
            st.table({"Word": [word for word, count in most_common],
                      "Count": [count for word, count in most_common]})

        except Exception as e:
            st.error(f"An error occurred while processing the file: {str(e)}")
            st.error("Please ensure the file is not corrupted and try again.")

if __name__ == "__main__":
    main()