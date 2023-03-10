# Generated by Django 4.1.6 on 2023-02-04 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_location', models.CharField(max_length=150, verbose_name='Локация покупки')),
                ('owner_FIO', models.CharField(max_length=150, verbose_name='ФИО владельца')),
            ],
        ),
        migrations.CreateModel(
            name='CarPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('plate_number', models.CharField(max_length=150, verbose_name='Номерной знак')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OwnerTravelPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=250, verbose_name='ФИО')),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataOfPassingCar',
            fields=[
                ('numberHistory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.carpass')),
                ('speed', models.FloatField()),
                ('driverFIO', models.CharField(max_length=250, verbose_name='Фио водителя')),
            ],
        ),
        migrations.CreateModel(
            name='TravelPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('main_owner_id', models.ManyToManyField(to='main.ownertravelpoint')),
            ],
        ),
        migrations.AddField(
            model_name='carpass',
            name='travel_point_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.travelpoint'),
        ),
        migrations.AddField(
            model_name='car',
            name='model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cartype'),
        ),
    ]
