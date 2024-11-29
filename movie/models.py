from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)  # 영화 제목
    description = models.TextField()          # 영화 설명
    image_name = models.CharField(max_length=100)  # 이미지 파일 이름
    release_date = models.DateField()         # 개봉일

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=50)    # 댓글 작성자
    content = models.TextField()              # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간

    def __str__(self):
        return f"{self.user}: {self.content[:20]}"