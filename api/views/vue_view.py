from django.views.generic import TemplateView


class VueAppView(TemplateView):
    template_name = 'vueapp/index.html'
