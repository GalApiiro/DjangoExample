from rest_framework.decorators import api_view


class Dove:

    @api_view()
    def get_doves(self):
        return ["dove1", "dove2"]
