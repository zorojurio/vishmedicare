from django.urls import path
from pages.views import ContactUsView, AboutUsView

app_name="pages"
urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
]
