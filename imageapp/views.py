from django.shortcuts import render , redirect , get_object_or_404
from .models import ImagePost
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST  #ajax로 할때
from .forms import ImagePostForm
from django.http import JsonResponse #ajax
# Create your views here.

# 전체 이미지 갤러리 보여조ㅜ기
def index(request):
    images = ImagePost.objects.all()
    context = {"images":images}
    return render(request, 'imageapp/index.html', context)

#detail
def  image_detail(request, image_id):
    image = get_object_or_404(ImagePost, pk=image_id)
    context = {'image':image , 'subscribed':image.is_subscribed(request.user)}
    return render(request, 'imageapp/image_detail.html', context)
#새게시글
@login_required
def image_write(request):
    if request.method =="POST":
        # 전송된 데이터를 저장(이미지파일이라서 약간 다름)
        form = ImagePostForm(request.POST, request.FILES)
       
        if form.is_valid(): #작성자 정보
            image_post = form.save(commit=False)
            image_post.author=request.user
            image_post.save()
            return redirect('imageapp:index')

    else:
        # 폼 생성

        form = ImagePostForm()
        return render(request, 'imageapp/image_form.html', {"form":form})



#수정
@login_required
def image_edit(request, image_id):
    image_post = get_object_or_404(ImagePost, pk=image_id)
    if request.method =="POST":
        # 전송된 데이터를 저장
        form = ImagePostForm(request.POST, request.FILES, instance=image_post)
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.author=request.user
            image_post.save()
            return redirect('imageapp:index')
    else:
        # 폼 생성        
        form = ImagePostForm(instance=image_post)
        return render(request, 'imageapp/image_form.html', {"form":form})

#삭제
@login_required
def image_delete(request, image_id):
    image_post = get_object_or_404(ImagePost, pk=image_id)
    image_post.delete()
    return redirect('imageapp:index')


#구독
# @login_required
# def toggle_subscribe(request, image_id):
#     #image_id를 가진 포스트를 가져와서
#     image_post = get_object_or_404(ImagePost , pk=image_id)
#     if image_post.is_subscribed(request.user):
#         image_post.unsubscribe(request.user)
#     else:
#         image_post.subscribe(request.user)
#     return redirect('imageapp:image_detail', image_id)

@login_required
@require_POST
def toggle_subscription(request, image_id):
    # post를 가져오기
    post = ImagePost.objects.get(pk=image_id)
    # 사용자를 가져와서
    user = request.user
    # 구독을 했는지 안했는지에 따라서
    if post.is_subscribed(user):
        post.unsubscribe(user)
        status = "unsubscribed"
    else:
        post.subscribe(user)
        status = "subscribed"
    # status 리턴
    context = {
        'status':status,
        'subscriber_count':post.get_subscriber_count()
    }
    return JsonResponse(context)

    

