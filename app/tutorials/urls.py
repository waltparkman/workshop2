from django.urls import path
from tutorials import views as tutorials_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', tutorials_views.index.as_view(), name='home'),
    path('api/tutorials/', tutorials_views.list_all_tutorials),
    path('cust-list', tutorials_views.list_all_tutorials, name='cust-list'),
    path('cust-create', tutorials_views.custCreate, name='cust-create'),
    path('cust-update/<int:id>', tutorials_views.custUpdate, name='cust-update'),
    path('cust-delete/<int:id>', tutorials_views.custDelete, name='cust-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
