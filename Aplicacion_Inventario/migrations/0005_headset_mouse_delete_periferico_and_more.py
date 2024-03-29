# Generated by Django 5.0.2 on 2024-03-03 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion_Inventario', '0004_computadora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_headset', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_mouse', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Periferico',
        ),
        migrations.AlterModelOptions(
            name='campania',
            options={'ordering': ['nombre_campania'], 'verbose_name': 'Campania', 'verbose_name_plural': 'Campañas'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['nombre_persona', 'apellido_persona']},
        ),
        migrations.RemoveField(
            model_name='persona',
            name='auricular_asignado',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='contraseña_preferida_usuario',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='mouse_asignado',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='teclado_asignado',
        ),
        migrations.AddField(
            model_name='computadora',
            name='estado_computadora_escritorio',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computadora',
            name='version_windows',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notebook',
            name='estado_notebook',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='id_campania',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_Inventario.campania'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='id_computadora_escritorio',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_Inventario.computadora'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='id_notebook',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_Inventario.notebook'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campania',
            name='nombre_campania',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='nombre_computadora',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='marca_notebook',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='modelo_notebook',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='nombre_notebook',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='numero_serie_notebook',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido_persona',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cuit_persona',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre_persona',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='persona',
            name='id_headset',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_Inventario.headset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='id_mouse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_Inventario.mouse'),
            preserve_default=False,
        ),
    ]
