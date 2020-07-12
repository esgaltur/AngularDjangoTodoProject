import json
from json import JSONEncoder

from django.db.models import Min, Max
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_api import JsonModel
from rest_api.JsonModel import TodoJsonModel
from rest_api.models import Todo, TodoSerializer
from django.core import serializers


class BaseManageView(APIView):
    """
    The base class for ManageViews
        A ManageView is a view which is used to dispatch the requests to the appropriate views
        This is done so that we can use one URL with different methods (GET, PUT, etc)
    """

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD static dictionary variable must be defined on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request, *args, **kwargs)

        return Response(status=405)


class TodoRetrieveView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateView(UpdateAPIView):
    lookup_field = 'id'
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreateView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDeleteView(DestroyAPIView):
    lookup_field = 'id'
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoManageView(BaseManageView):
    VIEWS_BY_METHOD = {
        'GET': TodoRetrieveView.as_view,
        'POST': TodoCreateView.as_view,
        'PUT': TodoUpdateView.as_view,
        'DELETE': TodoDeleteView.as_view,
    }

class TodoPkGet(APIView):
    def get(self,request):
        return JsonResponse(data={"next_id":Todo.objects.aggregate(Max("id"))['id__max']+1})

class TodoView(APIView):

    def get(self, request, *args, **kwargs):
        return self.get_all_todos()

    def get_all_todos(self):
        list_of_todos = Todo.objects.all()
        json_list = []
        for item in list_of_todos:
            m = TodoJsonModel(item.id, item.description, item.targetDate, item.IsDone)
            json_list.append(m.__dict__)
        return JsonResponse(json_list, safe=False)
