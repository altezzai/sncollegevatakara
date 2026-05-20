from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_campuslifepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusLifeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='campus_life/members/')),
                ('is_active', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='myapp.campuslifepage')),
            ],
            options={
                'ordering': ['sort_order', 'name', 'id'],
            },
        ),
    ]