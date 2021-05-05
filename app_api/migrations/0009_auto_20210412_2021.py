# Generated by Django 3.1.2 on 2021-04-12 20:21

from django.db import migrations, models
import django.db.models.deletion
import tyadmin_api_cli.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0008_auto_20210406_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_key', models.CharField(default='other', max_length=50, unique=True, verbose_name='赛道唯一标识')),
                ('track_name', models.CharField(default='其他', max_length=50, unique=True, verbose_name='赛道名称')),
            ],
            options={
                'verbose_name': '赛道',
                'verbose_name_plural': '赛道',
            },
        ),
        migrations.RemoveField(
            model_name='judge',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='judge',
            name='introduction',
        ),
        migrations.AddField(
            model_name='judge',
            name='mail',
            field=models.EmailField(default='cuiyuhui123@qq.com', max_length=255, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='avatar',
            field=tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='org_avatar', verbose_name='机构图标240x80px'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='orgtype',
            field=models.CharField(choices=[('director', '指导单位'), ('sponsor', '主办单位'), ('agency', '银牌金牌'), ('donator', '金牌赞助'), ('strategy', '战略合作单位'), ('supporter', '支持单位'), ('auxorg', '协办单位—机构组织'), ('auxuniv', '协办单位—各高校研会'), ('auxaux', '协办单位—各高校创协')], default='sponsor', max_length=255, verbose_name='机构类型'),
        ),
        migrations.AlterField(
            model_name='vipguest',
            name='avatar',
            field=tyadmin_api_cli.fields.SImageField(max_length=255, upload_to='vipguest_avatar', verbose_name='嘉宾头像210x280px'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, verbose_name='项目名称')),
                ('project_group_type', models.CharField(choices=[('creative', '创意组'), ('startup', '初创组')], max_length=255, verbose_name='项目组别')),
                ('project_leader_name', models.CharField(max_length=255, verbose_name='领队姓名')),
                ('project_phone', models.CharField(max_length=255, verbose_name='联系电话')),
                ('project_introduction', models.TextField(verbose_name='项目简介')),
                ('project_track', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_api.track', verbose_name='项目赛道')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.AddField(
            model_name='judge',
            name='track',
            field=models.ManyToManyField(blank=True, to='app_api.Track', verbose_name='赛道'),
        ),
    ]