from django.contrib import admin
from .models import Team, Player, Statistic, Division, Club, News

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Statistic)
admin.site.register(Division)
admin.site.register(Club)
admin.site.register(News)
