from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,unique = True)
    title = models.CharField(max_length = 300,blank=True)
    profile_image = models.ImageField(upload_to = 'profiles/')

    def __str__(self):
        return self.user.username

class Question(models.Model):
    question_id = models.AutoField(primary_key = True,null=False)
    question = models.CharField(max_length = 500)
    date_updated = models.DateTimeField(auto_now = True)
    asked_by = models.ForeignKey(Profile,to_field = "user",on_delete = models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer_id = models.AutoField(primary_key = True,null = False)
    answer = models.CharField(max_length = 2000)
    question_id = models.ForeignKey(Question,on_delete = models.CASCADE)
    date_answered = models.DateTimeField(auto_now = True)
    answered_by = models.ForeignKey(Profile,on_delete = models.CASCADE,to_field = "user")

    def __str__(self):
        return self.answer

class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    comment = models.CharField(max_length = 2000)
    posted_date = models.DateTimeField(auto_now = True)
    answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE)
    commented_by = models.ForeignKey(Profile,on_delete = models.CASCADE,to_field = "user")

    def __str__(self):
        return self.comment

class Poll(models.Model):
    poll_id = models.AutoField(primary_key = True)
    poll_type = models.IntegerField(null=True)
    answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE)
    polled_by = models.ForeignKey(Profile,on_delete = models.CASCADE,to_field = "user")
