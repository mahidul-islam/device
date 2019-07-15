from django.urls import path
from . import views

app_name = "cripto"
urlpatterns = [
    path("<int:m_pub>/", views.partial, name="partial"),
]
