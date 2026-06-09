import random
from functools import lru_cache
from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=64, unique=True)
    chosen_target = models.OneToOneField(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="selected_by",
    )

    def __str__(self):
        return self.name

    @property
    def has_chosen(self):
        return self.chosen_target_id is not None

    @property
    def selected_by_person(self):
        try:
            return self.selected_by
        except Participant.DoesNotExist:
            return None

    def available_targets(self):
        taken_ids = Participant.objects.filter(chosen_target__isnull=False).values_list("chosen_target_id", flat=True)
        return Participant.objects.exclude(pk=self.pk).exclude(pk__in=taken_ids)

    def assign_random_target(self):
        if self.has_chosen:
            return self.chosen_target

        available = list(self.available_targets())
        random.shuffle(available)
        assigned = {p.pk: p.chosen_target_id for p in Participant.objects.filter(chosen_target__isnull=False)}
        remaining_choosers = list(Participant.objects.filter(chosen_target__isnull=True).exclude(pk=self.pk))

        def can_complete(choosers, targets):
            if not choosers:
                return True
            chooser = choosers[0]
            for target in targets:
                if target.pk == chooser.pk:
                    continue
                next_targets = [t for t in targets if t.pk != target.pk]
                if can_complete(choosers[1:], next_targets):
                    return True
            return False

        for target in available:
            remaining_targets = [p for p in Participant.objects.exclude(pk__in=assigned.values()).exclude(pk=target.pk)]
            if can_complete(remaining_choosers, remaining_targets):
                self.chosen_target = target
                self.save()
                return target
        return None
