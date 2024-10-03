from rest_framework import serializers
from .models import Expense
from django.db import transaction

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['created_at','updated_at','is_active','is_deleted']

    
    def validate(self, attrs):
        if attrs.get('amount')<=0:
            raise serializers.ValidationError({'error':'Please enter a valid amount'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        try:
            with transaction.atomic():
                expense = Expense.objects.create(**validated_data)
        except Expense as e:
            print(e)
            raise serializers.ValidationError({'error':'something went wrong!'})
        return expense
    

class SummarySerializer(serializers.Serializer):
    total_expense = serializers.DecimalField(max_digits=10,decimal_places=2)
    # remaining_expense = serializers.DecimalField(max_digits=10,decimal_places=2)