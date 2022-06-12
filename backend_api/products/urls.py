from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductList, ProductDatail

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDatail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
