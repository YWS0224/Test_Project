# Generated by Django 2.1.4 on 2018-12-30 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodName', models.CharField(max_length=30)),
                ('goodNum', models.IntegerField()),
                ('goodPrice', models.FloatField()),
                ('goodType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='type.goodsType')),
            ],
        ),
    ]
