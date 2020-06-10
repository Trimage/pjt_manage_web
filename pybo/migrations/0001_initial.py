# Generated by Django 3.0.7 on 2020-06-10 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('reference', models.BinaryField()),
                ('place', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('cf_start', models.TimeField()),
                ('cf_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('num', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive', models.DateField()),
                ('contract', models.DateField()),
                ('delivery', models.DateField()),
                ('pjt_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Project_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real', models.DecimalField(decimal_places=3, max_digits=6)),
                ('total', models.DecimalField(decimal_places=3, max_digits=6)),
                ('real_expect', models.BooleanField()),
                ('total_expect', models.BooleanField()),
                ('pjt_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Project_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Construct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=10)),
                ('scale_width', models.IntegerField()),
                ('scale_length', models.IntegerField()),
                ('scale_depth', models.IntegerField()),
                ('tm', models.IntegerField()),
                ('steel', models.IntegerField()),
                ('earth', models.IntegerField()),
                ('scale_expect', models.BooleanField()),
                ('tm_expect', models.BooleanField()),
                ('steel_expect', models.BooleanField()),
                ('earth_expect', models.BooleanField()),
                ('pjt_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Project_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execute', models.CharField(max_length=30)),
                ('construct', models.CharField(max_length=30)),
                ('subcontract', models.CharField(max_length=30)),
                ('plan', models.CharField(max_length=30)),
                ('execute_expect', models.BooleanField()),
                ('construct_expect', models.BooleanField()),
                ('subcontract_expect', models.BooleanField()),
                ('plan_expect', models.BooleanField()),
                ('pjt_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Project_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Conference_Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('cfr_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Conference_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Conference_Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('writer', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('cfr_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Conference_Info')),
            ],
        ),
        migrations.AddField(
            model_name='conference_info',
            name='pjt_idx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Project_Info'),
        ),
        migrations.CreateModel(
            name='Conference_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('cfr_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Conference_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Conference_Attender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility', models.CharField(max_length=20)),
                ('agency', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('cfr_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Conference_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Conference_Approve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('cfr_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Conference_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Conference_Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('writer', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('point_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Conference_Point')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Question')),
            ],
        ),
    ]
