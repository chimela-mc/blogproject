from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=80, blank=False)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title
    
    # def get_log_message(self):
    #     return f"Created on {self.time.strftime('%Y-%m-%d %H:%M:%S')}"

    
class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"T