from django.http import JsonResponse
from django.shortcuts import render

import requests

import json


response = requests.get('https://jsonplaceholder.typicode.com/todos').json()


class Todo:

    def __init__(self,uid: int, id: int, title: str, status: bool):
        self.uid = uid
        self.id = id
        self.title = title
        self.status = status

    def show_stats(self):
        return f'user {self.uid}, ID: {self.id}, title: {self.title}.'


class Todos:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, Todos).__new__(cls)
        return cls.instance

    def __init__(self):
        self.todos = list()
        self.counter = 0

    def update_todo_list(self):
        for todo in response:
            self.todos.append(
                Todo(uid=todo['userId'], id=todo['id'], title=todo['title'],
                     status=todo['completed'])
            )

    def convert_to_json(self):
        return [todo.__dict__ for todo in self.todos]


todo_list = Todos()
todo_list.update_todo_list()
json_todo = todo_list.convert_to_json()


def todo(request):
    return JsonResponse({'todos': json_todo})


def home(request):
    return render(request, 'home.html', {'todos': json_todo})