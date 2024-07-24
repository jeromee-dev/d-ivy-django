from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from .models import Profile, Skill


def search_profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET['search_query']
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    return profiles, search_query


def paginate_profiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)
    
    try:
        if page is not None and page.isnumeric():
            page = int(page)
        else:
            raise PageNotAnInteger
        profiles = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.get_page(page)

    left_index = 1 if page - 4 < 1 else page - 4
    right_index = paginator.num_pages + 1 if page + 5 > paginator.num_pages else page + 5
    
    custom_range = range(left_index, right_index)
    return custom_range, profiles