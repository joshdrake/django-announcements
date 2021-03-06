from django.contrib import admin

from announcements.models import Announcement
from announcements.forms import AnnouncementAdminForm


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "creation_date", "expiration_date", "start_date", "members_only", "is_dismissable")
    list_filter = ("members_only",)
    form = AnnouncementAdminForm
    fieldsets = [
        (None, {
            "fields": ["title", "content", "site_wide", "members_only", "start_date", "expiration_date", "is_dismissable"],
        }),
        
        ("Manage announcement", {
            "fields": ["send_now"],
        }),
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            # When creating a new announcement, set the creator field.
            obj.creator = request.user
        obj.save()


admin.site.register(Announcement, AnnouncementAdmin)
