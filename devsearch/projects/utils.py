from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Project, Tag


def search_projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET['search_query']
    tags = Tag.objects.distinct().filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags) # checking to see if the tags in this project query is in the tags we got above
    )
    return projects, search_query


def paginate_projects(request, projects, results):
    page = request.GET.get('page')
    if page is None: page = 1
    
    paginator = Paginator(projects, results)
    
    try:
        page = int(page)
        projects = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.get_page(page)

    left_index = 1 if page - 4 < 1 else page - 4
    right_index = paginator.num_pages + 1 if page + 5 > paginator.num_pages else page + 5
    
    custom_range = range(left_index, right_index)
    return custom_range, projects