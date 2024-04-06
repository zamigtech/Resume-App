from django.shortcuts import render
from core.models import GeneralSetting

# Create your views here.

def index(request):

    site_title = GeneralSetting.objects.get(name='site_title').parameters
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameters
    site_description = GeneralSetting.objects.get(name='site_description').parameters
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameters
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameters
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameters
    about_myself_footer =GeneralSetting.objects.get(name='about_myself_footer').parameters
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameters





    context={
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'about_myself_welcome': about_myself_welcome,


    }
    return render(request, 'index.html', context=context)
