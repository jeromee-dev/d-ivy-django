# Generated by Django 5.0.3 on 2024-03-19 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
