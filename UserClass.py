class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_active = True

    def __str__(self):
        return f'User: {self.name} - {self.age}'
