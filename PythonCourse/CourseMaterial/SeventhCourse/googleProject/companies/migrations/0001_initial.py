# Generated by Django 3.0.7 on 2020-06-18 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('S.R.L', 'S.R.L.'), ('S.A.', 'S.A.')], max_length=10)),
                ('active', models.CharField(max_length=2)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location')),
            ],
        ),
    ]
