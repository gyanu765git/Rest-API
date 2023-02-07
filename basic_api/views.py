from .models import apiModel
from .serializers import apiSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
       
from rest_framework import generics

from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })

class apiViewList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = apiModel.objects.all()
    serializer_class = apiSerializer


class apiViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = apiModel.objects.all()
    serializer_class = apiSerializer
   

# @api_view(["GET","POST"])
# def apiViewList(request):
#     permission_classes=(IsAuthenticated)
#     if request.method=="GET":
#         objects=apiModel.objects.all()
#         serializer=apiSerializer(objects,many=True)
#         return Response(serializer.data)

#     if request.method=="POST":
#         serializer=apiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)    
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","DELETE"])
# def apiViewDetail(request,pk):
#     try:
#         object=apiModel.objects.get(pk=pk)
#     except apiModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)    

#     if request.method=="GET":  
#         serializer=apiSerializer(object)
#         return Response(serializer.data)

#     if request.method=="PUT":
#         serializer=apiSerializer(object,data=request.data)
#         if serializer.is_valid():
#             serializer.save()  
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

#     if request.method=="DELETE":
#         object.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)          
