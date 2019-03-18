from django.shortcuts  import render, redirect                    # 8.1

def welcome(request):
    if request.user.is_authenticated:                             # 8.1 Authenticated yetkilendirme için ilk olarak view de yönlendirme yaparız. 
        return redirect('player_home')                            # 8.1
    else:                                                         # 8.1
        return render(request, 'tictactoe/welcome.html')