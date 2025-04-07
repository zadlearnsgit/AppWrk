from django.db import models

# Create your models here.


class Tansaction(models.Model):
    """
    Model representing a transaction.
    """

    date = models.DateField()
    description = models.CharField(max_length=255)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    running_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.description} - {self.running_balance}"
