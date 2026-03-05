from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(
        null=True, blank=True, help_text='Optional due date')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    @property
    def is_overdue(self):
        """Check if item is overdue"""
        if not self.due_date or self.completed:
            return False
        return self.due_date < timezone.now().date()
