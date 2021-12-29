from flask_restx import Api, Resource

def add_endpoints(api):
    PROVIDER2 = api.namespace("provider2", description="Another provider")

    @PROVIDER2.route("/baseroute")
    class SomeController2(Resource):

        def get(self):
            return [], 200

        def post(self):
            return 200

api = Api(
    title="My Title",
    version="1.0",
    description="A description",
)

PROVIDER1 = api.namespace("provider1", description="Some provider")
@PROVIDER1.route("/baseroute")
class SomeController(Resource):

    def get(self):
        return [], 200
    
    def put(self):
        return 200
    
    def nohttpmethod(self):
        return 200

add_endpoints(api)