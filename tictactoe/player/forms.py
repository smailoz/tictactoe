from django.forms import ModelForm          # 8.7 invitation için model oluşturduktan sonra önce forms.py doayası oluşturuyor ve bu kodları yazıyoruz. 

from .models import Invitation


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ('from_user', 'timestamp')