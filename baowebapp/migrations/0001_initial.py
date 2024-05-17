# Generated by Django 5.0.6 on 2024-05-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("student_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50, null=True)),
                ("gender", models.IntegerField(null=True)),
                ("school", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
