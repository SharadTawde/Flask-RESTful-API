from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def _root():
    """
    root dir of server
    :return:str
    """
    return "This is root"


@app.route('/user')
def user_info():
    """
    get data from GET request and check length
    :return:json
    """
    json = request.get_json()
    if len(json['name']) == 0:
        return "Invalid name"
    return jsonify(json['name'])


@app.route('/user/<name>')
def user_name(name):
    """
    :param name:
    :return:
    """
    return jsonify(name)


@app.route('/save', methods=['POST'])
def save_note():
    """
    get data from POST method and return json response
    :return:json
    """
    json = request.get_json()
    title = json['title']
    disc = json['description']
    response = {
        "status": "success",
        "message": "note added successfully",
        "Your note": "" + title + " : " + disc
    }
    return jsonify(response)


# running in local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
