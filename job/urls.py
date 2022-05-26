from django.contrib import admin
from django.urls import path , include
from jobapp import views, viewset

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobapp.urls')),
    path('', include('account.urls')),
    path('api/jobs', viewset.JobView.as_view() ),
    path('api/jobs/<int:pk>', viewset.JobDetail.as_view() ),
    path('api/jobs/<int:pk>/delete', viewset.JobDelete.as_view() ),
    path('api/jobs/<int:pk>/update', viewset.JobUpdate.as_view() ),
    path('api/saved', viewset.SavedJob.as_view() ),





  #  path('api/Createjobs', viewset.JobView.as_view() ),



]

