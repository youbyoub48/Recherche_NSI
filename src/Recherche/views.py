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
        fin = position+len(motif)
        texte_gauche = texte[0:position]
        texte_millieu = texte[position:fin]
        texte_droit = texte[fin:]
        return render(request, "index.html", context={"texte_gauche": texte_gauche, "texte_millieu": texte_millieu, "texte_droit": texte_droit, "motif": motif, "position": position})