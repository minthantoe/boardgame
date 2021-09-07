from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class savedGameCheckers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    @property
    def since(self):
      return (timezone.now() - self.date).days
