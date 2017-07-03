from django.conf.urls import url, patterns
from .views import PostsView, PostView


urlpatterns = patterns('',
	url(r'^post/(?P<slug>[\w-]+)/$', PostView.as_view()),
	url(r'^$', PostsView.as_view())
)