from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home page redirects to our one course page for now.  We will want to remove
    # this before we go to production of course.
    url(r'^$', redirect_to, {'url': '/nlp/Fall2012/'}),
    url(r'^nlp$', redirect_to, {'url': '/nlp/Fall2012/'}),

    # Health check endpoint.  Used by AWS load balancer.  Want something stable that
    # won't be redirected or change
    url(r'_health$', 'c2g.views.healthcheck'),

    # Examples:
    url(r'^courses$', 'c2g.views.home', name='c2g_home'),
    # url(r'^class2go/', include('class2go.foo.urls')),

    # accounts app for user management
    url(r'^accounts/profile/?$', 'accounts.views.profile', name='accounts_profile'),
    url(r'^accounts/profile/edit/?', 'accounts.views.edit'),
    url(r'^accounts/profile/save_edits/?', 'accounts.views.save_edits'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # The following line is temprarily commented out until we figure out how django cascades its URL matching operations.
	# After this is figured out, the rest of the matches below shall be moved to courses.url.
	#url(r'.*', include('courses.urls')),

	url(r'^courses/new/?', 'courses.admin_views.new'),

	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/?$', 'courses.views.main'),
    url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/overview/?$', 'courses.views.overview'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/syllabus/?$', 'courses.views.syllabus'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/admin/?', 'courses.admin_views.admin'),

	# Announcements
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/announcements/?$', 'courses.announcements.views.list'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/announcements/admin/?', 'courses.announcements.views.admin'),

	# Forums
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/forums/?$', 'courses.forums.views.view'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/forums/admin/?', 'courses.forums.views.admin'),


	# Videos
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/videos/?$', 'courses.videos.views.list'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/videos/admin/?', 'courses.videos.views.admin'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/videos/(?P<video_id>[a-zA-Z0-9_]+)/?$', 'courses.videos.views.view'),
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/videos/(?P<video_id>[a-zA-Z0-9_]+)/edit/?', 'courses.videos.views.edit'),

	# Video Exercises
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/video_exercises/(?P<video_id>[a-zA-Z0-9_]+)/?$', 'courses.video_exercises.views.view'),

    #Problem Sets
	url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/problemsets/?$', 'problemsets.views.list'),
    url(r'^(?P<course_prefix>[a-zA-Z0-9_]+)/(?P<course_suffix>[a-zA-Z0-9_]+)/problemsets/(?P<pset>[a-zA-Z0-9_]+)?$', 'problemsets.views.show'),
)
