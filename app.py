from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings, load_pdf, text_split
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


# embeddings = download_hugging_face_embeddings()

# #Initializing the Pinecone
# index_name = "medical-chatbot2"
# pc=Pinecone(api_key=PINECONE_API_KEY)
# index = pc.Index(index_name)
# pc.list_indexes()

# extracted_data = load_pdf("data/")
# text_chunks = text_split(extracted_data)
# texts = [chunk.page_content for chunk in text_chunks]
# metadatas = [chunk.metadata for chunk in text_chunks]

# from langchain.vectorstores import Pinecone as LangChainPinecone
# docsearch = LangChainPinecone.from_texts(
#     texts=texts,
#     embedding=embeddings,
#     metadatas=metadatas,
#     index_name=index_name
# )
# PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# chain_type_kwargs={"prompt": PROMPT}

# llm= CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_1.bin",
#                    model_type="llama",
#                    config={'max_new_tokens': 512,
#                             'temperature': 0.8})


# qa=RetrievalQA.from_chain_type(
#     llm=llm, 
#     chain_type="stuff", 
#     retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
#     return_source_documents=True, 
#     chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     print(input)
#     result=qa({"query": input})
#     print("Response : ", result["result"])
#     return str(result["result"])





@app.route("/get01", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    # result=qa({"query": input})
    result="1. It's important to recognize that negative expectations of the future can be a cognitive distortion, which can lead to feelings of hopelessness and depression. 2. Cognitive therapy is a type of psychotherapy that focuses on identifying and challenging these distorted thinking patterns, in order to improve one's mental health and well-being."
    print("Response : ", )
    return str(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)