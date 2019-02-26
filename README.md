This microservice can be deployed as a Python Flask app either locally or on a server. It is 
currently deployed via Heroku at - https://ritvika-pig-latin-translator.herokuapp.com/pig-latin-translator/


A GET request can be sent to the mentioned url with the required text passed as a value enclosed 
in single or double quotes to the 'string' key. For example:

- `https://ritvika-pig-latin-translator.herokuapp.com/pig-latin-translator?string='Hello, my name 
is Ritvika!'`

To install it locally, make sure your machine has Python 3 installed. Go ahead and install the required packages:
- `pip install -r requirements.txt`

To run the app locally, run the app.py file as follows:
- `python app.py`
- The app should be running locally at http://127.0.0.1:5000/pig-latin-translator/


