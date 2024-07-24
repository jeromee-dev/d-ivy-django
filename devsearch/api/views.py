from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer
from projects.models import Project, Review


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},
        
        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def get_projects(request):
    print('USER', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_vote(request, pk):
    project = Project.objects.get(pk=pk)
    user = request.user.profile
    data = request.data
    print('DATA', data)
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project
    )
    review.value = data['value']
    review.save()
    project.get_vote_count
    serialzer = ProjectSerializer(project, many=False)
    return Response(serialzer.data)