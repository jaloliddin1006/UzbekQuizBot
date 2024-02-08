from datetime import datetime
from django.db import models
from apps.shared.models import BaseModel
from apps.users.models import BotUser


    
class Question(BaseModel):
    code = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    answers = models.JSONField()
    file = models.FileField(upload_to='questions', null=True, blank=True)
    size = models.IntegerField(null = True, blank = True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.code} - {self.subject}"
    
    def save(self, *args, **kwargs):
        self.size = len(self.answers)
        super(Question, self).save(*args, **kwargs)
        

class UserQuestionAnswer(BaseModel):
    user = models.ForeignKey(BotUser, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.JSONField()
    correct_answers = models.JSONField(null = True, blank = True)
    score = models.IntegerField(null = True, blank = True)
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.user.username} - {self.question.code} - {self.answer}"
    
    def save(self, *args, **kwargs):
        if not self.start_time:
            self.start_time = datetime.now()
        self.end_time = datetime.now()
        super(UserQuestionAnswer, self).save(*args, **kwargs)
        
    class Meta:
        unique_together = ('user', 'question')    