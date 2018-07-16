# from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'callisto_core/outer_site/intro.html'

    def get_queryset(self):
        return;

class SupportServices(generic.ListView):
    template_name = 'callisto_core/outer_site/support_services.html'
    
    def get_queryset(self):
        return;
        
class Contact(generic.ListView):
    template_name = 'callisto_core/outer_site/contact.html'
    
    def get_queryset(self):
        return;
        
class HowItWorks(generic.ListView):
    template_name = 'callisto_core/outer_site/how-it-works.html'
    
    def get_queryset(self):
        return;
        
class HelpAFriend(generic.ListView):
    template_name = 'callisto_core/outer_site/help-a-friend.html'
    
    def get_queryset(self):
        return;
        
class ReportingOptions(generic.ListView):
    template_name = 'callisto_core/outer_site/reporting-options.html'
    
    def get_queryset(self):
        return;
        
class About(generic.ListView):
    template_name = 'callisto_core/outer_site/about.html'
    
    def get_queryset(self):
        return;
        
class Privacy(generic.ListView):
    template_name = 'callisto_core/outer_site/privacy.html'
    
    def get_queryset(self):
        return;
        
class Terms(generic.ListView):
    template_name = 'callisto_core/outer_site/terms.html'
    
    def get_queryset(self):
        return;