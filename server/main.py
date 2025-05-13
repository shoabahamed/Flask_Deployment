from flask import Flask, send_from_directory, request
from flask_cors import CORS
from dotenv import load_dotenv
import os 
import cloudinary
from cloudinary.uploader import upload
from flask.json import jsonify

load_dotenv()


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 300 * 1024 * 1024  # ✅ Allow 50MB file uploads


app.secret_key = os.getenv("APP_SECRET")


cloudinary.config( 
    cloud_name = "dx9gej2lc", 
    api_key = "988347957788346", 
    api_secret = os.getenv("CLOUDNARY_API_SECRET_KEY"),
    secure=True
)


# sets the cors policy for the files in the static folder
CORS(app, resources={r"/server/static/*": {"origins": "*"}})


@app.route('/')
def index():
    return "<h1>Hello World</h1>"




# runs the server on port 5000
if __name__ == "__main__":
    if(os.getenv("DEPOLY_PRODUCTION").lower() == 'true'):
        print("launching server in production mode")
        app.run(debug=False)
    else:
        print("launching server in development mode")
        app.run(debug=True, port=5000)
