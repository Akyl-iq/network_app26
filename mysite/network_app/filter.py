import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    hashtag = django_filters.CharFilter(field_name='hashtag__hashtag_name', lookup_expr='icontains')
    user = django_filters.NumberFilter(field_name='people__id')

    class Meta:
        model = Post
        fields = ['hashtag', 'user']