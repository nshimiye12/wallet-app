from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("IN", "Income"),
        ("OUT", "Expense"),
    ]

    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} ({self.category})"



class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
