# Generated by Django 4.1.1 on 2023-02-01 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.DateTimeField(auto_now_add=True)),
                ('history_note', models.TextField()),
                ('history_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='history_file')),
                ('history_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.department', verbose_name='history_department')),
                ('history_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.feedback', verbose_name='history_feedback')),
                ('history_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.feedbacksource', verbose_name='history_status')),
                ('history_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='histroy_user')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Açık', 'Açık'), ('İşlemde', 'İşlemde'), ('Çözüldü', 'çözüldü')], max_length=7, verbose_name='f_status_name')),
                ('IdCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.company', verbose_name='status_ıdcompany')),
            ],
        ),
    ]
