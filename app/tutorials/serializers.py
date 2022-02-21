from rest_framework import serializers
from tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('customer_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city')
