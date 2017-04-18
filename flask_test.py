# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()



from flask import Flask
import random

app = Flask(__name__)

greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

@app.route('/hello')
def hello():
  greeting = random.choice(greets) + ", " + random.choice(places)
  return greeting + "\n"

if __name__ == '__main__':
  app.run()