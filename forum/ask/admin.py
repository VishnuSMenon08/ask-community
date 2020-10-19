from django.contrib import admin
from ask.models import Profile,Question,Poll,Answer,Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Answer)
admin.site.register(Comment)

