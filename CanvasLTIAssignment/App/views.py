from django.http import HttpResponse
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = "7~cvchMnLunvwRhLXxhtVKGJa6MtBkXc8D7E96wJJNYC67M7PH2wPM86nN72YGzXcZ"


def index(request):
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)
    course = canvas.get_course(request.POST["custom_course_id"])
    user = course.get_user(request.POST["custom_user_id"])
    welcome_mssg = f'<p>Welcome user: {user.name} to the course: {course.name}</p>'
    welcome_mssg+='<p>The students in this course are:</p>'
    users = course.get_users()
    user_dict = {}
    for user in users:
        user_dict[user.id] = user.name
        welcome_mssg += f'<p>{user.name}</p>'

    assignments = course.get_assignments()
    welcome_mssg+='<p>Following are assignments in the course along with whether they are submitted or unsubmitted </p>'
    for assignment in assignments:
        for submission in assignment.get_submissions():
            welcome_mssg+=f'<p>{user_dict.get(submission.user_id)} - {assignment.name} - {submission.workflow_state }</p>'
    return HttpResponse(welcome_mssg)

