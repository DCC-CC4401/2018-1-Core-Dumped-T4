# Generated by Django 2.0.4 on 2018-08-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loansApp', '0002_loan_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='state',
            field=models.CharField(choices=[('V', 'Vigente'), ('C', 'Caducado'), ('E', 'Recibido'), ('L', 'Perdido')], default='V', max_length=1, verbose_name='Estado'),
        ),
    ]
