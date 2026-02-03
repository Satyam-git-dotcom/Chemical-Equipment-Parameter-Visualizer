from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Keep only last 5 datasets
        if Dataset.objects.count() > 5:
            Dataset.objects.order_by('uploaded_at').first().delete()

    def __str__(self):
        return self.name