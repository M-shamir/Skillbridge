from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BeneficiaryProfile


class BeneficiaryRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    age = serializers.IntegerField()
    category_id = serializers.IntegerField()
    documents = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = BeneficiaryProfile
        fields = ["username", "email", "age", "category_id", "documents"]

    def create(self, validated_data):
        from categories.models import Category

      
        username = validated_data.pop("username")
        email = validated_data.pop("email")
        age = validated_data.pop("age")
        category_id = validated_data.pop("category_id")
        documents = validated_data.pop("documents", "")

        user = User.objects.create_user(username=username, email=email, password=None, is_active=False)

        category = Category.objects.get(pk=category_id)

        
        beneficiary = BeneficiaryProfile.objects.create(
            user=user,
            age=age,
            category=category,
            documents=documents,
            status="PENDING"
        )
        return beneficiary






class BeneficiaryApproveSerializer(serializers.Serializer):
    id = serializers.IntegerField()

