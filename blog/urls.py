from django.urls import path
from . import views

app_name ='blog'   #html에서 페이지 링크 {% url blog:category_list %} 네임스페이스에 사용됨.

urlpatterns = [
    #카테고리 표시 /카테고리 나열-DB에서 카테고리 리스트를 조회->templates
    path('category/', views.category_list, name='category_list'),     #name은 네임스페이스 뒤에 사용 쉽게생각하면 사이트 페이지 카테고리 별로 이름 붙여주는것
    path('category/add/', views.category_add, name='category_add'), #카테고리 추가
    path('category/<int:category_id>',views.category_post_list, name='category_post_list'), #특정 카테고리에 속한 post 보여주기
    


    # #게시글 관련 URL

    path('', views.index , name='index'),  #전체포스트의 나열, 리스트표시, 카테고리에 상관없이 시간순 내림차순-> 카테고리로 나열화면으로 가는 링크 추가
    path('post/<int:post_id>',views.post_detail, name='post_detail'), #한 포스트에 대한 세부내용(블로그 내용 표시)
    path('post/write/<int:category_id>/', views.post_write, name='post_write'), #포스트 생성
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'), #어떤 포스트 편집 (update)
    path('post/<int:post_id>/delete',views.post_delete,name='post_delete'), #어떤 포스트 삭제
     # Search
    path('search/', views.search, name='search'),
    path('search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),   #검색어 밑에 자동검색어

]