from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer


@api_view(["GET", "DELETE", "PUT"])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == "GET":
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)
    # delete a single puppy
    elif request.method == "DELETE":
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single puppy
    elif request.method == "PUT":
        serializer = PuppySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def get_post_puppies(request):
    # get all puppies
    if request.method == "GET":
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    elif request.method == "POST":
        data = {
            "name": request.data.get("name"),
            "age": int(request.data.get("age")),
            "breed": request.data.get("breed"),
            "color": request.data.get("color"),
        }
        serializer = PuppySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
