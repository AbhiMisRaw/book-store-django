# Generated by Django 5.0 on 2023-12-20 19:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Contributor's first name", max_length=50)),
                ('last_name', models.CharField(help_text="Contributor's last name", max_length=50)),
                ('email', models.EmailField(help_text='Contact email for Contributor', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title Of the Book', max_length=70)),
                ('publication_date', models.DateField(verbose_name='Date the Book was published')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN number of the book')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='BookContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co_Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='The role this contributor had in the book')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.book')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.contributor')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(through='Reviews.BookContributor', to='Reviews.contributor'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='The Review text')),
                ('rating', models.IntegerField(help_text='The rating reviewer has given')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The data and time the review was created')),
                ('date_edited', models.DateTimeField(help_text='Last edited', null=True)),
                ('book', models.ForeignKey(help_text='Book that this review is for', on_delete=django.db.models.deletion.CASCADE, to='Reviews.book')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
