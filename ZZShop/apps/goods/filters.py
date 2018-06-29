# _*_ coding:utf-8  _*_

__author__ = 'zhy'
__date__ = '2018/4/6 19:30'

import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # 模糊查询， icontains-->i忽略大小写
    # name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method="top_category_filter")

    def top_category_filter(self, queryset, name, value):
        """类别的查找功能"""
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        # 后台xadmin中展示出什么？
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
