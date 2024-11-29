from django.shortcuts import render, get_object_or_404
from .models import Movie, Comment

# 메인 페이지
def home(request):
    return render(request, 'home.html')

# 영화 리스트 페이지
def movie_list(request):
    movies = Movie.objects.all()  # 영화 3개 가져오기
    return render(request, 'movie/movie_list.html', {'movies': movies})

# 영화 상세 페이지
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    comments = movie.comments.all()

    if request.method == "POST":
        user = request.POST['user']
        content = request.POST['content']
        Comment.objects.create(movie=movie, user=user, content=content)

    return render(request, 'movie/movie_detail.html', {'movie': movie, 'comments': comments})
