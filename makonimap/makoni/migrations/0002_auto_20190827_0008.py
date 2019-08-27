# Generated by Django 2.1.7 on 2019-08-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makoni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(choices=[('PE', 'Pernambuco'), ('PB', 'Paraíba'), ('CE', 'Ceará'), ('SP', 'São Paulo'), ('SE', 'SERGIPE'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RN', 'Rio Grande do Norte'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('DF', 'Distrito Federal'), ('ES', 'Espirito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PR', 'Paraná'), ('PI', 'Piaui'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('TO', 'Tocantins')], max_length=25),
        ),
    ]
