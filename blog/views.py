from django.shortcuts import render, redirect , get_object_or_404
from.models import Category, Post
from .forms import CategoryForm, PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator #무슨 의미? 1~100 중 1~10번까지 /그다음페이지 앞에 열개는 빼고 11~20까지


# Create your views here.
  #로그인 인증된 사람만 편집? -blog 누르면 로그인 화면해야 사용가능
                #로그인 되있으면 밑에 함수로 넘어감 여기 적은 view에 적용(blog.view)
def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'categories':categories,          #무슨의미?
               'posts':posts
               }
    return render(request, 'blog/index.html',context)

def category_list(request):
    categories = Category.objects.all()
    posts= Post.objects.all()
    context = {'categories':categories,
               'posts':posts} # 무슨 의미?
    return render(request,'blog/category_list.html', context)

@login_required
def category_add(request):
    if request.method == 'POST':   #무슨의미?
        form = CategoryForm(request.POST)
        #유효성 검증
        if form.is_valid():
            form.save()
            return redirect('blog:category_list')
            
   
        pass
    elif request.method == "GET": # form 입력하는 페이지는 표시
        form = CategoryForm()  
    return render(request, 'blog/category_form.html', context={'form':form})

def post_detail(request, post_id):
    #post_id의 post를 보내주기
    post = Post.objects.get(pk=post_id)    #왼쪽옆에 원래있던 카테고리 목록 표시해줌
    posts = Post.objects.filter(category=post.category) #현재 보는 내용에 추가
    categories = Category.objects.all()
    context = {'post':post,'categories':categories}   #무슨 의미?
    return render(request,'blog/post_detail.html', context)

def category_post_list(request, category_id):
    #category_id인 카테고리에 속한 포스트들의 리스트를 보여주기
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()

    posts = Post.objects.filter(category=category)
    context = {'posts':posts, 'category' : category ,'categories': categories}
    return render(request, 'blog/index.html', context)

# def category_create(request):
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:category_list')  # 생성 후 목록으로 리다이렉트
#     else:
#         form = CategoryForm()
#     return render(request, 'blog/category_form.html', {'form': form})

@login_required
def post_write(request,category_id):
    if request.method == 'GET':
        category = Category.objects.get(pk=category_id)
        categories = Category.objects.all()
        form = PostForm()
        context={'form':form,'categories':categories,'category':category}
        return render(request=request, template_name='blog/post_form.html',context=context)
    # elif request.meghod=='POST'
    #     PostForm

    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            category = Category.objects.get(pk=category_id)
            post.category = category # 카테고리 설정
            # 추가적으로 작가 정보를 넣어야 됩니다!!
            # 어떻게 하면 될까요??
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post_id=post.id) #밑에거와는 입력한뒤 보여준
            # return redirect('blog:index')

@login_required
def post_edit(request, post_id):
    #post_id인 post의 내용을 편집
    #작성 폼의 형태는 기본 post와 같지만
    #이전의 내용이 담겨 있어야 효과적인 편집이 가능.
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        form = PostForm(instance= post)
        context={'form':form}
        return render(request,'blog/post_form.html', context)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save() # 내가 저장한 내용이 잘 보이는지 확인하고 싶습니다.
            return redirect('blog:post_detail', post_id=post.id)

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('blog:index')

def search(request):
    """    
    """
    # 해당 검색어로 table 조회
    # 조회 결과를 page와 결합해서(렌더링) 페이지를 응답하면 끝  /filter를 이용해서 Q사용
    query= request.GET['query']
    posts = Post.objects.select_related('author','category').all() #vs Post.objects.all() 전체 속도차이 실험/select_related(): 외래 키로 연결된 데이터도 함께 가져와서 성능을 개선합니다.

    searched_posts = posts.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(author__username__icontains=query) |
        Q(category__name__icontains=query)
        )
    
    # Pagination 적용 /게시판 사용? 화면 구성
    paginator = Paginator(searched_posts, 2)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context = {'searched_posts':page_obj}
    return render(request, 'blog/search.html',context)