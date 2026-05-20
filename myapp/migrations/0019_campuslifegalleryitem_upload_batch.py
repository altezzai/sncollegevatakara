import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_campuslifegalleryitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='campuslifegalleryitem',
            name='upload_batch',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]