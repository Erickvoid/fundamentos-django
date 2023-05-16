# Generated by Django 3.2.6 on 2023-05-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('R', 'Reviewed'), ('N', 'Not Reviewed'), ('E', 'Error'), ('A', 'Acepted')], default='R', max_length=1),
            preserve_default=False,
        ),
    ]
