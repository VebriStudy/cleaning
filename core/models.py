from django.db import models

class CleaningService(models.Model):
    CATEGORY_CHOICES = [
        ('rumah', 'Rumah'),
        ('kantor', 'Kantor'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='rumah')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('on_progress', 'On Progress'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ]
    service = models.ForeignKey(CleaningService, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"
