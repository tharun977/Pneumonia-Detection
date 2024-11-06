# Pneumonia Detection API

This project provides a REST API for predicting pneumonia in chest X-ray images using a pre-trained model built with FastAI.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Dependencies](#dependencies)
- [License](#license)

## Project Overview

This project uses FastAI and Django to create an API that accepts chest X-ray images and returns a prediction of whether the image indicates pneumonia. The model is exported from FastAI and loaded into a Django REST Framework backend to serve predictions.

## Setup and Installation

Follow these steps to set up the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/pneumonia-detection-api.git
cd pneumonia-detection-api
2. Set up a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Add your pre-trained model
Place your exported FastAI model (e.g., exported_model.pkl) in the models/ directory.

5. Run migrations
bash
Copy code
python manage.py migrate
6. Start the server
bash
Copy code
python manage.py runserver
The API will be available at http://127.0.0.1:8000.

Usage
You can use the API by sending a POST request to the /predict/ endpoint with an image file of a chest X-ray.

Example request:

bash
Copy code
curl -X POST -F "image=@path/to/your/xray_image.jpg" http://127.0.0.1:8000/api/predict/
The response will contain the predicted label (Pneumonia or Normal) and the confidence score.

API Endpoints
/api/predict/
Method: POST
Description: Accepts an image of a chest X-ray and returns the prediction (Pneumonia/Normal) with confidence score.
Request:
image: The chest X-ray image to analyze (JPEG/PNG format).
Response:
json
Copy code
{
  "prediction": "Pneumonia",
  "confidence": 0.95
}
Model Information
This project uses a pre-trained model saved as exported_model.pkl using FastAI. The model was trained to detect pneumonia from chest X-ray images.

How to train the model
To train a similar model, follow these steps:

Collect and preprocess the chest X-ray dataset.
Use FastAI to build and train the model.
Export the model using the learn.export() method.
Dependencies
Python 3.7+
Django 3.0+
FastAI
PyTorch
Django REST Framework
Install dependencies with:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet
Copy code
