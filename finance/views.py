from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Transaction


# Create your views here.
def home(request):
    return render (request, "finance/index.html")

def expense(request):
    return render (request, "finance/transactions.html")
def transactions(request):
    transactions = Transaction.objects.all().order_by("-date")
    return render(request, "finance/transactions.html", {"transactions": transactions})

def add_transaction(request):
    if request.method == "POST":
        transaction_type = request.POST.get("transaction_type")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        description = request.POST.get("description")

        Transaction.objects.create(
            transaction_type=transaction_type,
            amount=amount,
            category=category,
            description=description,
        )
        return redirect("finance-transactions")

    return render(request, "finance/add_transaction.html")


def view_transactions(request):
    transactions = Transaction.objects.all()  
    context = {
        "transactions": transactions
    }
    return render(request, "finance/view_transactions.html", context)


