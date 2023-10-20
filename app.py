import streamlit as st
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space

# Sidebar contents
with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [openAi](https://platform.openai.com/docs/models) LLM model
                
    ''')
    add_vertical_space(5)
    st.write('Made by [Prompt Engineer](https://youtube.com/@engineerprompt)')

def main():
    st.header("Chat with your PDF ")

    # Upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    st.write(pdf)

    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

            st.write(text)

if __name__ == '__main__':
    main()