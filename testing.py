from langchain import HuggingFaceHub
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import textwrap
from langchain.document_loaders import TextLoader
import requests
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


url = "https://raw.githubusercontent.com/hwchase17/langchain/master/docs/modules/state_of_the_union.txt"
res = requests.get(url)
with open("state_of_the_union.txt", "w") as f:
    f.write(res.text)

# Document Loader
loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()


def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text


# print(wrap_text_preserve_newlines(str(documents[0])))


# Text Splitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

len(docs)

docs[0]

# Embeddings

embeddings = HuggingFaceEmbeddings()

# Vectorstore: https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

db = FAISS.from_documents(docs, embeddings)

query = "What did the president say about the Supreme Court"
docs = db.similarity_search(query)

print(wrap_text_preserve_newlines(str(docs[0].page_content)))


llm = HuggingFaceHub(repo_id="google/flan-t5-xl",
                     model_kwargs={"temperature": 0, "max_length": 512})
chain = load_qa_chain(llm, chain_type="stuff")

query = "What did the president say about the Supreme Court"
docs = db.similarity_search(query)
chain.run(input_documents=docs, question=query)


query = "What did the president say about economy?"
docs = db.similarity_search(query)
chain.run(input_documents=docs, question=query)
