from django.db import models
from datetime import datetime
from os.path import splitext

class SvgFile(models.Model):
    file = models.FileField(upload_to='%Y-%m-%d:%H:%M:%S', null=True)

    def __str__(self):
        return str(self.file)