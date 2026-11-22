from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='hashed_password',
            field=models.CharField(
                default='',
                max_length=200,
                verbose_name='Password'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='refresh_token',
            field=models.CharField(
                default='',
                max_length=200,
                verbose_name='Refresh Token'
            ),
            preserve_default=False,
        ),
    ]
