# Generated by Django 4.1.7 on 2023-03-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiqo_parser', '0021_rename_contact_qontocontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='initiator_id',
            new_name='initiator',
        ),
    ]
