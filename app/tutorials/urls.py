from django.urls import path
from tutorials import views as tutorials_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', tutorials_views.index.as_view(), name='home'),
    path('api/tutorials/', tutorials_views.tutorial_list),
    path('api/tutorials/<int:pk>/', tutorials_views.tutorial_detail),
    path('api/tutorials/published/', tutorials_views.tutorial_list_published)
    path('cust-list', views.custList, name='cust-list'),
    path('cust-create', views.custCreate, name='cust-create'),
    path('cust-update/<int:id>', views.custUpdate, name='cust-update'),
    path('cust-delete/<int:id>', views.custDelete, name='cust-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
