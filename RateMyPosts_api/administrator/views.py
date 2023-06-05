from rest_framework.decorators import api_view
from django.http import JsonResponse

from django.shortcuts import render
from administrator.models import Tag

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
    serializer_data = TagSerializer(tags, many = True)
    # print(serializer_data)
    return JsonResponse({"tagList":serializer_data.data})  

@api_view(["POST"])
def postfun(request):
    params = request.data
    serialized_data = PostSerializer(data=params)
    print(serialized_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({"successMessage": "successfully posted"})
    else:
        return JsonResponse({"errorMessage": "Validation failed!"})


def statisticsfun(request):
    return render()
