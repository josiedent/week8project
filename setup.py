from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route("/process", methods = ["GET", "POST"] )
def process_form():
    #checked = request.form.getlist('option')
    #checked=request.form['radio1']
    #with open('1.txt','w') as file:
        #file.write("%s"%checked)
    # do something with checked array
    #return checked
    if request.method == 'GET':
        return 'hi'
    elif request.method == 'POST':
        temp = request.form['radio1']
        location = request.form['radio2']
        category = request.form['radio3']
        destinations = find_destinations(temp, location, category)
        if destinations:
            for dest in destinations:
                return dest.name
        else:
            return "No destinations found"

class Destination(object):

    def __init__(self, place, temp, location, category):
        self.place = place
        self.temp = temp #get_temp(name)
        self.location = location
        self.category = category

    #def get_temp(name):
        # has to go to the api and get the temperature
        #if temp > 20:
            #return "hot"

places = [Destination("Berlin", "Steaming", "Europe", "City"),
          Destination("London", "Chilly", "Europe", "City")]

def is_it_a_match(place, temp, location, category):
    return place.temp == temp
    return place.location == location
    return place.category == category

def find_destinations(temp, location, category):
    destinations = [place.name for place in places if is_it_a_match(place, temp, location, category)]
    return destinations



if __name__ == '__main__':
   app.run(debug = True)
