from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    rbr = Project.objects.get(title = "Rotating Basin Report")
    uwa = Project.objects.get(title = "Unified Watershed Assessment")
    dataPort = Project.objects.get(title = "Water Quality Data Portal") 
    okram = Project.objects.get(title = "Wetlands Assessment (OKRAM)")
    rwip = Project.objects.get(title = "Restorable Streams and Wetlands Protocol") 

    return render(request, "dashboards/home.html", {'projects':projects, 'rbr':rbr, 'uwa':uwa, 'dataPort':dataPort, 'okram':okram, 'rwip':rwip})


