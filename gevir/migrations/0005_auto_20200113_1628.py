# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-13 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gevir', '0004_auto_20181220_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='geneidentifier',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genescore',
            name='gevir_and_oe_lof_ad_enrichment',
            field=models.FloatField(verbose_name='VIRLoF AD'),
        ),
        migrations.AlterField(
            model_name='genescore',
            name='gevir_and_oe_lof_ar_enrichment',
            field=models.FloatField(verbose_name='VIRLoF AR'),
        ),
        migrations.AlterField(
            model_name='genescore',
            name='gevir_and_oe_lof_percentile',
            field=models.FloatField(verbose_name='VIRLoF %'),
        ),
        migrations.AlterField(
            model_name='genescore',
            name='oe_lof_ad_enrichment',
            field=models.FloatField(verbose_name='LOEUF AD'),
        ),
        migrations.AlterField(
            model_name='genescore',
            name='oe_lof_ar_enrichment',
            field=models.FloatField(verbose_name='LOEUF AR'),
        ),
        migrations.AlterField(
            model_name='genescore',
            name='oe_lof_percentile',
            field=models.FloatField(verbose_name='LOEUF %'),
        ),
    ]