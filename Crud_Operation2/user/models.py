from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.TextField()
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    id = models.AutoField(primary_key=True,)

    def __str__(self):
        return self.name