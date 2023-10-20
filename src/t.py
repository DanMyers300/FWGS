import subprocess
import sys
from langchain.llms import Ollama
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain import hub
from langchain.embeddings import GPT4AllEmbeddings
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 
from langchain.chains import RetrievalQA

model_name = "llama2"
question = "What's the RFQ number from the corpus document? ..."

# Load documents
loader = TextLoader("./corpus.txt")
data = loader.load()

# Split into chuncks 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
all_splits = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

# RAG prompt
QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")

llm = Ollama(model=model_name, callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

# QA chain
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever(), chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})


if __name__ == "__main__":
    subprocess.run(f"ollama pull {model_name}", shell=True, check=True, stdout=subprocess.PIPE)
    result = qa_chain({"query": question})
