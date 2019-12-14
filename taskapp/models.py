from django.db import models

# Create your models here.

class FieldUpload(models.Model):
    enter_char = models.CharField(max_length = 500)
    file_upload = models.FileField(upload_to = 'files')
    original_enter_char = None
    original_file_upload = None

    def __str__(self):
        return self.enter_char

    def __init__(self, *args, **kwargs):
        super(FieldUpload, self).__init__(*args, **kwargs)
        self.original_enter_char = self.enter_char
        self.original_file_upload = self.file_upload


    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.original_enter_char:
            if self.enter_char != self.original_enter_char:
                print('Enter char changed from ' + self.original_enter_char + ' to ' + self.enter_char)
            elif self.file_upload != self.original_file_upload:
                print('File changed from '+ self.original_file_upload.url + ' to ' + self.file_upload.url)
        else: 
            print('Object Created')
        super(FieldUpload, self).save(force_insert, force_update, *args, **kwargs)
        
