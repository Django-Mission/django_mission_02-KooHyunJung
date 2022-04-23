# Generated by Django 4.0.1 on 2022-04-23 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0003_remove_inquiry_updated_by_id_inquiry_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(verbose_name='답변 내용'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='inquiry_id',
            field=models.ForeignKey(db_column='inquiry_id', on_delete=django.db.models.deletion.CASCADE, to='support.inquiry', verbose_name='참조 문의글'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_by_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='답변 작성자'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='category',
            field=models.CharField(choices=[('NR', '일반'), ('AC', '계정'), ('Et', '기타')], max_length=2, verbose_name='문의 카테고리'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_by_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='질문 작성자'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=128, verbose_name='작성자 이메일'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='작성자 전화번호'),
        ),
    ]
