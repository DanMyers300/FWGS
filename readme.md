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

- `Sudo apt-get install docker`
- `Sudo docker pull danmyers300/fwgs:latest`
- `Sudo docker run --rm -v /mnt/{EXTERNAL FILES}:/usr/app/data/external danmyers300/fwgs:latest`

Reference [Docker Hub](https://hub.docker.com/repository/docker/danmyers300/fwgs/general)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


---
<!-- ROAD MAP -->
## Road map

- Rewrite PDF processor
- Train extraction models on data provided by FWGS
- Set up a LLM on documents upload
- Set up a LLM on entire database
- Connect extraction functionality with UI

## Extraction
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
9. mount/Purchase Orders
10. mount/Msc NNS Docs\POs from Exostar
11. mount/Msc NNS Docs\RFQs from Exostar
12. mount/Msc NNS Docs\NNS Quality\VIR
13. mount/Gov Specs & STDs

## UI
- Connect LLM and chatbot UI
- Establish functionality for upload button
- Give UI a facelift so it looks better
---
<!-- CONTACT -->
## Contact

Dan Myers - contact@danmyers.net

<p align="right">(<a href="#readme-top">back to top</a>)</p>
