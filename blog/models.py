from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100, unique=True, verbose_name='카테고리명')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name= '생성일')

    def __str__(self) -> str:
        return self.name     #super 부모메서드
    
    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural ='카테고리 목록'  #admin 페이지에서  이름변경할때 볼 수 있음
        db_table = 'lion_blog_category' #db에 이름 내가 정할 수 있음 보통 앱-테이블 이름 순서
                                        #blog_category 원래
        ordering = ['name']


class Post(models.Model):
    author = models.ForeignKey('auth.User' , on_delete=models.CASCADE) #편집할때 아무나 못하고 권한있는 아이디만/ 아이디 삭제 글도 삭제//아디삭제해도 글은 남게는 어떻게? author_
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='카테고리')  #foreign키 외부 category_id
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='게시글'
        verbose_name_plural='게시글 목록'
        db_table = 'lion_blog_post'
        ordering = ['-create_at']
        indexes = [
            models.Index(fields=['-create_at'])     
        ]
                                