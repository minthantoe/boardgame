from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from chess.forms import savedGameFormChess
from chess.models import savedGameChess
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from chess.serializers import ChessSerializer, UserSerializer
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'chess/home.html')

@login_required(login_url='/login/')
def local(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            new_game_form = savedGameFormChess(request.POST)
            if (new_game_form.is_valid()):
                match = new_game_form.cleaned_data["match"]
                user = User.objects.get(id=request.user.id)
                savedGameChess(user = user, match = match).save()
                return redirect("chess_local")
            else:
                context = {"form_data": new_game_form}
                return render(request, 'chess/local.html', context)
        else:
            return redirect("chess_local")

    else:
        context = {"form_data": savedGameFormChess()}
        return render(request, 'chess/local.html', context)

@login_required(login_url='/login/')
def ai(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            new_game_form = savedGameFormChess(request.POST)
            if (new_game_form.is_valid()):
                match = new_game_form.cleaned_data["match"]
                user = User.objects.get(id=request.user.id)
                savedGameChess(user = user, match = match).save()
                return redirect("chess_ai")
            else:
                context = {"form_data": new_game_form}
                return render(request, 'chess/ai.html', context)
        else:
            return redirect("chess_ai")

    else:
        context = {"form_data": savedGameFormChess()}
        return render(request, 'chess/ai.html', context)

@login_required(login_url='/login/')
def history(request):

    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        savedGameChess.objects.filter(id=id).delete()
        return redirect("chess_history")

    table_data = savedGameChess.objects.select_related().filter(user=request.user)

    context = {
        "table_data": table_data,
    }

    return render(request, 'chess/history.html', context)

class ChessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Chesss to be viewed or edited.
    """
    queryset = savedGameChess.objects.all()
    serializer_class = ChessSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
