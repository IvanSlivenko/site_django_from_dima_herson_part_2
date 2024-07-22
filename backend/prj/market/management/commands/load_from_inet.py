from django.core.management.base import BaseCommand, CommandError


from market.models import Category, Product
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from prj.settings import DATA_DIR, BASE_DIR

CURRENT_DATA_DIR = 'media'
CURRENT_DATA_DIR_PATH = fr'{BASE_DIR[:-3]}\{CURRENT_DATA_DIR}'                       
# CURRENT_FILE_NAME = 'price.xlsx'
# current_path = f'{CURRENT_DATA_DIR_PATH}\\{CURRENT_FILE_NAME}'


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Clearind DB')
        Category.objects.all().delete()
        Product.objects.all().delete()
        try:
            shutil.rmtree('%s\media' % BASE_DIR)
        except:
            pass    
        URL= 'https://prime-food.com.ua/uk/'
        print('Start importing from %s' % URL)
        rez= requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')
        content = soup.find('div', {'class':'main_grid'})
        
        
        for img in content.find_all('img'):
            c = Category()
            c.name = img.get('alt')
            img_url = 'https://prime-food.com.ua/%s' % img.get('src')
            # img_url = img.get('src')
            img_response = requests.get(img_url, stream=True, verify=False)
            # print(img_url)
            with open('tmp.png', 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            with open('%s/tmp.png' % BASE_DIR, 'rb') as img_file:
                c.image.save('cat.png', File(img_file), save=True)
            c.save()
            print('Saving ...%s' % c.name)
            
            
            


        




