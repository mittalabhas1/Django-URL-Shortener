from rest_framework import serializers
from .models import URLDatabase

class URLSerializer(serializers.ModelSerializer):
	class Meta:
		model = URL
		fields = ('long_url', 'short_url', 'visits', 'last_visit_time')
