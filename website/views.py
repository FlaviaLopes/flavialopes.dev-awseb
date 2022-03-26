from django.shortcuts import render
from .models import *
from datetime import date


def index(request):
    tags = HeadTag.objects.first()
    card = Card.objects.first()
    socials = Social.objects.all()
    social_networks = {}
    for it in socials:
        social_networks.update({it.social_network_name: it.social_network_link})
    del socials

    socials = ShareOn.objects.all()
    share_on = {}
    for it in socials:
        share_on.update({it.social_network_name: it.social_network_link})
    del socials

    about = About.objects.order_by('created_date')[0]

    projects = Project.objects.order_by('created_date')

    current_year = date.today().year

    return render(request, 'website/sitebase.html', locals())
