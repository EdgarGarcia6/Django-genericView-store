# Generated by Django 4.0.4 on 2022-05-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_examen_parcial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('banda', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('imagen', models.FileField(null=True, upload_to='canciones/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('casa_productora', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.FileField(null=True, upload_to='peliculas/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('casa_productora', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.FileField(null=True, upload_to='series/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('casa_desarrolladora', models.CharField(max_length=100)),
                ('imagen', models.FileField(null=True, upload_to='videojuegos/', verbose_name='')),
            ],
        ),
        migrations.RemoveField(
            model_name='libros',
            name='nombre',
        ),
        migrations.AddField(
            model_name='libros',
            name='autor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='libros',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='libros',
            name='titulo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='libros',
            name='imagen',
            field=models.FileField(null=True, upload_to='libros/', verbose_name=''),
        ),
    ]