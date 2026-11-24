from django.shortcuts import render, get_object_or_404, redirect
from .models import Lote
from .forms import LoteForm

def lista_lotes(request):
    variedade = request.GET.get("variedade")
    lotes = Lote.objects.all()
    if variedade:
        lotes = Lote.objects.filter(variedade=variedade)
    return render(request, "citricultura/lista.html", {"lotes": lotes})

def detalhe_lote(request, id):
    lote = get_object_or_404(Lote, id=id)
    return render(request, "citricultura/detalhe.html", {"lote": lote})

def novo_lote(request):
    form = LoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_lotes")
    return render(request, "citricultura/form.html", {"form": form})