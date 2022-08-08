from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def budget_greeting():
   message = "Hello, Saver!"
   return message

@app.route('/form')
def budget_input_form():
   return render_template("personal_budg_form.html")

@app.route('/results', methods=["POST"])
def budget_input_results():
   ann_income = request.form['ann_income']
   housing_cost = request.form['housing_cost']
   car_pay = request.form['car_pay']
   insur_pay = request.form['insur_pay']
   return render_template("personal_budg_results.html", ann_income = ann_income, housing_cost = housing_cost, car_pay = car_pay, insur_pay = insur_pay)

if __name__ == '__main__':
   app.run()