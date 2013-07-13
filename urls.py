from django.conf.urls import patterns, include, url
#from blog import views

urlpatterns = patterns('blog.views',
	url(r"^delete_comment/(\d+)/$", "delete_comment"),
	url(r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
	url(r"^month/(\d{4})/(\d+)/$", "month"),
	url(r"^(\d+)/$", "post"),
	url(r"^add_comment/(\d+)/$", "add_comment"),
	url(r"^(\d{4})/(\d+)/$", "month"),
	url(r"", "main"),
)
