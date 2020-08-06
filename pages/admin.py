from django.contrib import admin
from pages.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email', 'telephone', 'message',]
    list_display_links =[ 'name', 'email', 'telephone', 'message',]
    search_fields = [ 'name', 'email', 'telephone', 'message',]

admin.site.register(Feedback, FeedbackAdmin)
