from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    full_name = models.CharField(max_length=120)
    number_of_tweets = models.PositiveIntegerField()
    number_of_followers = models.PositiveIntegerField()
    number_of_friends = models.PositiveIntegerField()
    description = models.TextField()
    timestamp_created = models.DateTimeField(auto_now_add=True, auto_now = False)
    timestamp_updated = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self):        
        return self.name

class Fight(models.Model):
    user1 = models.ForeignKey(User, related_name='oponent1')
    user2 = models.ForeignKey(User, related_name='oponent2')
    time_of_fight = models.DateTimeField(auto_now_add=True)

