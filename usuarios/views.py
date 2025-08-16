from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)  # <- usamos login de Django renombrado
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('login_usuarios')
        else:
            messages.error(request, 'Error al crear la cuenta. Por favor verifique los datos ingresados.')
    else:
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


def login_usuarios(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  # <- usamos login de Django renombrado
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('lista_cancha')
            else:
                messages.error(request, 'Credenciales inválidas.')
        else:
            messages.error(request, 'Error al iniciar sesión. Verifica nuevamente.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})


def logout_usuarios(request):
    auth_logout(request)  # <- usamos logout de Django renombrado
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login_usuarios')
