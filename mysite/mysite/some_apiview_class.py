from rest_framework.views import APIView


class SomeApiView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def head(self, request):
        pass

    def non_http_method(self, request):
        pass
