from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class savedGameChess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)

    @property
    def since(self):
      return (timezone.now() - self.date).days
