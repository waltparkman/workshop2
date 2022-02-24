from django.urls import path
from tutorials import views as cust_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', cust_views.custList, name='home'),
    path('cust-list', cust_views.custList, name='cust-list'),
    path('cust-create', cust_views.custCreate, name='cust-create'),
    path('cust-delete/<id>', cust_views.custDelete, name='cust-delete'),
    path('cust-update/<id>', cust_views.custUpdate, name='cust-update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
