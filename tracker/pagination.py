from rest_framework.pagination import PageNumberPagination


class PageSize(PageNumberPagination):
    page_size = 5
    page_size_query = "page_size"
    max_page_size = 5