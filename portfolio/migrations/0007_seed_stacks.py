from django.db import migrations


def seed_stacks(apps, schema_editor):
    Stack = apps.get_model('portfolio', 'Stack')
    for nom in ('Django', 'React Native'):
        Stack.objects.get_or_create(nom=nom)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_stack_alter_project_options_remove_project_categorie_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_stacks, noop),
    ]
