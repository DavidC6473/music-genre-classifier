from django.db import models

class MusicFile(models.Model):
    file = models.FileField(upload_to='music_files')

class ClassificationResult(models.Model):
    music_file = models.ForeignKey(MusicFile, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
