# Generated by Django 2.2.7 on 2019-11-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipe', '0003_auto_20191124_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='measurement_choice',
            field=models.CharField(choices=[('pound', 'pound'), ('whole', 'whole'), ('tea spoon', 'tea spoon'), ('table spoon', 'table spoon'), ('liter', 'liter'), ('cup', 'cup')], default='whole', max_length=20),
        ),
    ]
