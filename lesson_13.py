from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
response = requests.get(os.environ.get('https://jsonplaceholder.typicode.com/todos')).json
list_responce = response


class Todo:
    def __init__(self, user_id, todo_id, title, completed):
        self.user_id = user_id
        self.todo_id = todo_id
        self.title = title
        self.completed = completed

    def _repr(self):
        return f"User: {self.user_id}, Todo: {self.todo_id}, Title: {self.title}, Completed: {self.completed}"


class Todos:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, Todos).__new__(cls)
        return cls.instance

    def __init__(self):
        self.todos = list()
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.todos):
            count = self.counter
            self.counter += 1
            return self.todos[count]
        raise StopIteration

    def __len__(self):
        return len(self.todos)

    def update_todo_list(self):
        for todo in response:
            self.todos.append(
                Todo(user_id=todo['userId'], todo_id=todo['id'],
                     title=todo['title'], completed=todo['completed'])
            )

    def get_by_id(self, id):
        for todo in self.todos:
            if todo.id == int(id):
                return todo.show_stats()

    @staticmethod
    def write_to_json():
        with open('json_todo_list.json', 'w') as write_file:
            json.dump(list_responce, write_file, indent='')

    @staticmethod
    def read_to_json():
        with open('json_todo_list.json', 'r') as read_file:
            read_data = json.load(read_file)
        return read_data

    def from_json(self, json_data):
        todos_data = json.loads(json_data)
        for todo_data in todos_data:
            todo = Todo(
                todo_data['id'],
                todo_data['Userid'],
                todo_data['title'],
                todo_data['completed'],
            )

