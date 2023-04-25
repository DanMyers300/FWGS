import torch
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig, pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

tokenizer = LlamaTokenizer.from_pretrained("chavinlo/alpaca-native")

base_model = LlamaForCausalLM.from_pretrained(
    "chavinlo/alpaca-native",
    load_in_8bit=True,
    device_map='auto',
    quantization_config=BitsAndBytesConfig(
        llm_int8_enable_fp32_cpu_offload=True),
    offload_folder= r'c:\Users\danie\.code',
)

pipe = pipeline(
    "text-generation",
    model=base_model,
    tokenizer=tokenizer,
    max_length=256,
    temperature=0.6,
    top_p=0.95,
    repetition_penalty=1.2
)

local_llm = HuggingFacePipeline(pipeline=pipe)


template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction: 
{instruction}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["instruction"])

llm_chain = LLMChain(prompt=prompt, llm=local_llm)

question = "What is the capital of England?"

print(llm_chain.run(question))
