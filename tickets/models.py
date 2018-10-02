from django.db import models


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('REVIEW', 'In Review'),
        ('CLOSED', 'Closed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='OPEN')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title