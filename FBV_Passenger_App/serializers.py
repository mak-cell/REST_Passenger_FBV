from FBV_Passenger_App.models import Passenger
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'