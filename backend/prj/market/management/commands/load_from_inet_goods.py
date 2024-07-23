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
        URL= 'https://prime-food.com.ua/subcategory/97/#prod_section'   
        category_name = "М'ясна Гастрономія"
        sub_category_name = 'Закарпатські сирокопчені делікатеси'
        #--------------------------------------------------------------------------------

        current_category=Category.objects.filter(name=category_name).first()
        current_subcategory=SubCategory.objects.filter(name=sub_category_name).first()
        print('-------------------------------------------------------------------------------')
        print('Start importing from %s' % URL)
        rez= requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')
        content = soup.findAll('div', {'class':'prod-item'})
         
        
        for item in content:
            img = item.find('img')

            good = Product()
            good.category=current_category
            good.subcategory=current_subcategory
            good.name = img.get('alt')

            if img.get('src'):
                print(img.get('src'))
                img_url = 'https://prime-food.com.ua%s' % img.get('src')
                print('img_url', img_url)
                img_response = requests.get(img_url, stream=True, verify=False)
                with open('tmp.webp', 'wb') as out_file:
                    shutil.copyfileobj(img_response.raw, out_file)
                with open('%s/tmp.webp' % BASE_DIR, 'rb') as img_file:
                    good.image.save('good.webp', File(img_file), save=True)
                good.save()

                print('Saving ...%s' % good.name)

            # elif img.get('data-src'):
            #     print(img.get('data-src'))
            #     img_url = 'https://prime-food.com.ua%s' % img.get('data-src')
            #     print('img_url', img_url)
            #     img_response = requests.get(img_url, stream=True, verify=False)
            #     with open('tmp.webp', 'wb') as out_file:
            #         shutil.copyfileobj(img_response.raw, out_file)
            #     with open('%s/tmp.webp' % BASE_DIR, 'rb') as img_file:
            #         good.image.save('good.webp', File(img_file), save=True)
            #     good.save()

            #     print('Saving ...%s' % good.name)   
            
            else:
                print(f'current {img.get('alt')} not found src')    
                
            print('-------------------------------------------------------------------------------')
            print('=================================================================================')
            
            
            
          
            
            
            


        




