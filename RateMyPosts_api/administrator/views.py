from rest_framework.decorators import api_view
from django.http import JsonResponse

from django.shortcuts import render
from administrator.models import Image, Post, Tag
from django.views.decorators.csrf import csrf_exempt


from administrator.serializer import PostSerializer, TagSerializer




# Create your views here.

@api_view(["POST"])
def tagfun(request):
    params = request.data
    serialized_data = TagSerializer(data=params)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({"successMessage": "Tag created successfully"})
    else:
        return JsonResponse({"errorMessage": "Validation failed!"})

@api_view(["GET"])
def viewTags_fun(request): #@admin side
    tags = Tag.objects.all()
    serialized_data = TagSerializer(tags, many=True)
    # print(tags)
    return JsonResponse({"tagList":serialized_data.data})  


@api_view(["GET"])
def view_tags(request):
    tags = Tag.objects.all().values('id', 'name')
    serialized_data = TagSerializer(tags, many=True)
    return JsonResponse({"tagList": serialized_data.data})

@api_view(["POST"])
def create_post(request):
    if request.method == 'POST':
        try:
            images = request.FILES.getlist('image')
            tag_id = request.POST.get('tag')
            description = request.POST.get('description')

            tag = Tag.objects.get(id=tag_id)

            post = Post.objects.create(
                description=description,
                tag=tag
            )

            for image in images:
                image_instance = Image.objects.create(image=image)
                post.images.add(image_instance)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'errorMessage': str(e)})

    return JsonResponse({'success': False, 'errorMessage': 'Invalid request method'})

@api_view(["GET"])
def get_images(request):
    images = Image.objects.all()
    image_urls = [image.image.url for image in images]
    return JsonResponse({"imageUrls": image_urls})





def statisticsfun(request):
    return render()
