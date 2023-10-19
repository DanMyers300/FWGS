import subprocess
import sys
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 

model_name = "llama2"
question = "Who was the first person on the moon? ..."

def pull_ollama_model(model_name):
    try:
        command = f"ollama pull {model_name}"
        subprocess.run(command, shell=True, check=True)
        print(f"Sucessfully pulled {model_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"error: {str(e)}")

if __name__ == "__main__":
    pull_ollama_model(model_name)
    llm = Ollama(model=model_name, callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
    llm(question)
