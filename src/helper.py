from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks

def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

def upload_to_pinecone(chunks, batch_size, embeddings, index):
    try:
        texts = [chunk.page_content for chunk in chunks]
        metadata = [{"source": chunk.metadata.get("source", ""),
                    "page": chunk.metadata.get("page", 0)} for chunk in chunks]
        
        embeddings = embeddings.embed_documents(texts)
        
        # Prepare vectors with metadata
        vectors = [
            (str(i), emb, meta) 
            for i, (emb, meta) in enumerate(zip(embeddings, metadata))
        ]
        
        # Upload in batches
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i + batch_size]
            index.upsert(vectors=[(id_, vec, meta) for id_, vec, meta in batch])
            print(f"Uploaded batch {i//batch_size + 1} of {len(vectors)//batch_size + 1}")
            
    except Exception as e:
        print(f"Error uploading to Pinecone: {str(e)}")
        raise

def query_documents(docsearch, query: str, k: int = 3):
        try:
            results = docsearch.similarity_search_with_score(query,k=k)
            return results
        except Exception as e:
            print(f"Error querying documents: {str(e)}")


