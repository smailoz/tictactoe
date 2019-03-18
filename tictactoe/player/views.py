from django.shortcuts import render, redirect, get_object_or_404                #8.12 kütüphaneyi de ekledik. Sondaki kütüphane 8.17 den geldi.
from django.contrib.auth.decorators import login_required      #8.3 login required
from django.core.exceptions import PermissionDenied                              # 8.17 den geldi. 
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from .forms import InvitationForm            # 8.8. forms un içinde oluşturulan formu çağııyorusz. 
from .models import Invitation               # 8.14 IntegrityError at /player/new_invitation NOT NULL constraint failed: player_invitation.from_user_id hatası sonrası bu kütüphaneyi yükledik. 
from gameplay.models import Game             # gameplayin içerisindeki modellerden Game i import et. 


@login_required()                                                 #8.3 login required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    finished_games = my_games.difference(active_games)  
    invitations = request.user.invitation_received.all()       # 8.16 invitationu cevaplama kısmına ilişkin          
    return render(request, "player/home.html", 
                {'active_games':active_games,
                'finished_games':finished_games,
                'invitations':invitations})            # home için urls den yapılan istek için player/home.html i gönder. # Game in içindeki oyunu say. 8.16 dan sonra buaraya invitations kısmını ilave ettik.  


@login_required()                                                  # 8.8. forms buraya ilave olarak 8.12 olarak işaretli kodlar eklendi. 
def new_invitation(request):
    if request.method == "POST":                                       # eklenen
        invitation = Invitation(from_user=request.user)                # 8.15 bir önceki maddede eklenen kütüphanedki hata için yazıldı. 
        form = InvitationForm(instance=invitation, data=request.POST)  # eklenen , instance kısmı 8.15 den sonra ilave edild.
        if form.is_valid():                                            # sonradan eklenen
            form.save()                                                # sonradan eklenen
            return redirect('player_home')                             # sonradan eklenen, kütüphaneyi de ekle yukarıya
    else:                                                              # eklenen
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})


@login_required()                                                    # 8.17
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user,
            )
        invitation.delete()
        return redirect('game')                                         
    else:
        return render(request,"player/accept_invitation_form.html",{'invitation':invitation})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "player/signup_form.html"
    success_url = reverse_lazy('player_home')