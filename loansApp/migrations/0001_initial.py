# Generated by Django 2.0.5 on 2018-06-28 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spacesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date_time', models.DateTimeField()),
                ('ending_date_time', models.DateTimeField()),
                ('state', models.CharField(choices=[('A', 'Aceptado'), ('R', 'Rechazado'), ('P', 'Pendiente')], default='P', max_length=1, verbose_name='Estado')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articlesApp.Article')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
