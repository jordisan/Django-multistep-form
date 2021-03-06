# Generated by Django 3.0.6 on 2020-06-12 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='general.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
