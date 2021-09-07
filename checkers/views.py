from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from checkers.forms import savedGameFormCheckers
from checkers.models import savedGameCheckers
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from checkers.serializers import CheckersSerializer, UserSerializer

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            new_game_form = savedGameFormCheckers(request.POST)
            if (new_game_form.is_valid()):
                match = new_game_form.cleaned_data["match"]
                user = User.objects.get(id=request.user.id)
                savedGameCheckers(user = user, match = match).save()
                return redirect("checkers")
            else:
                context = {"form_data": new_game_form}
                return render(request, 'checkers/home.html', context)
        else:
            return redirect("checkers")

    else:
        context = {"form_data": savedGameFormCheckers()}
        return render(request, 'checkers/home.html', context)


@login_required(login_url='/login/')
def history(request):

    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        savedGameCheckers.objects.filter(id=id).delete()
        return redirect("checkers_history")

    table_data = savedGameCheckers.objects.select_related().filter(user=request.user)

    context = {
        "table_data": table_data,
    }

    return render(request, 'checkers/history.html', context)


class CheckersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Checkerss to be viewed or edited.
    """
    queryset = savedGameCheckers.objects.all()
    serializer_class = CheckersSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
