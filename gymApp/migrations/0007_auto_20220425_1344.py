# Generated by Django 2.0.7 on 2022-04-25 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0006_auto_20220425_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instructor_name', models.CharField(max_length=30)),
                ('Instructor_email', models.CharField(max_length=30)),
                ('Instructor_phone', models.IntegerField(default=0)),
                ('Instructor_age', models.IntegerField()),
                ('Instructor_photo', models.CharField(max_length=100)),
                ('Instructor_specialty', models.CharField(max_length=100)),
                ('Instructor_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='class',
            name='Class_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymApp.Instructor'),
        ),
    ]
