# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'mediacat_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('file_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('alt_text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'mediacat', ['Image'])

        # Adding model 'ImageAssociation'
        db.create_table(u'mediacat_imageassociation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='associations', to=orm['mediacat.Image'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mediacat', ['ImageAssociation'])

        # Adding model 'ImageCrop'
        db.create_table(u'mediacat_imagecrop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='crops', to=orm['mediacat.Image'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('score', self.gf('django.db.models.fields.SmallIntegerField')(default=40)),
            ('scale', self.gf('django.db.models.fields.SmallIntegerField')(default=2)),
            ('x1', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('y1', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('x2', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('y2', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mediacat', ['ImageCrop'])

        # Adding unique constraint on 'ImageCrop', fields ['image', 'width', 'height']
        db.create_unique(u'mediacat_imagecrop', ['image_id', 'width', 'height'])

        # Adding model 'ImageCropApplication'
        db.create_table(u'mediacat_imagecropapplication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crop', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applications', to=orm['mediacat.ImageCrop'])),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mediacat', ['ImageCropApplication'])


    def backwards(self, orm):
        # Removing unique constraint on 'ImageCrop', fields ['image', 'width', 'height']
        db.delete_unique(u'mediacat_imagecrop', ['image_id', 'width', 'height'])

        # Deleting model 'Image'
        db.delete_table(u'mediacat_image')

        # Deleting model 'ImageAssociation'
        db.delete_table(u'mediacat_imageassociation')

        # Deleting model 'ImageCrop'
        db.delete_table(u'mediacat_imagecrop')

        # Deleting model 'ImageCropApplication'
        db.delete_table(u'mediacat_imagecropapplication')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mediacat.image': {
            'Meta': {'object_name': 'Image'},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mediacat.imageassociation': {
            'Meta': {'object_name': 'ImageAssociation'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'associations'", 'to': u"orm['mediacat.Image']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mediacat.imagecrop': {
            'Meta': {'unique_together': "(('image', 'width', 'height'),)", 'object_name': 'ImageCrop'},
            'height': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'crops'", 'to': u"orm['mediacat.Image']"}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'scale': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'score': ('django.db.models.fields.SmallIntegerField', [], {'default': '40'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {}),
            'x1': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'x2': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'y1': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'y2': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mediacat.imagecropapplication': {
            'Meta': {'object_name': 'ImageCropApplication'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'crop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['mediacat.ImageCrop']"}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mediacat']