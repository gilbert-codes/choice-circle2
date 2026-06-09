from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ParticipantChoiceForm
from .models import Participant


def home(request):
    form = ParticipantChoiceForm(request.POST or None)
    chosen_count = Participant.objects.filter(chosen_target__isnull=False).count()
    total_count = Participant.objects.count()

    if request.method == "POST" and form.is_valid():
        participant = form.cleaned_data["username"]
        return redirect("choose", participant_id=participant.pk)

    return render(request, "chooser/home.html", {
        "form": form,
        "chosen_count": chosen_count,
        "total_count": total_count,
    })


@require_http_methods(["GET", "POST"])
def choose(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if participant.has_chosen:
        return redirect("result", participant_id=participant.pk)

    if request.method == "POST":
        target = participant.assign_random_target()
        if target:
            return redirect("result", participant_id=participant.pk)
        return render(request, "chooser/result.html", {
            "participant": participant,
            "failed": True,
        })

    return render(request, "chooser/choose.html", {
        "participant": participant,
        "remaining_targets": participant.available_targets().count(),
    })


def result(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if not participant.has_chosen:
        return redirect("choose", participant_id=participant.pk)

    return render(request, "chooser/result.html", {
        "participant": participant,
        "target": participant.chosen_target,
        "selected_by": participant.selected_by_person,
    })


@login_required(login_url='/admin/login/')
def admin_dashboard(request):
    participants = Participant.objects.order_by("name")
    chosen = participants.filter(chosen_target__isnull=False)
    waiting = participants.filter(chosen_target__isnull=True)
    return render(request, "chooser/admin_dashboard.html", {
        "participants": participants,
        "chosen": chosen,
        "waiting": waiting,
    })


@login_required(login_url='/admin/login/')
@require_http_methods(["POST"])
def reset_participant_choice(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if participant.has_chosen:
        participant.chosen_target = None
        participant.save()
        messages.success(request, f"{participant.name}'s choice has been reset.")
    else:
        messages.info(request, f"{participant.name} has no choice to reset.")
    return redirect(reverse("admin_dashboard"))
