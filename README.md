# Notes 

# Pre-Requisite

pip/python/python3 install -r requirements.txt
 
Once requirements are installed, please run the following commands.

python/python3 manage.py makemigrations
python/python3 manage.py migrate
python/python3 manage.py runserver


# Requirements

Django==3.2.10
djangorestframework==3.12.4

# Testing

-------------------------------------------------------------

To Create: 

Set the request type to POST.
Set the URL to "http://{#url}/api/notes/"
Set the request body to JSON with the note data 
{
    "title": "New Note",
    "content": "This is the content of the first note."
}

-------------------------------------------------------------

To Show All notes: 

Set the request type to GET.
Set the URL to "http://{#url}/api/notes/"

-------------------------------------------------------------

To Show note by an ID: 

Set the request type to GET.
Set the URL to "http://{#url}/api/notes/{id}"
Example: "http://{#url}/api/notes/1"

-------------------------------------------------------------

To Update note: 

Set the request type to PUT.
Set the URL to "http://{#url}/api/notes/{id}/"
Example: "http://{#url}/api/notes/1/"

-------------------------------------------------------------

To Delete note: 

Set the request type to DELETE.
Set the URL to "http://{#url}/api/notes/{id}/"
Example: "http://{#url}/api/notes/4/"

-------------------------------------------------------------
