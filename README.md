**Django LTI Integration Application**

This application is designed to retrieve course and user IDs passed through custom fields during an LTI (Learning Tools Interoperability) launch. It then displays a list of users in a course along with their assignments, indicating whether they have submitted the assignments or not.

1. **Clone the Repository:** Clone the project repository to your local machine and navigate into the project directory.
2. **Install Django:** Install Django using pip.
3. **Create a Django Project:** Create a new Django project and navigate into the project's directory.
4. **Create a Django App:** Create an application within the Django project.
5. **Project Configuration:**<br/>
       Open the settings.py file and:<br/>
         ---- Add the application and SSL server to the INSTALLED_APPS.<br/>
         ---- Comment out the CSRF middleware in the MIDDLEWARE section.<br/>
         Include the PYLTI_CONFIG variable for the application consumers and secrets.
6. **URL Configuration:**<br/>
       ---- Create a urls.py file in the app's folder and define the URL patterns.<br/>
       ---- Modify the main project's urls.py file to include the app's URLs.<br/>
7. **Create Views:** In the app's views.py file, create views to handle the course and user information.
8. **Apply Migrations:** Apply the migrations to set up the database.
9. **Install SSL Server:** Install the SSL server to allow secure connections.
10. **Run the Server:** Run the Django server using SSL to make the application accessible.
11. **LTI Integration with Canvas:**<br/>
      ---- Create a course in Canvas and add a module.<br/>
      ---- Use the "External Tool" option in Canvas to link the application.<br/>
      ---- Add custom fields for custom_course_id and custom_user_id in the Canvas app settings.
