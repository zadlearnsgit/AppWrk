from django.shortcuts import render, redirect
from cash.models import Tansaction
import datetime


def new_transaction(request):
    """
    View to create a new transaction.
    """
    if request.method == "POST":
        latest_balance = 0
        try:
            latest_transaction = Tansaction.objects.latest("date")
            latest_balance = latest_transaction.running_balance
        except Tansaction.DoesNotExist:
            # No transactions exist, so the latest_balance remains 0
            pass

        if request.POST.get("transaction_type") == "Credit":
            new_balance = latest_balance + int(request.POST.get("amount"))
        else:
            new_balance = latest_balance - int(request.POST.get("amount"))

        new_transaction = Tansaction(
            date=datetime.date.today(),
            description=request.POST.get("description"),
            credit=(
                int(request.POST.get("amount"))
                if request.POST.get("transaction_type") == "Credit"
                else 0
            ),
            debit=(
                int(request.POST.get("amount"))
                if request.POST.get("transaction_type") == "Debit"
                else 0
            ),
            running_balance=new_balance,
        )
        new_transaction.save()
        # Redirect to the office_transactions url
        return redirect("office_transactions")


    return render(request, "cash/new_transaction.html")


def office_transactions(request):
    """
    View to display all transactions.
    """
    all_transaction = list()
    transactions = Tansaction.objects.all().order_by("-id")
    for transaction in transactions:
        all_transaction.append(
            {
                "date": transaction.date.strftime("%m/%d/%Y"),
                "description": transaction.description,
                "credit": transaction.credit,
                "debit": transaction.debit,
                "running_balance": transaction.running_balance,
            }
        )
    return render(
        request, "cash/office_transactions.html", {"transactions": all_transaction}
    )
