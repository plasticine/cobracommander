# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Build'
        db.create_table('build_build', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('project_name_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='a', max_length=1, blank=True)),
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('duration_ms', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('log', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('build', ['Build'])

        # Adding model 'Step'
        db.create_table('build_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('build', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['build.Build'])),
            ('type', self.gf('django.db.models.fields.CharField')(default='b', max_length=1, blank=True)),
            ('sha', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('log', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='a', max_length=1, blank=True)),
        ))
        db.send_create_signal('build', ['Step'])


    def backwards(self, orm):
        
        # Deleting model 'Build'
        db.delete_table('build_build')

        # Deleting model 'Step'
        db.delete_table('build_step')


    models = {
        'build.build': {
            'Meta': {'ordering': "['-created_datetime']", 'object_name': 'Build'},
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'duration_ms': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'project_name_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '1', 'blank': 'True'})
        },
        'build.step': {
            'Meta': {'ordering': "['created_datetime']", 'object_name': 'Step'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['build.Build']"}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sha': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '1', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'b'", 'max_length': '1', 'blank': 'True'})
        },
        'project.project': {
            'Meta': {'object_name': 'Project'},
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'targets': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['target.Target']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'target.target': {
            'Meta': {'object_name': 'Target'},
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'builds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['build.Build']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['build']
