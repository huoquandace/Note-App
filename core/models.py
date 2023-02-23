from django.db import models
from django.contrib.auth import get_user_model
from  django.utils.translation import gettext_lazy as _

class Note(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notes')
    headline = models.CharField(_('headline'), max_length=255)
    content = models.TextField(_('content'), blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.headline}'
