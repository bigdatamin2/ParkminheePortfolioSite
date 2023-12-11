from django.urls import path
from . import views
from .views import index, detail, BoardCreateView, BoardDeleteView, BoardUpdateView

app_name = "board"

urlpatterns = [
    path('', views.index, name="list"),
    path('<int:board_id>/', views.detail, name="detail"),
    path('create/', BoardCreateView.as_view(), name="board_create"),
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name='board_delete'),
    path('<int:pk>/update/', BoardUpdateView.as_view(), name='board_update'),

]
