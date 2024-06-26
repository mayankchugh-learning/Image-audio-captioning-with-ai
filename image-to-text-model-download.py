# Use a pipeline as a high-level helper
import torch
from transformers import pipeline

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Load the pretrained weights
caption_image = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large", device=device)