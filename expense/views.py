from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import ExpenseSerializer,SummarySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
# Create your views here.

class ExpenseViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.filter(is_deleted=False).order_by('-id')
    serializer_class = ExpenseSerializer
    http_method_names = ['post','pacth','get']
    search_fields = ['name']
    

class FilterExpenseView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.filter(is_deleted=False).order_by('-id')
    serializer_class = ExpenseSerializer
    
    def get(self,request,month,year,*args,**kwargs):
        try:
            filter_queryset = self.queryset.filter(created_at__month=month,created_at__year=year)
            serializer = self.serializer_class(filter_queryset,many=True)
            return Response({
                'date':f'{month}/{year}',
                'data':serializer.data,
                'status_code':status.HTTP_200_OK
                })
        except Exception as error:
            print(error)
            return Response({
                'message':'oops something went wrong',
                'status_code':status.HTTP_500_INTERNAL_SERVER_ERROR
            })
        

class ExpenseSummaryView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Expense.objects.filter(is_deleted=False).order_by('-id')
    serializer_class = SummarySerializer

    def get(self,request,*args,**kwargs):
        queryset = self.queryset.aggregate(total_expense=Sum('amount'),remaining_amount=Sum('amount'))
        return Response({
            'data':queryset
        })