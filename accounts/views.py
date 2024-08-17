from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from accounts.forms import UsuarioForm

def createuser(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoa/')
        else:
            return render(request, "accounts/form.html", {"form" : form})
    else:
        form = UsuarioForm()
        return render(request, "accounts/form.html", {"form" : form})