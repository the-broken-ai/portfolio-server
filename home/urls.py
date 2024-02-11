from django.urls import include, path

from home import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('api-token-auth/', views.CustomObtainAuthToken.as_view()),
]
