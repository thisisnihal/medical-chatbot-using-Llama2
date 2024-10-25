from src.helper import load_pdf, text_split, download_hugging_face_embeddings, upload_to_pinecone
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
import os


load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_API_ENV = os.getenv('PINECONE_API_ENV')

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
index_name = "medical-chatbot2"

pc=Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(index_name)

pc.list_indexes()

upload_to_pinecone(text_chunks, 1000, embeddings, index)


# texts = [chunk.page_content for chunk in text_chunks]
# metadatas = [chunk.metadata for chunk in text_chunks]


# from langchain.vectorstores import Pinecone as LangChainPinecone
# docsearch = LangChainPinecone.from_texts(
#     texts=texts,
#     embedding=embeddings,
#     metadatas=metadatas,
#     index_name=index_name
# )


