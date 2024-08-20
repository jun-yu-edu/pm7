from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('<int:id>/', views.article_detail),
    path('popular/', views.article_list_popular),
    # path('now_playing/', views.article_list_now_playing),

]
