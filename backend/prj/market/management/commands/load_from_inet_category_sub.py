from django.core.management.base import BaseCommand, CommandError


from market.models import Category, Product, SubCategory
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from prj.settings import DATA_DIR, BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Clearind DB-------------------------------------------------------------------')
        # Category.objects.all().delete()
        # SubCategory.objects.all().delete()
        # Product.objects.all().delete()
        # try:
        #     shutil.rmtree('%s\media' % BASE_DIR)
        # except:
        #     pass    

        #------------------------------------------------------------ input current value    
        URL= 'https://prime-food.com.ua/category/16/#subcategory'
        category_name = "Натуральні соки"
        #--------------------------------------------------------------------------------

        current_category=Category.objects.filter(name=category_name).first()
        # print(current_category)
        print('-------------------------------------------------------------------------------')
        print('Start importing from %s' % URL)
        rez= requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')
        content = soup.find('div', {'class':'recipes'})
         
        
        for img in content.find_all('img'):
            subcat = SubCategory()
            subcat.category=current_category
            subcat.name = img.get('alt')
            img_url = 'https://prime-food.com.ua%s' % img.get('src')
            # img_url = img.get('src')
            img_response = requests.get(img_url, stream=True, verify=False)
            print('-------------------------------------------------------------------------------')
            print(img_url)
            with open('tmp.webp', 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            with open('%s/tmp.webp' % BASE_DIR, 'rb') as img_file:
                subcat.image.save('sub_cat.webp', File(img_file), save=True)
            subcat.save()

            print('Saving ...%s' % subcat.name)
            
          
            
            
            


        




