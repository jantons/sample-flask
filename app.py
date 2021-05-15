import os
import boto3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:25060/{}?ssl-mode=REQUIRED'.format(
   os.getenv('DB_USER'),
   os.getenv('DB_PASSWORD'),
   os.getenv('DB_HOST'),
   os.getenv('DB_NAME')
)

db = SQLAlchemy(app)

# Database table
class Verification(db.Model):
    id_user = db.Column(db.Integer, unique=True, primary_key=True)
    email_address = db.Column(db.String(80))
    image_path = db.Column(db.String(200))
    checked = db.Column(db.Boolean)
    saved = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime)


    def __repr__(self):
        return '<User {}>'.format(self.email_address)


db.create_all()

#session = boto3.session.Session()
#client = session.client('s3',
#                        region_name=os.getenv('SPACES_REGION'),
#                        endpoint_url=os.getenv('SPACES_URL'),
#                        aws_access_key_id=os.getenv('SPACES_KEY'),
#                        aws_secret_access_key=os.getenv('SPACES_SECRET'))

#file = request.files['filefield']
#conn.upload_fileobj(file, 'mybucket', 'mykey')

#app.route('/upload', methods=['GET', 'POST'])
#def upload():
#    try:
#        latestfile = request.form.get('filetoupload')
#        conn = boto3.client('s3', region_name="eu-west-1", endpoint_url="example.com", aws_access_key_id='the access key here', aws_secret_access_key='the secret key here',)
#        conn.create_bucket(Bucket="mytestbucket22")
#        bucket_name = "mytestbucket22"
#        conn.upload_file(latestfile, bucket_name, latestfile)
#        return render_template('dashboard.html', name=current_user.username, sumsg="Upload done!")
#    except Exception as ermsg:
#        print(ermsg)
#        return render_template('dashboard.html', name=current_user.username, ermsg=ermsg)


@app.route("/")
def hello_world():
    return render_template("index.html")
