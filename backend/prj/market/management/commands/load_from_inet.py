from django.core.management.base import BaseCommand, CommandError


from market.models import Category, Product
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from prj.settings import DATA_DIR, BASE_DIR

# CURRENT_DATA_DIR = 'init_data'
# CURRENT_DATA_DIR_PATH = fr'{BASE_DIR[:-3]}\{CURRENT_DATA_DIR}'                       
# CURRENT_FILE_NAME = 'price.xlsx'
# current_path = f'{CURRENT_DATA_DIR_PATH}\\{CURRENT_FILE_NAME}'


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Clearind DB')
        Category.objects.all().delete()
        Product.objects.all().delete()
        # shutil.rmtree('%s\media' % BASE_DIR)
        URL= 'https://www.atbmarket.com'
        # print('Start importing from %s' % URL)
        rez= requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')
        content = soup.find('div', {'class':'home-categories__row'})
        print(content)
        
        # home-categories__img
        # for img in content.find_all('img',{'class':'home-categories__row'}):
        #     print(img)
        #     break


        




