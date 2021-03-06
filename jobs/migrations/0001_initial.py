# Generated by Django 2.0.9 on 2018-12-18 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('data',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=50)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.Data')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
