from django.urls import path
from .views import (
    UserBaseViewSet, RefreshViewSet, CompanyProjectViewSet, CompanyProjectsSettingsViewSet,
    CompanyAnaliticsViewSet
)

urlpatterns = [
    path('register/', UserBaseViewSet.as_view({'post': 'create'})),
    path('login/', UserBaseViewSet.as_view({'post': 'login'})),
    path('refresh/', RefreshViewSet.as_view({'post': 'post'}), name='token_refresh'),
    
    path('me/', UserBaseViewSet.as_view({'get': 'me'})),
    path('me/<str:id>/', UserBaseViewSet.as_view({'put': 'update'})),
    
    path("project/", CompanyProjectViewSet.as_view({'get': "lists", 'post': 'create'})),
    path("project/<str:id>", CompanyProjectViewSet.as_view({'get': "get", 'put': 'update', 'delete': 'delete'})),
    
    path("project/settings/", CompanyProjectsSettingsViewSet.as_view({'get': "lists", 'post': 'create'})),
    path("project/settings/<str:id>", CompanyProjectsSettingsViewSet.as_view({'get': "get", 'put': 'update', 'delete': 'delete'})),
    
    path("project/analitics/", CompanyAnaliticsViewSet.as_view({'get': "lists", 'post': 'create'})),
    path("project/analitics/<str:id>", CompanyAnaliticsViewSet.as_view({'get': "get", 'put': 'update', 'delete': 'delete'})),
]