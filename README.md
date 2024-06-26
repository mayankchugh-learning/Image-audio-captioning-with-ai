# Image-audio-captioning-with-ai

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p imageaudiocaptionvenv python -y
```

```bash
source activate ./imageaudiocaptionvenv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run application
```bash
Python app.py
```

[Models -> Task -> Image-to-text -> Salesforce/blip-image-captioning-large ](https://huggingface.co/Salesforce/blip-image-captioning-large)

##### after download move the model to code folder
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--kakao-enterprise--vits-ljs/ /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/Models/models--kakao-enterprise--vits-ljs
```
```bash
../Models/models--kakao-enterprise--vits-ljs/snapshots/3bcb8321394f671bd948ebf0d086d694dda95464
```

##### after download move the model to code folder
```
cd /Users/mayankchugh/.cache/huggingface/hub/
```
###### copy your downloaded model name and path and paste it below (it already pasted for my workspace)
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english
```


(To fix espeak issue on windows machine) - https://github.com/bootphon/phonemizer/issues/44


[Gradio documentation link](https://www.gradio.app/docs/gradio/file)