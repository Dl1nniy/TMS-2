# Задача №3 Допишите класс Family таким образом чтобы он влялся итератором
# и мы могли при помощи цикла for вывести всех ченов семьи
class Family:

    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.members)

    def __next__(self):
        if self.counter < len(self.members):
            self.counter +=1
            return self.members[self.counter-1]
        else:
            raise StopIteration

    def add_family_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"

