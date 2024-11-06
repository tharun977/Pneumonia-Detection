from fastai.vision.all import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from PIL import Image
import io

# Load the FastAI model (Ensure this path is correct)
learn = load_learner('models/exported_model.pkl')  # Update this path if necessary

@api_view(['POST'])
def predict_pneumonia(request):
    try:
        # Ensure that the image is provided in the request
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image file provided'}, status=400)

        # Get the image from the request
        img_file = request.FILES['image']
        img = Image.open(img_file)

        # Resize the image to the required size (224x224 for most CNNs)
        img = img.resize((224, 224))

        # Make the prediction using the FastAI model
        pred, pred_idx, probs = learn.predict(img)

        # Prepare the response with the prediction and confidence score
        response = {
            'prediction': str(pred),  # Class prediction (e.g., 'pneumonia' or 'normal')
            'confidence': float(probs.max())  # Maximum confidence score for the prediction
        }
        return JsonResponse(response, status=200)

    except Exception as e:
        # Catch any errors and return the error message
        return JsonResponse({'error': str(e)}, status=400)
