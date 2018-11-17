from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# def view_user_id(request):
#     current_user = request.user
#     html = "<html><body>User: %s.</body></html>" % current_user.id
#     return HttpResponse(html)




# def MQTT_Connection(request):
#     current_user = request.user
#     prefix_message = "Follow_Band_" + str(current_user)
#     new_localization = Localization







# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'ID')
#     list_select_related = ('profile', )

#     def get_id(self, instance):
#         return instance.profile.ID
#     get_id.short_description = 'ID'


