from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from hume.models import thumb
from cybero.models import thumb_cybero
from aimlo.models import thumb_aimlo
from webo.models import thumb_webo
from videos.models import Video
from vid_aiml.models import Video_aiml
from vid_cyber.models import Video_cyber
from vid_web.models import Video_web
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from accounts.models import User  # Import your custom User model
from django.http import JsonResponse





def homepage(request):
    query = request.GET.get('search', '')  # Get the search query from the GET request
    if query:
        humeData = thumb.objects.filter(title__istartswith=query).order_by('?')  # Filter by title starting with query
    else:
        humeData = thumb.objects.all().order_by('?')  # Fetch all videos if no query is provided
    return render(request, 'index.html', {'humeData': humeData})


def aiml(request):
    # Fetch all the video data
    humeData = thumb_aimlo.objects.all().order_by('?') 
    return render(request, 'aiml.html', {'humeData': humeData})

def cyber(request):
    # Fetch all the video data
    humeData = thumb_cybero.objects.all().order_by('?') 
    return render(request, 'cyber.html', {'humeData': humeData})

def web(request):
    # Fetch all the video data
    humeData = thumb_webo.objects.all().order_by('?') 
    return render(request, 'web.html', {'humeData': humeData})

def login(request):
    return render(request,"login.html")


# @login_required(login_url='login')
def profile(request):
    return render(request,"profile.html")

def info(request) :
    return render(request,"info.html")

def upload(request) :
    return render(request,"upload.html")

def video(request, id):
    video = Video.objects.get(id=id)
    return render(request, "video.html", {'video': video})
#  data = {
#         'video': video
#     }
#     return render(request, "video.html", data)

def videoshown_aiml(request, id):
    videoshown_aiml = Video_aiml.objects.get(id=id)
    return render(request, "video_aiml.html", {'videoshown_aiml': videoshown_aiml})

def videoshown_cyber(request, id):
    videoshown_cyber = Video_cyber.objects.get(id=id)
    return render(request, "video_cyber.html", {'videoshown_cyber': videoshown_cyber})

def videoshown_web(request, id):
    videoshown_web = Video_web.objects.get(id=id)
    return render(request, "video_web.html", {'videoshown_web': videoshown_web})

def setting(request) :
    return render(request,"setting.html")

def contactus(request) :
    return render(request,"contactus.html")

def news(request) :
    return render(request,"news.html")


def video_cyber(request, id):
    videocy = Video_cyber.objects.get(id=id)
    return render(request, "video_cyber.html", {'video': videocy})

def video_web(request, id):
    videowe = Video_web.objects.get(id=id)
    return render(request, "video_web.html", {'video': videowe})

def saveEnquiry(request):
    if request.method=="POST":
        titlenows=request.POST.get('title')
        descriptionnows=request.POST.get('description')
        datenows=request.POST.get('date')
        thumbnailnows=request.POST.get('thumbnail')
        videonows=request.POST.get('video')
        datanows1=thumb(title=titlenows,dinak=datenows,thumbnail_image=thumbnailnows)
        datanows2=Video(title=titlenows,video_file=videonows,date=datenows,text=descriptionnows,image=thumbnailnows)
        datanows1.save()
        datanows2.save()

    humeData = thumb.objects.all().order_by('?') 
    return render(request, 'index.html', {'humeData': humeData})


def search_suggestions(request):
    query = request.GET.get('term', '')  # 'term' is used by most autocomplete plugins
    if query:
        suggestions = thumb.objects.filter(title__icontains=query).values_list('title', flat=True)[:10]
        return JsonResponse(list(suggestions), safe=False)  # Convert to JSON response
    return JsonResponse([], safe=False)


def welcome_matrix(request) :
    return render(request,"welcome.html")