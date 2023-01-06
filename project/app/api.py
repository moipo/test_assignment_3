from rest_framework.views import APIView
from rest_framework.response import Response

from tinydb import TinyDB, Query



class FormAPIView(APIView):
    def post(self, request):
        db = TinyDB("db.json")
        print(db.all())
        # db.insert({"type":"apple", "count":"7"})
        # print(db.all())
        return Response({"something":"something"})
