from flask import Flask, render_template, jsonify

app = Flask(__name__)

tasks_type = ["red, orange, yellow, green, blue, purple"]
tasks = [
  {
    'id': 1,
    'title': 'Mates',
    'Description': 'p123 1,2,3',
    'fecha': '23/02/2023'
  },
  {
    'id': 2,
    'title': 'TDR',
    'Description': 'Index',
    'fecha': '28/02/2023'
  },
  {
    'id': 3,
    'title': 'Tecno',
    'Description': 'questions 1,2,3',
    'fecha': '1/03/2023'
  },
  {
    'id': 3,
    'title': 'Tecno',
    'Description': 'questions 1,2,3',
    'fecha': '1/03/2023'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', tasks=tasks)


@app.route("/api/tasks")
def tasks_api():
  return jsonify(tasks)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
