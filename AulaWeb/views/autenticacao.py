from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout


def logar(request):
    frm = AuthenticationForm(request, data=request.POST)

    if frm.is_valid():
        login(request, frm.get_user())
        return redirect(request.GET.get('next','home'))

    return render(request, "autenticacao/logar.html", {
        'frm': frm
    })

def deslogar(request):
    logout(request)
    return redirect('login')