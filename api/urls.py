from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register('roles', views.RoleViewSet, basename='role')
routers.register('users', views.UserViewSet, basename='user')
routers.register('officer-properties', views.OfficerPropertyViewSet, basename='officer-property')
routers.register('officer-maintenances', views.OfficerMaintenanceViewSet, basename='officer-maintenance')
routers.register('soldier-properties', views.SoldierPropertyViewSet, basename='soldier-property')
routers.register('soldier-maintenances', views.SoldierMaintenanceViewSet, basename='soldier-maintenance')
routers.register('non-residential-properties', views.NonResidentialPropertyViewSet, basename='non-residential-property')
routers.register('non-residential-maintenances', views.NonResidentialMaintenanceViewSet,
                 basename='non-residential-maintenance')

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('refresh', views.RefreshView.as_view()),
    path('current', views.CurrentUserView.as_view()),
    path('permissions', views.PermissionListView.as_view()),
    path('dashboard', views.DashboardView.as_view())
]

urlpatterns += routers.urls
