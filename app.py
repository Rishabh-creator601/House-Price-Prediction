from flask import Flask ,redirect,url_for,request,render_template
import pickle 







app = Flask(__name__,template_folder='template')

@app.route("/")
def home():

	return render_template("login.html")

@app.route("/model",methods=['POST','GET'])
def model():

	cities = pickle.load(open("city.pkl","rb"))


 
	if request.method == 'POST':
		name=  request.form['username']
		return render_template("model_file.html",data=list(cities.keys()),username=name)
	else:

		name=request.form.get("username")
		return render_template("model_file.html",data=list(cities.keys()),username=name)

	return render_template("model_file.html",data=list(cities.keys()))


	


@app.route("/predict",methods=['POST','GET'])
def predict():

	cities = pickle.load(open("city.pkl","rb"))
	model =pickle.load(open("model.pkl","rb"))

	if request.method == 'POST':
		floors  = int(request.form['floors'])
		bedrooms  = int(request.form['bedrooms'])
		bathrooms  = int(request.form['bathrooms'])
		condition_house  = int(request.form['condition'])
		sqft_living  = int(request.form['sqft_living'])
		sqft_above  = int(request.form['sqft_above'])
		sqft_lot  = int(request.form['sqft_lot'])
		city = str(request.form.get('city'))
		city_new = cities[city]

		features  = [bedrooms,bathrooms,sqft_living,sqft_lot,floors,condition_house,sqft_above,city_new]


		prediction = model.predict([features])
		statement  = "The Average Price of house in {} would be ${}".format(city,prediction[0])

		return render_template("model_file.html",data=list(cities.keys()),pred=statement)


	return render_template("model_file.html",data=list(cities.keys()))

	    


	




if __name__ == "__main__":
	app.run(debug=True)