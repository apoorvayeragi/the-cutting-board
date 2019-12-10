# Generated by Django 2.2.7 on 2019-11-25 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient_name',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient_quantity',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='measurement_choice',
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=50)),
                ('measurement_choice', models.CharField(choices=[('pound', 'pound'), ('whole', 'whole'), ('tea spoon', 'tea spoon'), ('table spoon', 'table spoon'), ('liter', 'liter'), ('cup', 'cup')], default='whole', max_length=10)),
                ('ingredient_quantity', models.IntegerField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrecipe.Recipe')),
            ],
        ),
    ]