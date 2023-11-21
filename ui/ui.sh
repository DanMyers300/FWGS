#!/bin/bash

ollama pull llama2
python3 ingest.py
python3 privateGPT.py