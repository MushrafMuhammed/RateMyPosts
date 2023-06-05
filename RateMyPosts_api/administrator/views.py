from django.shortcuts import render

# Create your views here.
def postfun(request):
    
    return render(request, 'administrator/post.html')
