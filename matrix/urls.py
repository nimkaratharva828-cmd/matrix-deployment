from django.contrib import admin
from django.urls import path, include
from matrix import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('profile/', views.profile),
    path('info', views.info),
    path('upload', views.upload),
    path('video/<int:id>/', views.video, name='video_detail'),
    path('video_of_aiml/<id>',views.videoshown_aiml, name='video_detail_aiml'),
    path('video_of_cyber/<id>',views.videoshown_cyber, name='video_detail_cyber'),
    path('video_of_web/<id>',views.videoshown_web, name='video_detail_web'),
    path('aiml', views.aiml),
    path('cyber', views.cyber),
    path('web', views.web),
    path('setting', views.setting),
    path('welcome_matrix/', views.welcome_matrix, name='welcome_matrix'),
    path('', include('base.urls')),
    path('contactus', views.contactus),
     # Include the URLs from the accounts app
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
    path('saveenquiry', views.saveEnquiry,name='saveenquiry'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
