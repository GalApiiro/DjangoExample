from rest_framework.decorators import api_view


class Dog:

    @api_view()
    def list_dogs(self):
        return ["Rex", "Lucky"]
