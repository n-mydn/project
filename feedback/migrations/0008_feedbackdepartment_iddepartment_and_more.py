# Generated by Django 4.1.1 on 2023-02-14 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_feedbackdepartment_feedbackstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdepartment',
            name='IdDepartment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feedback.department', verbose_name='Talep-Şikayet Departmanı'),
        ),
        migrations.AlterField(
            model_name='feedbackdepartment',
            name='FeedbackStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.feedbackstatus', verbose_name='Talep-Şikayet Durumu'),
        ),
    ]
