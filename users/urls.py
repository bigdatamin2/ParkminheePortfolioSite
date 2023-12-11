from django.urls import path
from . import views
from .views import certificate_view, CertificateListView


urlpatterns = [
  path('', views.index, name="list"),
  path('AboutMe', views.AboutMe, name="AboutMe"),
  path('ResearchProject', views.ResearchProject, name="ResearchProject"),
  path('Certificate/', views.certificate_view, name='certificate_view'),
  path('Certificate/', certificate_view, name='Certificate'),

  path('certificate_list/', CertificateListView.as_view(), name='certificate_list'),
  path('SchoolLife', views.SchoolLife, name="SchoolLife"),
  path('<int:certificate_id>/', views.detail, name="detail"),
]