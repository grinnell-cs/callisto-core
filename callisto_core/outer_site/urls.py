from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(emotional-support|support|support-services)$', views.SupportServices.as_view(), name='support_services'),
    url(r'contact-?(us)?$', views.Contact.as_view(), name='contact'),
    url(r'how-it-works$', views.HowItWorks.as_view(), name='how-it-works'),
    url(r'help(-a-friend)?$', views.HelpAFriend.as_view(), name='help-a-friend'),
    url(r'reporting-options$', views.ReportingOptions.as_view(), name='reporting-options'),
    url(r'about$', views.About.as_view(), name='about'),
    url(r'privacy$', views.Privacy.as_view(), name='privacy'),
    url(r'(terms|terms-and-conditions|terms-conditions)$', views.Terms.as_view(), name='terms')
]
