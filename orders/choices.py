from django.db import models


class OrderStatusChoices(models.TextChoices):
    New = 'New'
    ProcessInProgress = 'Process In Progress'
    Cancel = 'Cancel'
    Paid = 'Paid'
