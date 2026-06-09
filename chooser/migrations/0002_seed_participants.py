from django.db import migrations

PARTICIPANT_NAMES = [
    "Elder",
    "Gilbert",
    "Roben",
    "Belise",
    "Divine",
    "Amina",
    "Yvan",
    "Confianceee",
    "Arosdanton",
    "Kagame",
    "Arsene",
    "Byusa",
    "Bishop",
]


def create_participants(apps, schema_editor):
    Participant = apps.get_model("chooser", "Participant")
    for name in PARTICIPANT_NAMES:
        Participant.objects.get_or_create(name=name)


def reverse_participants(apps, schema_editor):
    Participant = apps.get_model("chooser", "Participant")
    Participant.objects.filter(name__in=PARTICIPANT_NAMES).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("chooser", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_participants, reverse_participants),
    ]
