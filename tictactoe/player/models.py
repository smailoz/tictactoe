from django.db import models

from django.contrib.auth.models import User  


class Invitation(models.Model):                                              # 8.6. İnvitation oluşturma ilk adım. 8.20 de değiştirdik burasını
    from_user = models.ForeignKey(User, related_name="invitations_send", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, 
        related_name="invitation_received",
        verbose_name="User to invite",
        help_text="Please select the user you want to play a game with", 
        on_delete=models.CASCADE
    )
    message = models.CharField(
        max_length=300, blank=True,
        verbose_name="Optional Message",
        help_text="It's always nice to add a friendly message!")                # buarada timestampi kaldırdık. Böylece makemigrations apmamız gerekt.
    

