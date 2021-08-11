
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import  FeedbackSerializer
from .models import Feedback



class FeedbackView(APIView):
    """
    Posts and gets review given by visitor
    """
    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Feedback Submitted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    def get(self, request):
        try:
            user = request.user
            if user.is_member:
              member= Feedback.objects.all()
              serializer = FeedbackSerializer(member)
              return Response(serializer.data, status=status.HTTP_200_OK)
            else : return Response(status=status.HTTP_403_FORBIDDEN)
        except Feedback.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)


from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DepartmentSerializer

from .models import Department

# Create your views here.

class DepartmentListView(APIView):
    '''
    Gets a list of all Department objects
    '''

    def get(self, request):
        departments = Department.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = DepartmentSerializer(departments, many=True)
        return Response({"departments": departments})




class DepartmentDetailView(APIView):
    '''
    Gets a specific Department object corresponding to its name
    '''
    def get(self, request, name):
        department = get_object_or_404(Department,name=name)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

