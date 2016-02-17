from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from browse.models import Professor, School, Course, Review, Department


class BrowseViewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        self.creds = {"username": "jason", "password": "top_secret"}
        self.two_review_types = ["by_school", "by_professor"]
        self.three_review_types = ["by_school_professor"]
        self.user = User.objects.create_user(**self.creds,
                                             email="jsholm@mst.edu",
                                             first_name="Jason",
                                             last_name="Holm")

        self.mst = School(name="Missouri S&T", url="http://mst.edu/")
        self.mst.save()

        # Create a professor
        self.price = Professor(created_by=self.user, first_name="Clayton",
                               last_name="Price", school=self.mst)
        self.price.save()

        # With a department
        self.cs = Department(created_by=self.user, name="Computer Science",
                             school=self.mst, url="http://cs.mst.edu")
        self.cs.save()

        # and a course
        self.course = Course(name="Object Oriented Numerical Modeling I",
                             number="5201", department=self.cs,
                             created_by=self.user)
        self.course.save()

        # Create a review
        self.review = Review(owner=self.user, text="Good stuff",
                             target=self.price, course=self.course)
        self.review.save()

    def test_index(self):
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)

    def test_profile_not_logged_in(self):
        resp = self.client.get(reverse("profile"))
        self.assertEqual(resp.status_code, 200)

        # Should be someone else.
        self.assertNotEqual(resp.context["user"].username, self.user.username)

    def test_profile_logged_in(self):
        self.client.login(**self.creds)
        resp = self.client.get(reverse("profile"))

        # Should be feeding it the profile for our user.
        self.assertEqual(resp.context["user"].username, self.user.username)

    def test_profile_specific(self):
        resp = self.client.get(reverse("profile", kwargs={"id": 2}))
        self.assertEqual(resp.status_code, 200)

        self.client.login(**self.creds)
        resp = self.client.get(reverse("profile", kwargs={"id": 2}))
        self.assertEqual(resp.status_code, 200)

    def test_login(self):
        resp = self.client.get(reverse("login"))
        self.assertEqual(resp.status_code, 200)

    def test_login_login(self):
        resp = self.client.post(reverse("login"), {
                                "username": self.user.username,
                                "password": self.user.password})
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        self.client.login(**self.creds)

        resp = self.client.get(reverse("logout"))
        self.assertEqual(resp.status_code, 302)  # redir to index

        resp = self.client.get(reverse("index"))
        self.assertEqual(str(resp.context["user"]), "AnonymousUser")

    def test_review_specific(self):
        resp = self.client.get(reverse("review", kwargs={"review_id": 2}))
        self.assertEqual(resp.status_code, 200)

    def test_reviews_overview(self):
        resp = self.client.get(reverse("review", kwargs={"review_id": 2}))
        self.assertEqual(resp.status_code, 200)

    def test_reviews_page(self):
        resp = self.client.get(reverse("reviews", kwargs={"page": 1}))
        self.assertEqual(resp.status_code, 200)

    def test_reviews_by_type(self):
        for type in self.two_review_types:
            resp = self.client.get(reverse("reviews",
                                   kwargs={"page": 1, "type": type,
                                           "first_id": 1}))
            self.assertEqual(resp.status_code, 200)

        for type in self.three_review_types:
            resp = self.client.get(reverse("reviews",
                                   kwargs={"page": 1, "type": type,
                                           "first_id": 1,
                                           "second_id": 1}))
            self.assertEqual(resp.status_code, 200)

    def test_school(self):
        resp = self.client.get(reverse("school"))
        self.assertEqual(resp.status_code, 200)

    def test_school_specific(self):
        resp = self.client.get(reverse("school", kwargs={"id": 1}))
        self.assertEqual(resp.status_code, 200)

    def test_professor(self):
        resp = self.client.get(reverse("professor"))
        self.assertEqual(resp.status_code, 200)

    def test_professor_specific(self):
        resp = self.client.get(reverse("professor", kwargs={"id": 1}))
        self.assertEqual(resp.status_code, 200)
