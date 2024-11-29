from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # 영화 리스트 페이지
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),  # 특정 영화 상세 페이지
]
