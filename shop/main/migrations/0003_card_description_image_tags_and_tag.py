from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(default='', upload_to='cards/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(to='main.tag'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='', upload_to='users/'),
            preserve_default=False,
        ),
    ]
