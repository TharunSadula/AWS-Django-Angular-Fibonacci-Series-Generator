from django.conf.urls import url
from django.views.generic import TemplateView

from .api import FibApi
urlpatterns = [
    url(r'^fib/(?P<num>.+)$', FibApi.as_view()),
    url(r'^$', TemplateView.as_view(template_name="core/home.html")),
]
