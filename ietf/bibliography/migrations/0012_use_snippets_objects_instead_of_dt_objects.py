# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-02-13 23:00
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.contenttypes.models import ContentType

def forward(apps, schema_editor):
    BibliographyItem = apps.get_model('bibliography','BibliographyItem')

    DtRFC = apps.get_model('datatracker', 'RFC')
    SnippetsRFC = apps.get_model('snippets', 'RFC')

    DtCharter = apps.get_model('datatracker', 'Charter')
    SnippetsCharter = apps.get_model('snippets', 'Charter')

    source_type = ContentType.objects.get_for_model(DtRFC, for_concrete_model = False)
    target_type = ContentType.objects.get_for_model(SnippetsRFC, for_concrete_model = False)

    for item in BibliographyItem.objects.filter(content_type_id=source_type.pk):
        dt_rfc = DtRFC.objects.get(pk = item.object_id)
        item.content_type_id = target_type.pk
        item.object_id = SnippetsRFC.objects.get(rfc=dt_rfc.rfc).pk
        item.save()

    source_type = ContentType.objects.get_for_model(DtCharter, for_concrete_model = False)
    target_type = ContentType.objects.get_for_model(SnippetsCharter, for_concrete_model = False)
    for item in BibliographyItem.objects.filter(content_type_id=source_type.pk):
        dt_charter = DtCharter.objects.get(pk = item.object_id)
        item.content_type_id = target_type.pk
        item.object_id = SnippetsCharter.objects.get(name=dt_charter.name).pk
        item.save()

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0011_bibliographyitem_content_long_title'),
        ('datatracker','0026_auto_20180202_1623'),
        ('snippets','0037_populate_snippets_from_dt'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]