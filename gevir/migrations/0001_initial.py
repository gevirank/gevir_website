# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-10 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_identifier_upper', models.CharField(max_length=128)),
                ('canonical_transcript', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GeneScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_name', models.CharField(max_length=128, verbose_name='Gene Name')),
                ('canonical_transcript', models.CharField(max_length=20, unique=True, verbose_name='Canonical Transcript')),
                ('gevir_percentile', models.FloatField(verbose_name='GeVIR %')),
                ('oe_lof_percentile', models.FloatField(verbose_name='LoF %')),
                ('gevir_and_oe_lof_percentile', models.FloatField(verbose_name='GeVIR+LoF %')),
                ('gevir_ad_enrichment', models.FloatField(verbose_name='GeVIR AD')),
                ('oe_lof_ad_enrichment', models.FloatField(verbose_name='LoF AD')),
                ('gevir_and_oe_lof_ad_enrichment', models.FloatField(verbose_name='GeVIR+LoF AD')),
                ('gevir_ar_enrichment', models.FloatField(verbose_name='GeVIR AR')),
                ('oe_lof_ar_enrichment', models.FloatField(verbose_name='LoF AR')),
                ('gevir_and_oe_lof_ar_enrichment', models.FloatField(verbose_name='GeVIR+LoF AR')),
                ('gevir_ad_p', models.FloatField()),
                ('oe_lof_ad_p', models.FloatField()),
                ('gevir_and_oe_lof_ad_p', models.FloatField()),
                ('gevir_ar_p', models.FloatField()),
                ('oe_lof_ar_p', models.FloatField()),
                ('gevir_and_oe_lof_ar_p', models.FloatField()),
            ],
        ),
    ]