from flask import Flask, render_template
app = Flask(__name__)

import datetime                                                                                                                
                                                                                                                                  
@app.route('/')
def index():
    return render_template("index.html", server_time = datetime.datetime.now())
if __name__ == '__main__':
    app.run()
