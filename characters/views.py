from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from characters.models import Character, CharacterForm
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'index.html')

def diceroll(request):
    return render(request, 'diceroll.html')

@login_required
def mycharacters(request):
    user_characters = Character.objects.filter(user=request.user)
    return render(request, 'mycharacters.html', {'characters': user_characters})

    
def newcharacter(request):
    user_characters = Character.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('mycharacters')
    else:
            form = CharacterForm(initial={'user': request.user})
    return render(request, 'newcharacter.html', {'form': form, 'characters': user_characters})

def editcharacter(request, pk):
        character = get_object_or_404(Character, pk=pk)
        if request.method == 'POST':
            form = CharacterForm(request.POST, request.FILES, initial={'user': request.user}, instance=character)
            if form.is_valid():
                form.save()
            return redirect('mycharacters')
        else:
            form = CharacterForm(initial={'user': request.user}, instance=character)
        return render(request, 'editcharacter.html', {'form': form, 'character':character})
    
     
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                # Authentication succeeded, so log in the user
                login(request, user)
                return redirect('index')
            else:
                # Authentication failed, show an error message
                error_message = "Invalid username or password. Please try again."
                return render(request, 'signup.html', {'form': form, 'error_message': error_message})
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})