from browse.models import Review, Course, Professor
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['target', 'course', 'text']


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'number', 'department']


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'school']
