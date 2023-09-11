from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

from AulaWeb.forms import TrocarSenhaForm


def logar(request):
    frm = AuthenticationForm(request, data=request.POST)

    if frm.is_valid():
        login(request, frm.get_user())
        return redirect(request.GET.get('next','home'))

    return render(request, "autenticacao/logar.html", {
        'frm': frm
    })

@login_required
def deslogar(request):
    logout(request)
    return redirect('login')

@login_required
def trocar_senha(request):
    form = TrocarSenhaForm(request.POST or None)
    if form.is_valid():
        request.user.set_password(form.cleaned_data['senha'])
        request.user.save()
        return redirect('home')

    return render(request, 'autenticacao/trocar_senha.html',{
          'frm':form
    })
