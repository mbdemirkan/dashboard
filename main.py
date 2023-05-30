from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type": "application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response.json())

echo_url = "https://postman-echo.com/post"
echo_url = "https://postman-echo.com/server-events/2"  # postman-echo.com/server-events/:numberOfEvents # numberOfEvents = default 10
todo = {"event": "message", "request": "POST"}
response = requests.post(echo_url, data=json.dumps(todo), headers=headers)
print(response.content)


@app.route("/")
def hello():
    ad = "ad"  # burada ise url’imize gönderdiğimiz parametreleri çektik.
    soyad = "soyad"
    return render_template("index.html", ad=ad, soyad=soyad)
    #  return "Hello World"


if __name__ == "__main__":  # There is an error on this line
    app.run(debug=True, host='0.0.0.0')
    #  print("test")
