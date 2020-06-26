from companies import views
from django.urls import path

app_name = 'companies'

urlpatterns = [
    path('', views.CompaniesIndexView.as_view(), name='index'),
    path('createNewCompany', views.NewCompanyView.as_view(), name="create_companies"),
    path('<int:pk>/updateCompany/', views.UpdateCompanyView.as_view(), name="update_companies"),
]
