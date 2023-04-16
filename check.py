from PIL import Image
import requests
from io import BytesIO
import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification

# Load the pre-trained model and feature extractor
model_path = '/home/akhil/Downloads/hack/'
model = ViTForImageClassification.from_pretrained(model_path)
feature_extractor = ViTFeatureExtractor.from_pretrained(model_path)

# Load the label mappings from the custom config file
import json
with open("config.json") as f:
    label_mappings = json.load(f)["id2label"]

# Set the device to use
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Preprocess the input image
image_path = "images.jpeg"
image = Image.open(image_path)
inputs = feature_extractor(images=image, return_tensors='pt').to(device)

# Make predictions
outputs = model(**inputs)
predicted_probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
topk_probs, topk_indices = torch.topk(predicted_probs, k=4)

# Print the top 4 predicted classes along with their probabilities
print("Top 4 predicted classes:")
for i in range(4):
    predicted_label = label_mappings[str(topk_indices[0][i].item())]
    predicted_prob = topk_probs[0][i].item()
    print(f"{predicted_label}: {predicted_prob:.2f}")
