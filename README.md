# We will launch a book very soon for basic Python, Flask, Cloud computing, RedHat openshift, Project creation and deployment on cloud and additional section of IBM product and features.(some unique project)

.....................................................

# Cloud Lab

![image](https://github.com/baiju012/Cloud_1/assets/111991510/d845d04b-7252-4818-9484-9e29bfb3f369)
![image](https://github.com/baiju012/Cloud_Lab/assets/111991510/1e6cd8e4-93c7-452a-9c5b-c701f46e97e1)


# Syllabus
* Basic web application on flask(run on web server in enable and disable )
* Building of url dynamically and have variable rules
* GET and POST methods of flask
* * jinza2 template in flask
* Simple admission and Health care form by using flask, html
* integrating css/js in flask



# If You are facing error like "not found", "Not responding" 

# Server is Runnings
* Confirm that your Flask server (appname.py) is running. When you run python appname.py
# Check The URL:
* Check the URL:  you're accessing the correct URL in your browser. In your code, you're defining the route as /login
* make sure you're trying to access http://127.0.0.1:5000

 # Port and Host:
 * Verify that the host and port in your HTML form match the Flask server configuration. In your HTML form
you have specified action="http://127.0.0.1:5000", which should match the host and port where your Flask app is running

# Correct HTTP Method: 
* Ensure that you are using the correct HTTP method in your form and route. In your code, you've defined the login route to accept GET requests  (methods=['GET']), which matches your form's method (method='GET')

# Browser Cache:
* Sometimes, browsers can cache responses. Try clearing your browser cache or opening the application in an incognito/private window to rule out any caching issues.

# Server Restart:
  * If you make changes to your Flask code (appname.py), make sure to restart the Flask server to apply the changes.








# Django Overview
# Step 1: Django Project Setup

  # 1. Install Django:
  * Make sure you have Django installed. You can install it using the following command:
  * pip install django
  
  # 2. Create a New Django Project:
  * Once Django is installed, create a new Django project using:
  * django-admin startproject myproject
  * This will create a directory structure for your Django project with the following key files:
  
  * manage.py: Command-line utility to interact with Django.
  * myproject/settings.py: Contains project settings.
  * myproject/urls.py: Root URL configuration.
  * myproject/wsgi.py & myproject/asgi.py: Interfaces for deploying Django.
    
  # 3. Start the Development Server:
  * Move into your project directory and start the development server:
  * cd myproject
  * python manage.py runserver
  * You can view the project at http://127.0.0.1:8000.

# Step 2: Django App Creation
  # 1. Create an App:
  * In Django, apps are components of a project. Let’s create an app named blog:
  * python manage.py startapp blog
  
  # 2. Add the App to Installed Apps:
  * In the settings.py file, add the new app to the INSTALLED_APPS section:
  
        python code
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'blog',  # Add your app here
        ]

# Step 3: Setting Up URLs
  # 1. Define a URL in App:
  * In the blog app, create a urls.py file (if it doesn’t exist) and define a URL pattern:
  
      * python code
      * blog/urls.py
        from django.urls import path
        from . import views
        
        urlpatterns = [
            path('', views.home, name='home'),
        ]
  # 2. Include App URLs in the Project:
  * Next, in the main myproject/urls.py, include the blog app’s URLs:
  
     * python code
     * myproject/urls.py
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('blog.urls')),  # Include blog app URLs
        ]
# Step 4: Views (Basic Views)
  # 1. Create a View Function:
  * In views.py of your blog app, create a simple view function:
  
     * python code
     * blog/views.py
     from django.http import HttpResponse
     
     def home(request):
         return HttpResponse("Hello, Django! This is the home page.")
  # 2. Running the Project:
  * Once the view is defined and URLs are configured, run the development server:
  
      bash code
      python manage.py runserver
      You can view the homepage by visiting http://127.0.0.1:8000/.
      
  # Step 5: Templates
  * 1. Create a Template Folder:
  * In your blog app, create a folder named templates and inside it create another folder blog (to match the app name). Inside this folder, create an HTML file home.html:
  
       * html code
       <!-- blog/templates/blog/home.html -->
       <!DOCTYPE html>
       <html>
       <head>
           <title>Home Page</title>
       </head>
       <body>
           <h1>Welcome to My Django Blog</h1>
       </body>
       </html>
  # 2. Modify View to Render Template:
  * In the views.py file, modify the view to render this template:
  
        * python code
        * blog/views.py
          from django.shortcuts import render
          
          def home(request):
              return render(request, 'blog/home.html')
  # 3. Configure Templates in Settings:
  * Make sure the TEMPLATES setting in settings.py includes the following:
  
       python code
       TEMPLATES = [
           {
               'BACKEND': 'django.template.backends.django.DjangoTemplates',
               'DIRS': [],  # You can specify additional directories here
               'APP_DIRS': True,
               'OPTIONS': {
                   'context_processors': [
                       'django.template.context_processors.debug',
                       'django.template.context_processors.request',
                       'django.contrib.auth.context_processors.auth',
                       'django.contrib.messages.context_processors.messages',
                   ],
               },
           },
       ]
     Now, if you visit http://127.0.0.1:8000/, the home.html template will be displayed.

# Step 6: Django Models
1. Define a Model:
Models represent the database structure. Let’s create a simple Post model in models.py:

      python code
      blog/models.py
      from django.db import models
      
      class Post(models.Model):
          title = models.CharField(max_length=100)
          content = models.TextField()
          created_at = models.DateTimeField(auto_now_add=True)
      
          def __str__(self):
              return self.title
2. Migrate the Model to the Database:
Run the following commands to apply the model changes:

bash code
python manage.py makemigrations
python manage.py migrate
3. Register the Model in Admin:
To manage the Post model via Django Admin, register it in admin.py:

     python code
     #log/admin.py
     from django.contrib import admin
     from .models import Post
     
     admin.site.register(Post)
Now you can access the Post model in the admin interface at http://127.0.0.1:8000/admin/.

Step 7: Django Admin
1. Create Superuser for Admin Access:
To access the admin panel, create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the instructions and provide a username, email, and password.

2. Admin Interface:
Visit http://127.0.0.1:8000/admin/ and log in using the superuser credentials. You will see the Post model listed, and you can add, edit, and delete posts from there.

Step 8: Displaying Data from the Database
1. Query Data in the View:
Modify the view to query data from the Post model and pass it to the template:

    python code
    #blog/views.py
    from .models import Post
    
    def home(request):
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})
2. Display Data in the Template:
Update the home.html template to loop through the posts and display them:

     htmL code
     <!-- blog/templates/blog/home.html -->
     <!DOCTYPE html>
     <html>
     <head>
         <title>Home Page</title>
     </head>
     <body>
         <h1>Welcome to My Django Blog</h1>
         <ul>
             {% for post in posts %}
             <li>
                 <h2>{{ post.title }}</h2>
                 <p>{{ post.content }}</p>
                 <small>{{ post.created_at }}</small>
             </li>
             {% endfor %}
         </ul>
     </body>
     </html>
Now, the posts from the database will be displayed on the homepage.

We have covered:

Django installation and project setup.
Creating a Django app.
Setting up URLs and views.
Working with templates.
Defining and using models.
Using the Django admin interface.
Querying and displaying data from the database.



project of django
Ecommerce website
Admision form
Movie reccomendation website
Book website
Paggination projct of news artical
lawyer website

