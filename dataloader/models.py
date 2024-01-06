from django.db import models

# Create your models here.
FILE_STATUS=(('Uploaded','Uploaded'),('Uploading Failed','Uploading Failed'),('Under Process','Under Process'),('Processing Completed','Processing Completed'),('Processing Failed','Processing Failed'))
FOLDER_STATUS=(('Generated','Generated'),('Downloaded','Downloaded'),('Not Available','Not Available'))
class BhavcopyRaw(models.Model):
    bhavcopy_csv_file = models.FileField(upload_to='./data/bhavcopy/uploads/', max_length = 100)
    file_date = models.DateField(auto_now=False, auto_now_add=False)
    upload_date=models.DateField(auto_now=False, auto_now_add=True)
    processing_date=models.DateTimeField(auto_now=True, null=True,blank=True)
    file_status=models.CharField(max_length=200,default='File Status', choices=FILE_STATUS)

    def __str__(self):
        return 'BHAVCOPY_'+str(self.file_date)
class PRFolderStatus(models.Model):
    folder_date = models.DateField(auto_now=False, auto_now_add=False)
    folder_link=models.URLField(max_length=500)
    folder_status=models.CharField(max_length=200,default='Folder Status', choices=FOLDER_STATUS)
    
    def __str__(self):
        return 'PR_FOLDER'+str(self.folder_date)+str(self.folder_status)
    
