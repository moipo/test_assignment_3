from django.shortcuts import render

# Create your views here.

class Main:
    def main(request):
        ctx = {}
        return render(request,'main.html',ctx)
