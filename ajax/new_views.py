from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed

import json

from ajax.utils import get_template_for_model

from browse.models import Review, ReviewVote, Professor, School, Department, \
    Field, FieldCategory, Course
from new.forms import ReviewForm, ProfessorForm, SchoolForm, DepartmentForm, \
    FieldForm, FieldCategoryForm, CourseForm

@login_required
def new(request, page=None):
    model = None
    response = {"error": {"error": ""}}
    model_map = {"review": Review,
                 "professor": Professor,
                 "school": School,
                 "department": Department,
                 "course": Course,
                 "field": Field,
                 "fieldcategory": FieldCategory,
                 }
    model_form_map = {"review": ReviewForm,
                      "professor": ProfessorForm,
                      "school": SchoolForm,
                      "course": CourseForm,
                      "department": DepartmentForm,
                      "field": FieldForm,
                      "fieldcategory": FieldCategoryForm,
                      }

    if request.method != "POST":
        return get_template_for_model(request, model_form_map, page)

    data = json.loads(request.body.decode())

    if page not in model_map.keys():
        return json_error({"error": "Unknown page requested."})

    model = model_map[page]

    # Otherwise we will complain about it existing
    del data["error"]

    # If model has an owner or created by field, add us
    if model_form_map[page].needs_owner:
        data["owner"] = request.user
    elif model_form_map[page].needs_created_by:
        data["created_by"] = request.user

    for key in data.keys():
        # Check that this is a key that exists
        if key not in model._meta.get_all_field_names():
            return json_error({"error": ''.join(["No field for ",
                                                 str(model), ": \"",
                                                 key, "\""])})
        # Check that an id field exists for required foreign key fields
        field = model._meta.get_field(key)
        if field.is_relation and isinstance(data[key], dict):
            if "id" not in data[key]:
                response["error"][key] = "No {} specified".format(
                    field.target_field.model.__name__)
            elif not field.target_field.model.objects.filter(
                    id=data[key]["id"]).count():
                response["error"][key] = "{} does not exist".format(
                    field.target_field.model.__name__)
            else:
                data[key] = field.target_field.model.objects.get(
                    id=data[key]["id"])

    # Check for required keys
    for field in model_form_map[page].Meta.fields:
        if field not in data or data[field] == "":
            response["error"][field] = "No {} specified".format(
                field)

    # Look for any errors
    for k, v in response["error"].items():
        if len(v) > 0:
            return HttpResponse(json.dumps(response))

    # Try to create it
    try:
        new = model(**data)
    except Exception as e:
        print("ERROR: " + str(e))
        return HttpResponse(json_error({"error": str(e)}))

    for field in model_form_map[page].Meta.fields:
        response["error"][field] = ""  # clear errors

    response["id"] = new.id  # return new id at top level.

    # Save and return all info
    new.save()
    return HttpResponse(json.dumps(response))


def addVote(request):
    if request.method == "POST":
        if not request.user.is_authenticated():
            jsonResponse = {"success": False,
                            "error": "User not logged in"}
            return HttpResponse(json.dumps(jsonResponse),
                                content_type="application/json")

        review_id = request.POST.get("review-id")
        action = request.POST.get("action").lower()
        user = request.user
        review = Review.objects.get(id=review_id)

        try:
            vote = ReviewVote.objects.filter(target=review,
                                             owner=user)

            # If the vote exists, we need to change it based on input.
            # Currently votes are changed as such:
            #     If the user presses the same direction as their current vote
            #     then the vote is removed
            #     If the user presses opposite their vote, the vote is changed
            #     to the new direction
            if vote.exists():
                vote = vote[0]
                if (vote.quality and action == "up") or \
                   (not vote.quality and action == "down"):
                    vote.delete()
                else:
                    vote.quality = (action == "up")
                    vote.save()
            # vote doesn't exist yet, then it needs to be created.
            elif (action == "up" or action == "down"):
                vote = ReviewVote(target=review,
                                  owner=user,
                                  quality=(action == "up"))
                vote.save()

        except:
            jsonResponse = {"success": False,
                            "error": "Could not complete vote"}
            return HttpResponse(json.dumps(jsonResponse),
                                content_type="application/json")

        return HttpResponse(json.dumps({"success": True}),
                            content_type="application/json")
    else:
        return HttpResponseNotAllowed(["POST"])