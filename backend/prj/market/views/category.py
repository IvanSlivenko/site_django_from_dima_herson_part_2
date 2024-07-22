from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action



from market.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryViewSet(viewsets.ModelViewSet):
    """
    CategoryViewSet coment

    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_clasess = [permissions.AllowAny]
    # http_method_names = ['get', 'post', 'patch', 'delete', 'put'] # all methods
    http_method_names = ['get', 'post'] # custome match method 

    # @action(detail=True, methods = ['post'])
    @action(detail=False, methods = ['post'])
    def set_password(self, request, pk=None):
        pass


        
