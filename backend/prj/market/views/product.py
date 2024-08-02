from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Product
from rest_framework import serializers
from market.views.category import CategorySerializer
from market.filters import ProductFilter


class ProduktSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'get_small_image_url', 'in_stock']




class ProductListView(ListModelMixin, GenericAPIView):
    queryset=Product.objects.all()
    serializer_class = ProduktSerializer
    filterset_class = ProductFilter
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)





