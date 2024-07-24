from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ProjectForm, ReviewForm
from .models import Project, Tag
from .utils import search_projects, paginate_projects


def projects(request):
    search_query = ''
    projects, search_query = search_projects(request)
    results = 6
    custom_range, projects = paginate_projects(request, projects, results)

    context = {'projects': projects, 'search_query': search_query, 
               'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project_obj
        review.owner = request.user.profile
        review.save()
        # get_vote count is defined as a @property but based on the usage below I think it would be better as a method
        project_obj.get_vote_count
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=project_obj.id)

    return render(request, 'projects/single-project.html', {'project': project_obj, 'form': form})


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    if request.method == 'GET':
        form = ProjectForm()
        context = {'form': form}
        return render(request, 'projects/project-form.html', context)
    elif request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    # this line below improves on the above because now we can only get that id if it is ownerd by the current user
    project = profile.project_set.get(id=pk)
    if request.method == 'GET':
        form = ProjectForm(instance=project)
        context = {'form': form}
        return render(request, 'projects/project-form.html', context)
    elif request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'GET':
        context = {'object': project}
        return render(request, 'delete-template.html', context)
    elif request.method == 'POST':
        project.delete()
        return redirect('projects')