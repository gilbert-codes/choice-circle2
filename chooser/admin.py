from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "has_chosen", "chosen_target", "selected_by_person")
    readonly_fields = ("selected_by_person",)

    def selected_by_person(self, obj):
        return obj.selected_by_person
    selected_by_person.short_description = "Selected by"
