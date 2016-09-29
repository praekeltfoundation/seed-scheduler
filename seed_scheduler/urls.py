import os
from django.conf.urls import patterns, include, url
from django.contrib import admin
from scheduler import views

admin.site.site_header = os.environ.get('SCHEDULER_TITLE', 'Scheduler Admin')


urlpatterns = patterns(
    '',
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api/metrics/', views.MetricsView.as_view()),
    url(r'^api/health/', views.HealthcheckView.as_view()),
    url(r'^', include('scheduler.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
)
