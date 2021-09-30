# CloudSek Project

**Components:**

1. Redis : Message Broker
2. Django-q : Task Queue
3. WebApp : Django App for the API's requested
4. Docker Images:
   - redis:alpine : Redis Image
   - kiranbc050/cloudsekproj-web-app:0.0.1 : Web App Image
   - kiranbc050/cloudsekproj-django-q:0.0.1 : Django Q Image

**Usage:**

1. clone the github repo
2. Run the docker-compose.yml file
3. Tests:
   - Examples:
     - GET http://127.0.0.1:8000/
     - GET http://127.0.0.1:8000/calculate/10/9
     - GET http://127.0.0.1:8000/get_answer/28
