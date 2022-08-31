from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import task, Subtask, User
from .serializer import TaskSerializer

class TaskAPIView(APIView):
    def get(self, request):
        listTask = task.objects.filter( user_id_id = request.session.get("id")).order_by('color').values()
        user = User.objects.filter(id = request.session.get("id")).values()
        listSubtasks = Subtask.objects.all().values()
        for i in range(len(listTask)):
            listSubtasks = list(Subtask.objects.filter(head_id_id = listTask[i]["id"]).values())
            listTask[i]["subtask"] = listSubtasks
        return Response({"tasks" : list(listTask), "user": user[0]["login"]})
    def post(self, request):
        if request.data["place"] == "task":
            new_task = task.objects.create(
                title = request.data["title"],
                color = request.data["color"],
                user_id_id = request.session.get("id")
            )
            return Response({"new_task": new_task})
        elif request.data["place"] == "subtask":
            new_subtask = Subtask.objects.create(
                title = request.data["title"],
                head_id_id = request.data["head_id"],
            )
            return Response({"new_subtask": new_subtask})
        elif request.data["place"] == "delete_subtask":
            Subtask.objects.filter(id=request.data["id"]).delete()
            return Response({})
        elif request.data["place"] == "delete_task":
            task.objects.filter(id=request.data["id"]).delete()
            return Response({})
    #queryset = task.objects.all()
    #serializer_class = TaskSerializer

class UserAPIView(generics.ListAPIView):
    def get(self, request):
        listUser = User.objects.all().values()
        return Response({"user": listUser})
    def post(self, request):
        if(request.data["place"] == "login"):
            user = User.objects.filter(login = request.data["login"]).values()
            if not(user):
                return Response({"send": False})
            if request.data["password"] == user[0]["password"]:
                request.session["id"] = user[0]["id"]
                return Response({"send" : True})
            else:
                return Response({"send": False})

        elif (request.data["place"] == "register"):
            user = User.objects.filter(login = request.data["login"]).values()
            if user:
                return Response({"send": False})
            new_user = User.objects.create(
                login=request.data["login"],
                password=request.data["password"],
            )
            request.session["id"] = new_user.id
            return Response({"send": True})
        elif (request.data["place"] == "logout"):
            request.session["id"] = 0;
            return Response({"send": True})
# Create your views here.
