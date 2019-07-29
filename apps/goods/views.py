from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination

from .models import Goods, GoodsCategory, GoodsImage
from .serializaers import CategorySerializer, GoodsSerializer

# Create your views here.
class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100



class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination