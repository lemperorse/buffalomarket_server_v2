from django.db.models import Q
from django_filters import Filter, FilterSet, NumberFilter
from service_main.models import Category, CategoryDetail, Product, Geography, Province, Amphur, District, Choice, Profile, Farm, Social
class ListFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        self.lookup_expr = 'in'
        values = value.split(',')
        return super(ListFilter, self).filter(qs, values)



class ProductFilter(FilterSet):
    category = ListFilter(field_name='category')
    price_in = NumberFilter(field_name='price', lookup_expr='gt')
    price_out = NumberFilter(field_name='price', lookup_expr='lt')
    price_start = NumberFilter(field_name='price_start', lookup_expr='gt')
    price_end = NumberFilter(field_name='price_end', lookup_expr='lt')
    class Meta:
        model = Product #'farm__province','farm__amphur','farm__district'
        fields  = ['category','id','farm','user','product_type','price_in','price_out','price_start','price_end','farm__province','status']
    # def filter_both(self, queryset, geo, value):
    #     return queryset.filter(
    #         Q(geo=value)
    #     )
