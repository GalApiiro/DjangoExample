from rest_framework.decorators import api_view


class Dog:
    def __init__(self):
        self.dogs = []

    @api_view()
    def list_dogs(self):
        return self.dogs

    @api_view(['PUT', 'POST'])
    def add_dog(self, dog):
        self.dogs.append(dog)
