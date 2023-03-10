# Generated by Django 4.1.7 on 2023-03-14 10:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tiqo_parser', '0028_transaction_vat_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAccount',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('id_odoo', models.SmallIntegerField()),
            ],
        ),
    ]
