# Generated by Django 4.0.2 on 2022-02-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customervehicles',
            name='kind',
            field=models.IntegerField(choices=[(1, 'Carro'), (2, 'Moto')], null=True),
        ),
    ]