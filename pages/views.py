from django.shortcuts import render
from pages.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'pages/index.html', {'users': User.objects.all()})


@login_required
def blog_list_view(request):
    my_blogs = Blog.objects.filter(user=request.user)

    data = []
    for i in my_blogs:
        data.append({
            'title' :i.title,

        })
    return JsonResponse(data)
