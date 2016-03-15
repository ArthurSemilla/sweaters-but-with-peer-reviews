"""
All of these drop a lumx form where they are called. Please note that you must
have new.js loaded and lumx dependencies included.
"""
from django import template


register = template.Library()


@register.inclusion_tag("new/tags/professor.html")
def new_professor():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/new_professor_popup.html")
def new_professor_popup(button=None, wrap_controller=True):
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/course.html")
def new_course():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/school.html")
def new_school():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/department.html")
def new_department():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/review.html")
def new_review():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/field.html")
def new_field():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/field_category.html")
def new_field_category():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}


@register.inclusion_tag("new/tags/school.html")
def new_school():
    """
    Must be within a ng-controller="form-handler" with a parameter for this
    form model.
    """
    return {}