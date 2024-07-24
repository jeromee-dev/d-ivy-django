import uuid

from django.db import models

from users.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    # the first argument in the ManyToManyField constructor is the to argument and it has the model that it has the many to many relationship with. Normally we would just pass in the name of the class but because the class we are referenceing is defined below thiis class we have to pass in the name of the model we are making the relationship with as a string 
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True) # personally, since we are setting the vote to 0 by default I don't see why we set null=True
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    # I personally think this should be a method especially since it does not return a value but the tutorial defines this as a proprty
    @property
    def get_vote_count(self):
        reviews = self.review_set.all()
        upvotes = reviews.filter(value='up').count()
        total_votes = reviews.count()
        ratio = (upvotes / total_votes) * 100  # ratio as a percentage
        self.vote_total = total_votes
        self.vote_ratio = ratio
        self.save()
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # using on_delete=models.CASCADE means that when the corresponding entry in the Project table is deleted then we delete all the associated Reviews too. The other option in on_delete=models.SET_NULL
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    
    class Meta:
        unique_together = [['owner', 'project']]


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name