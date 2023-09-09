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

1. Place .pdf files to extract in data folder
2. Run
   ```sh
   python main.py
   ```
3. If you've never ran the program before then press "y" when it prompts you.
4. Extracted items with be placed in data/outputs

<p align="right">(<a href="#readme-top">back to top</a>)</p>


---
<!-- ROADMAP -->
## Roadmap
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

---
<!-- Files -->
## Files

### main.py

- Runs the rest of the files neccessary to complete a full ner from a pdf.

### src/pdf_processor.py

- A simple script that extracts information from a pdf file into a txt file.

### src/create_spacy_file.py

- Converts a .json file containing training information into a binary format called .spacy

### Spacy Files

- config.cfg
    - A configuration file to train a custom spacy model
- train.spacy
    - Converted training data .json to a binary format that spacy can understand

### src/run_ner.py
- This is the main script. This contains objects for each of the items to extract.

---
<!-- CONTACT -->
## Contact

Daniel Myers - contact@danmyers.net

<p align="right">(<a href="#readme-top">back to top</a>)</p>