from django.db import models
from cryptography.fernet import Fernet
from django.db.models.signals import post_save,Signal
from django.dispatch import receiver
# Create your models here.

class FieldEncrypt(models.Model):
    char_file = models.CharField(max_length = 2000, blank=True,null=True)
    file_up = models.FileField(upload_to = 'files')
    original_char_file = None
    original_file_up = None

    def str(self):
        return self.char_file

    def __init__(self, *args, **kwargs):
        super(FieldEncrypt, self).__init__(*args, **kwargs)
        self.original_char_file = self.char_file
        self.original_file_up = self.file_up
        

@receiver(post_save, sender=FieldEncrypt)
def create_char_file(sender, instance, created, **kwargs):
    if created:
        #Process of encrypting the file which is newly created
        key = Fernet.generate_key()
        with open(instance.file_up.url, 'r'):
            data = bytes(instance.file_up.read())
        fernet = Fernet(key)
        #Storing encrypted data of the file in the object's char field
        instance.char_file = fernet.encrypt(data)
        print('Object created')
        instance.save()
    else:
        key = Fernet.generate_key()
        with open(instance.file_up.url, 'r'):
            data = bytes(instance.file_up.read())
        fernet = Fernet(key)
        d = fernet.encrypt(data)
       
        try:
            FieldEncrypt.objects.filter(file_up = instance.file_up.url, id = instance.id).update(char_file = d)
            print('File changed from ' + instance.original_file_up.url + ' to ' + instance.file_up.url)
            print('Original Charfield ' + instance.original_char_file)
            #Now we fetch the object using id as instance.char_file is still storing old value as we have not updated it and it will be updated as with new value whenever we make save on the object to modify it.
            s = FieldEncrypt.objects.get(id = instance.id)
            print('Updated CharField ' + s.char_file)
        except ValueError:
            pass