from django.shortcuts import render
import requests
from hume.models import thumb

API_KEY = '83e3f2145ec04fd19b954440caceacab'

# Home view to display articles fetched from the News API
def home(request):
    url = f'https://newsapi.org/v2/everything?q=apple&from=2023-09-08&to=2023-09-08&sortBy=popularity&apiKey={API_KEY}'
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code != 200:
        # If the request fails, return an error message
        return render(request, 'base/home.html', {'error': 'Failed to retrieve data from the news API.'})
    
    data = response.json()

    # Safely access the 'articles' key, defaulting to an empty list if not found
    articles = data.get('articles', [])
    
    context = {
        'data': data,
        'articles': articles,
    }

    return render(request, 'base/home.html', context)


# Category view to display articles by category
def category(request, category):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code != 200:
        # If the request fails, return an error message
        return render(request, 'base/category.html', {'error': 'SELECT CATEGORY TO EXPLORE'})
    
    data = response.json()

    # Safely access the 'articles' key, defaulting to an empty list if not found
    articles = data.get('articles', [])
    
    context = {
        'category': category.capitalize(),  # Capitalize the category name for display
        'articles': articles,
    }
    
    return render(request, 'base/category.html', context)

def homepage(request):
    # Fetch all the video data
    humeData = thumb.objects.all().order_by('?') 
    return render(request, 'index.html', {'humeData': humeData})
