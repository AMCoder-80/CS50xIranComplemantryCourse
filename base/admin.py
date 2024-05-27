from django.contrib import admin
from base.models import User, Profile, WorkoutGif, Client, Exercise

# Register your models here.


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(WorkoutGif)
admin.site.register(Client)
admin.site.register(Exercise)