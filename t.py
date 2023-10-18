import subprocess
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler 

try:
    process = subprocess.Popen("ollama pull llama2", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end="")
    print("Return Code:", process.wait())
except subprocess.CalledProcessError as e:
    print("Error:", e)


llm = Ollama(model="llama2", 
                     callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
llm("Who was the first person on the moon? ...")
