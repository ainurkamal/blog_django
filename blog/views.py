from django.shortcuts import render


def posts_list(request):
    n = ['Ainur', 'Julia', 'Gulshat', 'Roman']
    return render(request, 'blog/index.html', context={'names': n})
