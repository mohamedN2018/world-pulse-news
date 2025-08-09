from . views import home, newsgategory, news_detail
from django.urls import path



app_name = 'main_core'

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('<slug:slug>/', newsgategory, name='newsgategory'),  # News category URL
    path('<slug:slug>/', news_detail, name='news_detail'),  # News detail URL
]