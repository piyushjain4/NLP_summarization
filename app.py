import streamlit as st
from transformers import pipeline

st.set_page_config(layout="wide")
st.title("Deep Learning in action!!")
@st.cache_resource
def text_summary(text,model, maxlength=None):
    summary = text
    if model=="Gpt2" :
      gpt2_id = '/content/drive/MyDrive/summarizer/gpt2Output/gpt2-medium-finetuned-bbc-lemmatized/checkpoint-11500'
      gpt2_summary = pipeline("text-generation", model=gpt2_id)
      # print(len(text))
      # st.write(len(text))
      summary = gpt2_summary(text+"TL;DR:",max_length =len(text.split())+200)[0]["generated_text"]
      summary = summary.replace(text+"TL;DR:", ' ')
    elif model=="Bart":
      bart_id ='/content/drive/MyDrive/summarizer/bart/bart-large-cnn-finetuned-bbc-lemmatized/checkpoint-1500'
      bart_summary = pipeline("summarization", model=bart_id)
      summary = bart_summary("summarize:"+text,max_length = 300)[0]["summary_text"]
    return summary

choice = st.sidebar.selectbox("What do you want us to do?", ["Summarize Text"])
model = st.sidebar.selectbox("Select Your Model",["Gpt2","Bart"])

if choice == "Summarize Text":
    st.subheader(f"Summarize Text using {model} ")
    input_text = st.text_area("Enter your text here")
    if input_text is not None:
        if st.button("Summarize Text"):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("**Your Input Text**")
                st.info(input_text)
            with col2:
                st.markdown("**Summary Result**")
                result = text_summary(input_text,model)
                st.success(result)
    
  
                