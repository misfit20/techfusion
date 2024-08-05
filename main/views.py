from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from signup.models import Post
from django.contrib.auth.models import User, Group

# Create your views here.

def account_locked(request):
    return render(request, 'account_locked.html')


@login_required(login_url="login/")
def homepage(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
             post = Post.objects.filter(id=post_id).first()
             if post and (post.author == request.user or request.user.has_perm("signup.delete_post")):
                 post.delete()
       
        
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:

                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)

                except:
                    pass

                try:
                    group = Groub.objects.get(name='mod')
                    group.user_set.remove(user)

                except:
                     pass
                        
    return render(request, 'homepage.html', {"posts":posts})