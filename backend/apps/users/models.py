from django.db import models
from apps.shared.models import BaseModel
from apps.shared.utils import UserStatus, Language

# Create your models here.

class BotUser(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, choices = Language.choices(), default=Language.UZBEK)
    user_status = models.CharField(max_length=100, choices = UserStatus.choices(), default=UserStatus.ACTIVE)

    def __str__(self):
        return self.username
    