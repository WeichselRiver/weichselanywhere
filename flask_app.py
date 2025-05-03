# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import csv

app = Flask(__name__)

with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

@app.route('/')
def hello_world():
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rows = []
        for row in spamreader:
            rows.append(', '.join(row))
    return render_template("index.html", test = rows)

if __name__ == "__main__":
    app.run(debug=True)
