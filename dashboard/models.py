from django.db import models

class DashboardStat(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.value}"
