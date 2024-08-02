from django.core.management.base import BaseCommand, CommandError


from market.models import Category, Product, SubCategory, InStock
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from prj.settings import DATA_DIR, BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_status='toOrder'
        products=Product.objects.all()
        current_instock = InStock.objects.filter(status=current_status).first()

        for el in products:
            el.in_stock=current_instock
            el.save()
            print(el.name)
        
            
          
            
            
            


        




