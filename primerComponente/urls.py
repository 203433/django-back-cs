from django.urls import path, re_path
from django.conf.urls import include 
from primerComponente.views import PrimertTablaList


urlpatterns = [
    re_path(r'^primer_componente/$', PrimertTablaList.as_view()),
]