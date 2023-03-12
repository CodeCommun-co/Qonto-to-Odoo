# Generated by Django 4.1.7 on 2023-03-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiqo_parser', '0019_odoocontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='odoocontact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='odoocontact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='odoocontact',
            name='id_odoo',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]