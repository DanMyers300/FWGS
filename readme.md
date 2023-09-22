<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">FWGS Entity Extraction</h3>

  <p align="center">
    Named Entity Extraction for Forth-Worth Gasket and Supply
    <br />
    <a href="https://github.com/DanMyers300/FWGS/issues">Report Bug</a>
    ·
    <a href="https://github.com/DanMyers300/FWGS/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#files">File Contents</li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

PDF extraction using NLP library [Spacy](https://spacy.io/api)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---
<!-- USAGE EXAMPLES -->
## Usage

- Currently only usable via command line
	1) Create python VENV
	2) Run `pip install -r requirements.txt`
	3) Run `python src/runNER.py`

Reference [[#Road map]] for UI information
<p align="right">(<a href="#readme-top">back to top</a>)</p>


---
<!-- ROAD MAP -->
## Road map

## Extraction:
#### Working
1. Emails
2. URLS
3. Dates
4. Addresses
5. RFQ
6. CODED NOTES

#### Not working
1. Version Number
2. Distribution Method
3. NNS End Use
4. Purchaser Group
5. Buyer Title
6. DPAS Rating section
7. Summary of hardware section
8. APPENDICES TO HARDWARE

### UI
#### Form
- Give the front page a face lift, change themes and establish the "look and feel".
#### Function
- Connect chat api LLM for queries on database.

### Language Models
- Create custom models from FWGS data to extract all items.
#### LLM
- Set up language model on extracted items to query on inputted pdf file.
- *Long term:* Set up language model on entire database.
---
<!-- Files -->
## Files

### `/data`
- `/base_files`
	- Original files given for training.
- `/models`
	- Trained SpaCy models.
- `/outputs`
	- Extracted items are dumped here.
- `/training_data`
	- Formatted training data to train the spacy models.
- `corpus.txt`
	- The raw text that is dumped from pdf_processor.py.
### `/src`
- `/spacy`
- `pdf_processor.py`
	- Dumps text from one or more pdf files into `/data/corpus.txt`.
- `runNER.py`
	- The main python file that executes all the extraction modules.
### `/ui`
- `/static`
	- Contains files for website UI.
- `__init__.py`
	- Runs the flask app and handles the api.

---
<!-- CONTACT -->
## Contact

Dan Myers - contact@danmyers.net

<p align="right">(<a href="#readme-top">back to top</a>)</p>