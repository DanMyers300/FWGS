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

loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()


def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text


text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
len(docs)
docs[0]


embeddings = HuggingFaceEmbeddings()

db = FAISS.from_documents(docs, embeddings)

llm = HuggingFaceHub(repo_id="google/flan-t5-xl",
                     model_kwargs={"temperature": 0, "max_length": 512})
# chain = load_qa_chain(llm, chain_type="stuff")

query = "List every time the president mentioned capitalism"
docs = db.similarity_search(query)
# chain.run(input_documents=docs, question=query)


print(wrap_text_preserve_newlines(str(docs[0].page_content)))
