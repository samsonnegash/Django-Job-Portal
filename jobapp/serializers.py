from django.contrib.auth.models import User, Group
from rest_framework import serializers

from jobapp.models import Job, BookmarkJob


class JobSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.first_name')
    user_id = serializers.ReadOnlyField(source = 'user.id')

    class Meta:
        model = Job
        fields = ['id','user', 'user_id', 'title', 'description','location','job_type','category','salary','company_name','url','last_date','is_published','is_closed','timestamp']





class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookmarkJob
        fields = ['id','user', 'job']

    def __str__(self):
        return self.job.title