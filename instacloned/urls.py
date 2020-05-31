from django.urls import path,re_path

urlpatterns = [

]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )