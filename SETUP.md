# Setup for GCP ML

<img src="https://github.com/lynnlangit/gcp-ml/blob/master/images/notebook-instances.png" width=800>


## 1. Client Environment

You have several options for setting up a client development environment for GCP Machine Learning.  These environments match different use cases, summarized below as follows.  If you need to setup a new GCP account for learning, see the section at the bottom of this page for quick steps to do this.  

- **1. Google Colabs** - this is a zero-setup, browser-based Jupyter notebook environment which runs on GCP.  
    - Although you can save your work (`.ipynb` and data files), this is an emphemeral comupute environment. 
    - There is a free tier, with CPU/RAM service limits (but you can add TPU capacity) and also a higher resourced tier which has service costs.
    - Save your files (notebooks and input data) in Google Drive, GitHub or locally.
- **2. GCP AI Platform Notebooks** - this is a partially-managed (PaaS) customizable VM solution, running on GCE.  
    - You can select from a number of common pre-confirgured instance types (R, Python, TensorFlow, etc...). 
    - The instances have a charge per minute of use.  Instances can be stopped and re-started when not in use to reduce service costs.  
    - This is the preferred method for this course - screenshot shown above.
- **3. raw GCE VM** - not recommended for study - you would have to install all lanaguages and libraries
- **4. local dev env** - it is possible to install Jupyter locally, either directly on your laptop or via a Docker container.

## 2. Code & Code Editor

You can use the editor and language of your choice.  I am using VSCode and Python on a MacOS.
- Verify Python - NOTE: I wrote this course using Python 2.7, I haven't tested everything with Python 3.x yet
- Install VSCode - do not need to install Git
    - install these extentions for VSCode: 
        - TensorFlowSnippets
        - BigQuery highlight syntax
        - material theme icons
        - Python
        - VS Code Jupyter Notebook viewer

## GCP SDK 
 
 You can use the included console in GCP to run GCP SDK (gcloud) commands or you can download and install the GCP SDK locally

 - Download,unzip, install and authenticate to GCP SDK
 - Verify with `gcloud auth list` or `gcloud config list`

 ## Enable APIs

 You will be using a number of GCP services.  Some services are enabled by default, however, for other services you will need explicitly enable API or service.  

TIP: Verify that you using the intended GCP Project before you enable a service:

GCP Services enabled by default:
 - GCS, GCE, BigQuery, Kubernetes  

 Must be explicitly enabled:
 - Vision API, Video API, Natural Language API, Speech API, Translation API, Dialogflow
 - Cloud Machine Learning Engine
 - Cloud TPU
 - MLKit (for Firebase - TensorFlow Lite on mobile device)
 - Cloud Repositories (if using some of GCP-supplied code samples)
 
 ## GCP AI Hub
  - AI Hub - https://aihub.cloud.google.com/u/0/ (see screen shot below)
  - Resources in the AI Hub include the following:
    - sample training data
    - trained ML models & technical guides
    - compute templates - kubeflow pipelines, ML continers, Jupyter notebooks, ML services, TF models and VM images
    
![AI Hub](https://github.com/lynnlangit/gcp-ml/blob/master/images/ai-hub-main.png)

---

## 0. General GCP Account Setup

The following are general setup steps:
- **1. CREATE** a new gmail account for testing
    - **SIGN IN** to Chrome with this account  
- **2. CREATE** a new GCP account using a gmail address
    - **LOGIN** to the GCP console with your gmail address
    - **CREATE** a billing account (required credit card)
    - **USE** 'new account' $ 300 credit
- **3. CREATE** a new GCP Project
    - **ASSOCIATE** a billing account with this GCP project
    - **SETUP** a billing alert for that project with a notification via pub/sub
    - (Optional) **CREATE** a non-owner IAM admin user to reduce the attack surface
    
---
