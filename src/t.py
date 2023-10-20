import subprocess
import sys
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 

model_name = "llama2"
question = "Who was the first person on the moon? ..."

if __name__ == "__main__":
    subprocess.run(f"ollama pull {model_name}", shell=True, check=True, stdout=subprocess.PIPE)
    llm = Ollama(model=model_name, callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
    llm(question)
