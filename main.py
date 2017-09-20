from flask import Flask, request
from caeser import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form="""

<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px;
                width: 540px;
                height: 120px:
            }
        </style>
    </head>
    <body>
         <form  method="post">
            <label for="rot">Rotate by:  </label >
            <input type="text" name="rot" placeholder="0"  />
            
            <textarea name="textarea">
            </textarea>
            
              <input type="submit" />
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
   return form

@app.route('/' ,methods=['POST'])
def encrypt():  
   rotate = request.form['rot']
   rotate = int(rotate)
   text = request.form['textarea']
   rotated = rotate_string(text, rotate)
   return rotated
app.run()