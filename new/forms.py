"""
This file houses forms which are used to check if submitted JSON blobs have
the appropriate fields required.
"""

from browse.models import Review, Course, Professor, School, Department,\
    Field, FieldCategory, ReviewComment, Report, PeerReview
from django.forms import ModelForm


class ReviewForm(ModelForm):
    """
    Fields in all of these models lists fields which must be filled by a
    form. fields_extra are for metafields, which are in forms, but aren't on
    the models themselves and are ignored when doing required data checks.

    When in doubt, just add whatever you have to fields. Fields_extra is rare.
    """
    needs_owner = True
    needs_created_by = False

    class Meta:
        model = Review
        fields = ['target', 'course', 'text', 'title', 'rating_overall',
                  'rating_value', 'rating_difficulty']
        fields_extra = []


class CourseForm(ModelForm):
    needs_owner = False
    needs_created_by = True

    class Meta:
        model = Course
        fields = ['name', 'number', 'department']
        fields_extra = []


class ProfessorForm(ModelForm):
    needs_owner = False
    needs_created_by = True

    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'school']
        fields_extra = []


class SchoolForm(ModelForm):
    needs_owner = False
    needs_created_by = True

    class Meta:
        model = School
        fields = ['name', 'location', 'url', 'email_pattern']
        fields_extra = []


class DepartmentForm(ModelForm):
    needs_owner = False
    needs_created_by = True

    class Meta:
        model = Department
        fields = ['name', 'school', 'fields', 'url']
        fields_extra = []


class FieldForm(ModelForm):
    needs_owner = False
    needs_created_by = True

    class Meta:
        model = Field
        fields = ['name', 'categories']
        fields_extra = []


class FieldCategoryForm(ModelForm):
    needs_owner = False
    needs_created_by = True

    class Meta:
        model = FieldCategory
        fields = ['name']
        fields_extra = []


class CommentForm(ModelForm):
    needs_owner = True
    needs_created_by = False

    class Meta:
        model = ReviewComment
        fields = ['text', 'target', 'owner']
        fields_extra = []


class ReportForm(ModelForm):
    needs_owner = True
    needs_created_by = False

    class Meta:
        model = Report
        fields = ['summary']
        # Only used for internal checks.
        fields_extra = ['text']


class ResolveReportForm(ModelForm):
    needs_owner = True
    needs_created_by = False

    class Meta:
        model = Report
        fields = ['summary']
        # Only used for internal checks.
        fields_extra = ['text']


class PeerReviewForm(ModelForm):
    class Meta:
        model = PeerReview
        fields = ['text', 'rating', 'flag']
        fields_extra = []
