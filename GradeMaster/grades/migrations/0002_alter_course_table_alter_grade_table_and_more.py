# Generated by Django 4.2.7 on 2023-11-04 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='Course_Table',
        ),
        migrations.AlterModelTable(
            name='grade',
            table='Grade_Table',
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student_Table',
        ),
    ]
