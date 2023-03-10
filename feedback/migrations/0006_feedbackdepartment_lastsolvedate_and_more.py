# Generated by Django 4.1.1 on 2023-02-11 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_remove_feedbackdepartment_feedbackopendate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdepartment',
            name='LastSolveDate',
            field=models.CharField(default='', max_length=100, verbose_name='Talep ve Şikayetin Yanıtı İçin Gerekli Zaman(Gün)'),
        ),
        migrations.AlterField(
            model_name='feedbackdepartment',
            name='DurationTime',
            field=models.CharField(blank=True, max_length=100, verbose_name='Geçen Süre'),
        ),
        migrations.AlterField(
            model_name='feedbackdepartment',
            name='FeedbackClosedDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Talep-Şikayet Son İşlem Saati'),
        ),
        migrations.AlterField(
            model_name='feedbackdepartment',
            name='IdFeedbackPriorityLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.feedbackprioritylevel', verbose_name='Talep-Şikayet Öncelik Seviyesi'),
        ),
    ]
