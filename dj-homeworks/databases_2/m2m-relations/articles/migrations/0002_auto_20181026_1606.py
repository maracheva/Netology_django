# Generated by Django 2.1.1 on 2018-10-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScopeShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
            ],
            options={
                'verbose_name': 'Тематика статьи',
                'verbose_name_plural': 'Тематика статьи',
                'ordering': ['scope'],
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=25, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['topic'],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['title'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='articlescopeship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='articlescopeship',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Scope'),
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.ArticleScopeShip', to='articles.Scope'),
        ),
    ]