'''
==============================================
django-cloudistatic library
Author: Dibyajyoti Mondal
Github Profile : https://github.com/djm-1
==============================================
'''
from django.core.management.base import BaseCommand, CommandError
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings
import os
import shutil


class Command(BaseCommand):
    help='Uploads the static files to cloudinary'
    
    '''
        Additional arguments for cloudistatic
    '''
    def add_arguments(self, parser):

        '''
        Named (optional) arguments to delete
        existing STATIC_ROOT in the current django project

        Usage => python manage.py cloudistatic --deletelocal
        '''

        parser.add_argument(
            '--deletelocal',
            action='store_true',
            help='Delete local STATIC_ROOT after uploading contents to Cloudinary',
        )



    def handle(self,*args,**options):
        
        '''
        Referring to Cloudinary credentials
        mentioned in settings.py file
        '''
        
        cloud_name = settings.CLOUDI_NAME
        api_key = settings.CLOUDI_API_KEY
        api_secret = settings.CLOUDI_API_SECRET        
        
        '''
        configuring Cloudinary upload
        '''

        cloudinary.config( 
          cloud_name = cloud_name, 
          api_key = api_key, 
          api_secret = api_secret,
          secure = True
        )
        
        '''
        file upload count
        '''

        upload_count=0
        
        
        '''
        Uploading all files from STATIC_ROOT to Cloudinary
        '''

        for dirpath, dirnames, filenames in os.walk(settings.STATIC_ROOT):
            for filename in [f for f in filenames]:
                file_to_upload=os.path.join(dirpath, filename)
                response=cloudinary.uploader.upload(file_to_upload, 
                    folder = dirpath.replace('\\','/'), 
                    public_id = os.path.splitext(filename)[0],
                    invalidate=True,
                    overwrite = True, 
                    resource_type = "raw",
                )
                
        
                print (file_to_upload+' uploaded...')
                upload_count+=1
        print(f'\n{upload_count} files staticfiles uploaded successfully !!!')
        

        '''
        if delete argument given
        '''

        if options['deletelocal']:
            static_root=settings.STATIC_ROOT
            shutil.rmtree(settings.STATIC_ROOT)
            print(f'Local STATIC_ROOT directory {static_root} removed')