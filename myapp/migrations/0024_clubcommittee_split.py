from django.db import migrations, models
import django.db.models.deletion


def migrate_club_committee_items(apps, schema_editor):
    ClubCommittee = apps.get_model('myapp', 'ClubCommittee')
    ClubCommitteePerson = apps.get_model('myapp', 'ClubCommitteePerson')
    ClubCommitteeItem = apps.get_model('myapp', 'ClubCommitteeItem')

    for item in ClubCommitteeItem.objects.all().iterator():
        club, created = ClubCommittee.objects.get_or_create(
            page_id=item.page_id,
            name=item.name,
            defaults={
                'description': item.description,
                'is_active': item.is_active,
                'created_at': item.created_at,
            },
        )
        if not created:
            updated = False
            if not club.description and item.description:
                club.description = item.description
                updated = True
            if item.is_active and not club.is_active:
                club.is_active = True
                updated = True
            if updated:
                club.save()

        ClubCommitteePerson.objects.create(
            club_id=club.id,
            name=item.person_name,
            position=item.person_position,
            photo=item.person_photo,
            is_active=item.is_active,
            created_at=item.created_at,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_programmesyllabuscourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clubs', to='myapp.campuslifepage')),
            ],
            options={
                'ordering': ['name', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ClubCommitteePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('position', models.CharField(max_length=180)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='campus_life/clubs/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='myapp.clubcommittee')),
            ],
            options={
                'ordering': ['name', 'id'],
            },
        ),
        migrations.RunPython(migrate_club_committee_items, reverse_code=migrations.RunPython.noop),
        migrations.DeleteModel(
            name='ClubCommitteeItem',
        ),
    ]
