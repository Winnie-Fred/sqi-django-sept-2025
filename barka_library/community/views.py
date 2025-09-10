from django.shortcuts import render

# Create your views here.
def community_events(request):
    return render(request, "community/community.html")