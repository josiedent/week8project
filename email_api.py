import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox8ce6c77a3af84126941dd3cfb1b53bb9.mailgun.org/messages",
        auth=("api", "1969f491b0bc1955278edacc8aa9ac2b-9525e19d-76f85060"),
        data={"from": "Excited User <mailgun@sandbox8ce6c77a3af84126941dd3cfb1b53bb9.mailgun.org>",
              "to": ["josiedent@hotmail.co.uk"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

from flask import Flask, render_template, request

app = Flask("MyApp", methods=["POST"])
@app.route("/")
def index():
    return render_template("index.html", name=name.title())
    form_data = request.form
    print send_simple_message()

app.run(debug=True)
