from django.db import migrations, models


def seed_campus_life_pages(apps, schema_editor):
    CampusLifePage = apps.get_model('myapp', 'CampusLifePage')

    defaults = [
        ("PTA", "pta", 10),
        ("NSS", "nss", 20),
        ("Placement Cell", "placement-cell", 30),
        ("COK", "cok", 40),
        ("Examination Committee", "examination-committee", 50),
        ("Scholarships", "scholarships", 60),
        ("Other Clubs / Committees", "other-clubs-committees", 70),
    ]

    for title, slug, sort_order in defaults:
        CampusLifePage.objects.get_or_create(
            slug=slug,
            defaults={
                "title": title,
                "sort_order": sort_order,
                "is_published": True,
                "content": "",
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_galleryitem_file_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusLifePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('content', models.TextField(blank=True)),
                ('hero_image', models.ImageField(blank=True, null=True, upload_to='campus_life/')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='campus_life/')),
                ('is_published', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['sort_order', 'title', 'id'],
            },
        ),
        migrations.RunPython(seed_campus_life_pages, migrations.RunPython.noop),
    ]
