from rest_framework.views import APIView
from rest_framework.response import Response
from tinydb import TinyDB, Query
# from .utils import validate, get_type
import json


class FormAPIView(APIView):
    def post(self, request):
        db = TinyDB("db.json")
        print(db.all())
        Form = Query()
        data = request.data

        print(db.search(Form.field_name_4.matches("[aZ]*")))
        
        var = "field_name_4"
        print(db.search(getattr(Form, f'{var}').matches("[aZ]*")))
        return Response({"something":"something"})
