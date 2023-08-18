import cv2
from PIL import Image
import torch
import imageio
from transformers import ViTFeatureExtractor, ViTForImageClassification
import requests

# Load the pre-trained model and feature extractor
model_path = '/home/Akhil/Documents/kk/Crime-Detection-using-Machine-Learning/'
model = ViTForImageClassification.from_pretrained(model_path)
feature_extractor = ViTFeatureExtractor.from_pretrained(model_path)

# Load the label mappings from the custom config file
import json
with open("config.json") as f:
    label_mappings = json.load(f)["id2label"]

# Set the device to use
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Load the video
vid = imageio.get_reader('video4.mp4',  'ffmpeg')
cap = cv2.VideoCapture('video4.mp4')

# Get video fps
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Set frame count and total frames
count = 0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    # Process every 5th frame
    if count % (fps * 2) == 0:
        # Check if frame is empty
        if frame is None:
            break

        # Convert to RGB and resize
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (256, 256))

        # Convert to PIL image and preprocess
        image = Image.fromarray(frame)
        inputs = feature_extractor(images=image, return_tensors='pt').to(device)

        # Make predictions
        outputs = model(**inputs)
        predicted_probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        topk_probs, topk_indices = torch.topk(predicted_probs, k=4)

        # Print the top 4 predicted classes along with their probabilities
        print(f"Frame: {count} / {total_frames}")
        for i in range(4):
            predicted_label = label_mappings[str(topk_indices[0][i].item())]
            predicted_prob = topk_probs[0][i].item()
            print(f"{predicted_label}: {predicted_prob:.2f}")
            if predicted_label != "NormalVideos" and predicted_prob > 0.3:
                # Save the frame with predicted label as filename
                filename = f"{predicted_label}(frame{count}).jpg"
                cv2.imwrite(filename, frame)
                print(f"Saved {filename}")
                # Make API request to save the image and predicted label
                url = 'http://127.0.0.1:8000/api/images/'
                files = {'image': open(filename, 'rb')}
                data = {'text': filename, 'image': image}
                response = requests.post(url, files=files, data=data)
                break

cap.release()
cv2.destroyAllWindows()
