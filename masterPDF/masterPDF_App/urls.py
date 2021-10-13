from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index, name="index"),
    path('compress', views.compress, name="compress"),
    path('compress_download',views.compress_download, name='compress_download'),
    path('merge', views.merge, name="merge"),
    path('merge_download',views.merge_download, name='merge_download'),
    path('split', views.split, name="split"),
    path('split_download',views.split_download, name='split_download'),
    path('p2w', views.p2w, name="p2w"),
    path('p2w_download',views.p2w_download, name='p2w_download'),
    path('w2p', views.w2p, name="w2p"),
    path('w2p_download',views.w2p_download, name='w2p_download'),
    path('pdf_reader',views.pdf_reader,name="pdf_reader"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
