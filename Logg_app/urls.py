from django.urls import path
from .views import log_example_view

urlpatterns = [
    path("log-test/", log_example_view),
]
