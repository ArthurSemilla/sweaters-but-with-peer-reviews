from django.conf.urls import url
import api.views as aviews
import api.new_views as nviews
# import new.views as nviews

urlpatterns = [
    url(r'^professors?$', aviews.get_professors),
    url(r'^courses?$', aviews.get_courses),

    url(r'^courses_matching/(?P<partial>.+)$',
        aviews.get_courses_matching),
    url(r'^schools_matching/(?P<partial>.+)$',
        aviews.get_schools_matching),
    url(r'^departments_matching/(?P<partial>.+)$',
        aviews.get_departments_matching),
    url(r'^professors_matching/(?P<partial>.+)$',
        aviews.get_professors_matching),
    url(r'^fields_matching/(?P<partial>.+)$',
        aviews.get_fields_matching),
    url(r'^field_categiries_matching/(?P<partial>.+)$',
        aviews.get_fields_categories_matching),

    url(r'^course_per_professor$', aviews.get_course_per_professor),
    url(r'^get_fields_for_model/(?P<model>[A-Za-z_]+)$',
        aviews.get_fields_for_model),

    url(r'^view_for_model_at_id/(?P<model>[^\/]+)/(?P<id>[0-9]+)$',
        aviews.get_view_for_model),

    url(r'login/?$', aviews.login, name="login"),


    url(r'^(?P<page>(school|department|professor|review|course|field'
        '|fieldcategory))$',
        nviews.new, name="new"),
    url(r'^add_vote$', nviews.addVote, name="addVote"),
]