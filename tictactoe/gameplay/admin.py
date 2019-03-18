from django.contrib import admin

from .models import Game, Move

@admin.register(Game)                                      # buraya normalde admin.site.register(Game) yazdığımızda Games 
class GameAdmin(admin.ModelAdmin):                         # ekranında tek sütunun altında maç yapacak kişileri görüyoruz.
    list_display = ('id', 'first_player', 'second_player', 'status')  # bu durumda listede belirtilen sütunlara böldük.
    list_editable = ('status',)                             # sondaki virgül olmayınca hata veriyor. 


admin.site.register(Move)