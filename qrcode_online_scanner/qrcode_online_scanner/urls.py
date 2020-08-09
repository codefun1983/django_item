from django.urls import path, include

urlpatterns = [
    path('scanner/', include('app.urls')),
]
