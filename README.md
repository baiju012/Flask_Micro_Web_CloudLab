# Cloud_1

<img src =https://github.com/baiju012/Cloud_1/assets/111991510/dae83c43-2512-4820-9eb4-f1f648c46c77 >


## If You are facing error like "not found", "Not responding" 

# Server is Runnings
* Confirm that your Flask server (get.py) is running. When you run python get.py
# Check The URL:
* Check the URL:  you're accessing the correct URL in your browser. In your code, you're defining the route as /login
* make sure you're trying to access http://127.0.0.1:5000/login

 # Port and Host:
 * Verify that the host and port in your HTML form match the Flask server configuration. In your HTML form
you have specified action="http://127.0.0.1:5000/login", which should match the host and port where your Flask app is running

# Correct HTTP Method: 
* Ensure that you are using the correct HTTP method in your form and route. In your code, you've defined the login route to accept GET requests  (methods=['GET']), which matches your form's method (method='GET')

# Browser Cache:
* Sometimes, browsers can cache responses. Try clearing your browser cache or opening the application in an incognito/private window to rule out any caching issues.


  # Server Restart:
  * If you make changes to your Flask code (get.py), make sure to restart the Flask server to apply the changes.
