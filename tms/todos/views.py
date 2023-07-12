from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()


class Todo:

    def __init__(self, uid: int, id: int, title: str, status: bool):
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
    return render(request, "todos.html", {"todos": json_todo})


@csrf_exempt
def todos(request):
    if request.method == 'POST':
        task = dict(request.POST)
        for key in task:
            task[key] = task[key][0]

        task['uid'] = int(task['uid'])
        task['id'] = int(task['id'])
        task['title'] = str(task['title'])
        task['status'] = bool(task['status'])
        todo_list.update_todo_list()
        global json_todo
        json_todo = todo_list.convert_to_json()
    return render(request, "todos.html", {"todos": json_todo})


def create_todo(request):
    return render(request, "create_new_todo.html")
