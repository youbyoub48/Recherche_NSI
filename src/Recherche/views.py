from django.shortcuts import render

import API

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    
    elif request.method == "POST":
        motif = request.POST.get("motif")
        texte = request.POST.get("texte")
        print(motif)
        print(texte)
        return render(request, "index.html")