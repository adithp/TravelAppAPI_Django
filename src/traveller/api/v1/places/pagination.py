from rest_framework import pagination


class StandardResultSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_query = "page"
    page_size_query_param = "page_size"
    max_page_sizze = 100
    
    