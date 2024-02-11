from django.urls import include, path

from home import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('api/csrf_token/', views.csrf_token, name='csrf_token'),
    path('api-token-auth/', views.CustomObtainAuthToken.as_view()),
    path('submit/post/',views.PostCreateView.as_view(), name='post-create'),
]
