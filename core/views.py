from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Project
from .models import ContactMessage, GroupeCompetence, ModuleAcademique, AutoFormation


def home(request):
    projets = Project.objects.prefetch_related('stacks').all()
    groupes = GroupeCompetence.objects.prefetch_related('competences').all()
    modules = ModuleAcademique.objects.all()
    auto_formations = AutoFormation.objects.all()
    return render(request, 'home.html', {
        'projets': projets,
        'groupes': groupes,
        'modules': modules,
        'auto_formations': auto_formations,
    })


def cookies(request):
    return render(request, 'cookies.html')


def contact(request):
    if request.method == 'POST':
        prenom = request.POST.get('prenom', '').strip()
        nom = request.POST.get('nom', '').strip()
        email = request.POST.get('email', '').strip()
        objet = request.POST.get('objet', '').strip()
        message = request.POST.get('message', '').strip()

        if prenom and nom and email and objet and message:
            ContactMessage.objects.create(
                prenom=prenom,
                nom=nom,
                email=email,
                objet=objet,
                message=message,
            )
            return redirect('contact_merci')
        else:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')

    return redirect('home')


def contact_merci(request):
    return render(request, 'contact_merci.html')
