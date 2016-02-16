from django.conf.urls import url
import browse.views as bviews

urlpatterns = [
    url(r'^user/(?P<id>[0-9]+)?$', bviews.profile, name="profile"),
    url(r'^school/(P?<id>[0-9]+)?$', bviews.school, name="school"),
    url(r'^professor/(?P<id>[0-9]+)?$', bviews.professor, name="professor"),

    url(r'^review/(?P<review_id>[0-9]+)/?$', bviews.review, name="review"),
    url(r'^new_review/?$', bviews.new_review,
        name="new_review"),
    url(r'^reviews/?$', bviews.reviews, name="reviews_overview"),
    url(r'^reviews/(?P<page>[0-9]+)/?$', bviews.reviews, name="reviews"),
    url(r'^reviews/(?P<page>[0-9]+)/(?P<type>[A-Za-z_]+)/?$', bviews.reviews,
        name="reviews_by_type"),
    url(r'^reviews/(?P<page>[0-9]+)/(?P<type>[A-Za-z_]+)/'
        '(?P<first_id>[0-9]+)/?$', bviews.reviews, name="reviews_by_type_one"),
    url(r'^reviews/(?P<page>[0-9]+)/(?P<type>[A-Za-z_]+)/(?P<first_id>[0-9]+)'
        '/(?P<second_id>[0-9]+)/?$', bviews.reviews,
        name="reviews_by_type_two"),

    url(r'login/?$', bviews.login, name="login"),
    url(r'logout/?$', bviews.logout, name="logout"),
]
