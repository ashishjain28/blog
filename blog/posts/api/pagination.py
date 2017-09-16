from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 4


class PostPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 3
