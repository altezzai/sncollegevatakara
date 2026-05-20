from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_campuslifegalleryitem_upload_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='campus_life/scholarships/')),
                ('description', models.TextField(blank=True)),
                ('link_url', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scholarship_items', to='myapp.campuslifepage')),
            ],
            options={
                'ordering': ['-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='ClubCommitteeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('person_name', models.CharField(max_length=180)),
                ('person_position', models.CharField(max_length=180)),
                ('person_photo', models.ImageField(blank=True, null=True, upload_to='campus_life/clubs/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_committee_items', to='myapp.campuslifepage')),
            ],
            options={
                'ordering': ['-created_at', '-id'],
            },
        ),
    ]