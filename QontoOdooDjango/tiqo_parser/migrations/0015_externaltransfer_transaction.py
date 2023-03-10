# Generated by Django 4.1.7 on 2023-03-10 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiqo_parser', '0014_externaltransfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='externaltransfer',
            name='transaction',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='external_transfer', to='tiqo_parser.transaction'),
            preserve_default=False,
        ),
    ]
