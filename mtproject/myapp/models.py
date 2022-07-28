from django.db import models

# Create your models here

class Board(models.Model):#django.db.models.Model 상속
    board_title = models.CharField(max_length=20)
    board_text = models.TextField()
    
class Comment(models.Model):
    comment_text = models.TextField()
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
