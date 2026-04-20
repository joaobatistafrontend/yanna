from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback, Perfil
from .forms import CustomUserCreationForm
from django.contrib.auth import login


@login_required
def home(request):
    perfil, _ = Perfil.objects.get_or_create(
        user=request.user,
        defaults={'tipo': 'cliente'}
    )

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.cliente = request.user
            fb.save()
            return redirect('home')
    else:
        form = FeedbackForm()

    # CLIENTE só vê o dele
    if perfil.tipo == 'cliente':
        feedbacks = Feedback.objects.filter(cliente=request.user)

    # ATENDENTE / ANALISTA / GESTOR vê tudo
    else:
        feedbacks = Feedback.objects.all()

    return render(request, 'home.html', {
        'form': form,
        'feedbacks': feedbacks,
        'perfil': perfil
    })



def singup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 🔥 login automático
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'singup.html', {'form': form})