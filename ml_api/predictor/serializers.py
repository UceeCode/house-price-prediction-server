from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    Bedrooms = serializers.IntegerField()
    Toilets = serializers.IntegerField()
    Parking_Space = serializers.IntegerField()