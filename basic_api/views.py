from .models import apiModel
from .serializers import apiSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# write your views from here
@api_view(["GET","POST"])
def apiViewList(request):
    if request.method=="GET":
        objects=apiModel.objects.all()
        serializer=apiSerializer(objects,many=True)
        return Response(serializer.data)

    if request.method=="POST":
        serializer=apiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def apiViewDetail(request,pk):
    try:
        object=apiModel.objects.get(pk=pk)
    except apiModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    

    if request.method=="GET":  
        serializer=apiSerializer(object)
        return Response(serializer.data)

    if request.method=="PUT":
        serializer=apiSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    if request.method=="DELETE":
        object.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)          
