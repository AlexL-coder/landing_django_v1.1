from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

def home(request):
    # Determine the base directory for articles
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'static')

    # Get category and article name from the query parameters
    category = request.GET.get('category', 'default')
    article_name = request.GET.get('article', 'default_article.html')

    # Build the path to the requested article
    if category == 'default':
        article_path = os.path.join(base_dir, 'default', article_name)
    else:
        article_path = os.path.join(base_dir, category, f"{article_name}.html")

    # Load the article content
    try:
        with open(article_path, 'r', encoding='utf-8') as file:
            article_content = file.read()
    except FileNotFoundError:
        article_content = "<h3>Article Not Found</h3><p>The requested article could not be found.</p>"

    return render(request, 'landing/home.html', {'article_content': article_content})


def article_view(request, category, article_name):
    # Define the base directory where articles are stored
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'static', category)

    # Construct the path to the requested article
    article_path = os.path.join(base_dir, f"{article_name}.html")

    try:
        # Read the content of the static HTML file
        with open(article_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # Return the content as an HTTP response
        return HttpResponse(content)
    except FileNotFoundError:
        # Return a 404 error if the file does not exist
        raise Http404("Article not found.")