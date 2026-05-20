from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_campuslifemember'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusLifeGalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('image', 'Photo'), ('video', 'Video')], default='image', max_length=16)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='campus_life/gallery/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='campus_life/gallery/')),
                ('video_url', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_items', to='myapp.campuslifepage')),
            ],
            options={
                'ordering': ['-created_at', '-id'],
            },
        ),
    ]