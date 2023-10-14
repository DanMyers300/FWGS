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


<!-- ABOUT THE PROJECT -->
## About The Project

A python app to intelligently extract items from documents and allow the user to perform queries on the docuemnts using a large language model.

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

#### To-Do
1. Purchase Orders
2. Msc NNS Docs\POs from Exostar
3. Msc NNS Docs\RFQs from Exostar
4. Msc NNS Docs\NNS Quality\VIR
5. Gov Specs & STDs

## UI
- Establish functionality for upload button
- Give UI a facelift so it looks better

## AI
- Set up langchain with llama 2 for Q and A on extracted documents
---
<!-- CONTACT -->
## Contact

Dan Myers - contact@danmyers.net

<p align="right">(<a href="#readme-top">back to top</a>)</p>
