from django.shortcuts import render

from API import tableau_sauts, boyer_moore_horspool

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    
    elif request.method == "POST":
        motif = request.POST.get("motif")
        texte = request.POST.get("texte")
        tDs = tableau_sauts(motif)
        position = boyer_moore_horspool(texte, motif, tDs)
        print(position)
        return render(request, "index.html")