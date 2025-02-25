# predictor/views.py
import joblib
from django.http import JsonResponse
from rest_framework.decorators import api_view
from predictor.serializers import PredictionSerializer


model = joblib.load("predictor/ml_model.pkl")

@api_view(['POST'])
def predict_price(request):
    serializer = PredictionSerializer(data=request.data)
    if serializer.is_valid():
        bedrooms = serializer.validated_data['Bedrooms']
        toilets = serializer.validated_data['Toilets']
        parkingspace = serializer.validated_data['Parking_Space']
        prediction = model.predict([[bedrooms, toilets, parkingspace]])[0]
        return JsonResponse({"Predicted Price": f"₦{round(prediction, 2)}"})
    return JsonResponse(serializer.errors, status=400)
