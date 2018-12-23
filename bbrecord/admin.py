from django.contrib import admin
from .models import User, Game, Playerstats


admin.site.register(User)
admin.site.register(Game)
admin.site.register(Playerstats)