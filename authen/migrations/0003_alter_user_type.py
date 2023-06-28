# Generated by Django 4.2.2 on 2023-06-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authen", "0002_rename_fullname_user_full_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="type",
            field=models.CharField(
                choices=[(0, "student"), (1, "teacher")], default=0, max_length=9
            ),
        ),
    ]
