from django.shortcuts import render ,redirect, get_object_or_404
from django.views.generic import (
    ListView, 
    DetailView,
    DeleteView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Pays , Localite, Conseil
from django.db.models import Q


def home(request): # pour afficher les produits a vendre sur l_index
    context = {
        'pays': Pays.objects.all()
    }
    return render(request, 'tracker/index.html', context)

class PaysListView(ListView): # list des produits
    model = Pays
    template_name = 'tracker/index.html'
    context_object_name = 'pays'
    ordering = ['nom']
    paginate_by = 8

class Search(ListView): # Rechercher un Produit depuis index (home)
    model = Pays
    template_name = 'tracker/search.html'
    context_object_name = 'pays'
    ordering = ['nom']
    paginate_by = 1
    def get_queryset(self):
        query = self.request.GET.get('q')
        liste = Pays.objects.filter(
            Q(nom__icontains = query) 
        )
        return liste




class LocaliteListView(ListView):
    model = Localite
    template_name = 'tracker/pays_localite.html'
    context_object_name = 'local'
    ordering = ['nom']
    paginate_by = 8

    def get_queryset(self):
        country = get_object_or_404(Pays, nom=self.kwargs.get('nom'))
        return Localite.objects.filter(pays=country).order_by('created')
