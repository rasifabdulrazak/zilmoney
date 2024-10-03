from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewset,FilterExpenseView,ExpenseSummaryView

router = DefaultRouter()
router.register('expenses',ExpenseViewset,'expenses')

urlpatterns = [
    path('', include(router.urls)),
    path('expense/total/',ExpenseSummaryView.as_view(),name='summary_expense'),
    path('expenses/month/<str:month>/<str:year>/',FilterExpenseView.as_view(),name='filter_expense'),
    
]
