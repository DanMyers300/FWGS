import gradio as gr
import logging
from llama_index import Document
from llama_index import SimpleDirectoryReader, LangchainEmbedding, GPTListIndex, GPTSimpleVectorIndex, PromptHelper
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LLMPredictor, ServiceContext
import torch
from langchain.llms.base import LLM
from transformers import pipeline


class customLLM(LLM):
    model_name = "chavinlo/alpaca-native"
    pipeline = pipeline("text2text-generation", model=model_name,
                        device=0, model_kwargs={"torch_dtype": torch.bfloat16})

    def _call(self, prompt, stop=None):
        return self.pipeline(prompt, max_length=9999)[0]["generated_text"]

    def _identifying_params(self):
        return {"name_of_model": self.model_name}

    def _llm_type(self):
        return "custom"


llm_predictor = LLMPredictor(llm=customLLM())


hfemb = HuggingFaceEmbeddings()
embed_model = LangchainEmbedding(hfemb)

text1 = r'./test.txt'


text_list = [text1]

documents = [Document(t) for t in text_list]


# # set number of output tokens
# num_output = 500
# # set maximum input size
# max_input_size = 512
# # set maximum chunk overlap
# max_chunk_overlap = 15


# prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)


# index = GPTSimpleVectorIndex(documents, embed_model=embed_model, llm_predictor=llm_predictor)

# index = GPTListIndex(documents, embed_model=embed_model, llm_predictor=llm_predictor)

# index.save_to_disk('index.json')

service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor, embed_model=embed_model)
index = GPTSimpleVectorIndex.from_documents(
    documents, service_context=service_context)


logging.getLogger().setLevel(logging.CRITICAL)

response = index.query("Who is the supplier")
response.response

index = None


def build_the_bot(input_text):
    text_list = [input_text]
    documents = [Document(t) for t in text_list]
    global index
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, embed_model=embed_model)
    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=service_context)
    return ('Index saved successfull!!!')


def chat(chat_history, user_input):

    bot_response = index.query(user_input)
    # print(bot_response)
    response = ""
    # [bot_response[i:i+1] for i in range(0, len(bot_response), 1)]:
    for letter in ''.join(bot_response.response):
        response += letter + ""
        yield chat_history + [(user_input, response)]


with gr.Blocks() as demo:
    gr.Markdown('# Q&A Bot with Hugging Face Models')
    with gr.Tab("Input Text Document"):
        text_input = gr.Textbox()
        text_output = gr.Textbox()
        text_button = gr.Button("Build the Bot!!!")
        text_button.click(build_the_bot, text_input, text_output)
    with gr.Tab("Knowledge Bot"):
        #          inputbox = gr.Textbox("Input your text to build a Q&A Bot here.....")
        chatbot = gr.Chatbot()
        message = gr.Textbox("What is this document about?")
        message.submit(chat, [chatbot, message], chatbot)

demo.queue().launch(debug=True)
