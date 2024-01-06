from django.contrib import admin
from dataloader.models import BhavcopyRaw,PRFolderStatus
import datetime as dt
from django.contrib import messages
import requests
import zipfile as zp
import re

# generate links till today
# first check what is the last link date and generate accordingly
# if  not select the first date and start to generate from that date


def download_pr_folder(prurl):
    req=requests.get(prurl)
    if(req.status_code==200):
        with open('./data/downloads/PR/'+prurl[-12:],'wb') as zip:
            zip.write(req.content)
        pdurl='./data/downloads/PR/'+prurl[-12:]
        with zp.ZipFile(pdurl,'r') as pdzip:
            for info in pdzip.infolist():
                print(info.filename)
                if re.match(r'^Pd.*csv$',info.filename):
                    # 'Pd'+prurl[-10:-4]+'.csv'
                    pdzip.extract(info,path='./data/downloads/PR/PdExtract/')
                    print('Extraction complete')
        return True
    else:
        return False
    

def create_pr_obj(folderdate,prurl):
    prfolder=PRFolderStatus(folder_date=folderdate,folder_link=prurl,folder_status='Generated')
    prfolder.save()

def download_pr_zip(modeladmin,request,queryset):
    for pr in queryset.filter(folder_status='Generated'):
        status=download_pr_folder(pr.folder_link)
        if status:
            pr.folder_status='Downloaded'
            pr.save()
            messages.success(request,'Folder Downloaded')
        else:
            pr.folder_status='Not Available'
            pr.save()
            messages.success(request,'Folder Not Available')
    messages.success(request,'Process Completed!')

def add_PR_data(modeladmin,request,queryset):
    FIRSTDATE=dt.date(2010,2,1)
    PR_URL_PREFIX='https://www1.nseindia.com/archives/equities/bhavcopy/pr/PR'
    PR_URL_SUFFIX='.zip'
    generated_urls={}
    if queryset is not None:
        last_date=queryset.latest('folder_date').folder_date
        today=dt.date.today()
        new_date=dt.date(2000,2,1)
        while(new_date.strftime('%d%m%y')!=today.strftime('%d%m%y')):
            
            new_date=(last_date+dt.timedelta(days=1))
            
            if (new_date.weekday()<5) :
                prurl=PR_URL_PREFIX+new_date.strftime('%d%m%y')+PR_URL_SUFFIX
                generated_urls[new_date.strftime('%d%m%y')]=prurl
            last_date=new_date

    else:
        last_date=FIRSTDATE
        new_date=''
        while(new_date!=today.strftime('%d%m%y')):
            
            new_date=last_date+dt.timedelta(days=1)
            
            if (new_date.weekday<5):
                generated_urls.append(PR_URL_PREFIX+new_date.strftime('%d%m%y')+PR_URL_SUFFIX)
            last_date=new_date
    for prdate ,prlink in generated_urls.items():
        year='20'+prdate[4:6]
        month=prdate[2:4]
        day=prdate[0:2]
        # print(year,month,day)
        folder_date=dt.date(year=int(year),month=int(month),day=int(day))
        create_pr_obj(folder_date,prlink)
        # break


    messages.success(request,'URLS generated')
download_pr_zip.short_description='Download PR Zip File'
add_PR_data.short_description='Add PR Folder till Today'
        # PRFolderStatus.objects.create()
class DataLoaderAdmin(admin.ModelAdmin):
    actions=[add_PR_data,download_pr_zip]     






# Register your models here.
admin.site.register(BhavcopyRaw)
admin.site.register(PRFolderStatus,DataLoaderAdmin)