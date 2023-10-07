from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    best_record = serializers.SerializerMethodField('_get_best_record')

    # Define a private method
    # Here, driver_object is a normal variable not keyword variable
    def _get_best_record(self, driver_object):
        best_time = 30 # minutes
        round_finishing_time=getattr(driver_object,'round_finishing_time')
        # round_finishing_time = driver_object.round_finishing_time
        if round_finishing_time and round_finishing_time < best_time:
            best_time = round_finishing_time
            return best_time
        else:
            return best_time
    
    class Meta:
        model = Driver
        fields = ['id','driver_name', 'car_brand',
                  'round_finishing_time', 'best_record']