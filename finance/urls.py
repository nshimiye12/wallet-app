from django.urls import path
from . import views
urlpatterns = [
    path("", views.home,name='finance-home'),
    path("expense/", views.expense,name='finance-expense'),
    path("transactions/", views.transactions, name="finance-transactions"),  # This line should exist

    path("transactions/add/", views.add_transaction, name="finance-add-transaction"),

    path("view-transactions/", views.view_transactions, name="view_transactions"),
    path('add/', views.add_transaction, name='add_transaction'),



]