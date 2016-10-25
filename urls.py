from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect


# Not the best place for views, but this is test task
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('gmail.urls')),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
]
