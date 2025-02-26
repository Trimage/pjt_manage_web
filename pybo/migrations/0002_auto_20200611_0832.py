# Generated by Django 3.0.7 on 2020-06-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference_attender',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='conference_attender',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='conference_content',
            name='detail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='conference_info',
            name='reference',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='project_company',
            name='construct',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project_company',
            name='execute',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project_company',
            name='plan',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project_company',
            name='subcontract',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='earth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='scale_depth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='scale_length',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='scale_width',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='shape',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='steel',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_construct',
            name='tm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_cost',
            name='real',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='project_cost',
            name='total',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
