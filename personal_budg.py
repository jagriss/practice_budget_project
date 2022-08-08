from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def budget_greeting():
   message = "Hello, Saver!"
   return message

@app.route('/form')
def budget_input():
   message = "Hello, Saver!"
   return render_template("personal_budg_form.html")

if __name__ == '__main__':
   app.run()