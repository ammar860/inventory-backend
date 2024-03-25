from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from api.views import VueAppView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/api/', include('api.urls')),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('vueapp/', VueAppView.as_view()),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# urlpatterns += [re_path(r"^$", TemplateView.as_view(template_name='index.html'), name="index")]
