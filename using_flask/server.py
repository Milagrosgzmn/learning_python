from flask import Flask, make_response, request, Response

from module_data import data
app = Flask(__name__)

@app.route("/")
def index():
    """ This is just returns a typical string"""
    return ({"message":"hello world"}, 200)

@app.route('/no_content')
def no_content():
    """ Returns 'no content' in a json with explicit status code in tuple"""
    return({"message":'No content found'}, 204)

@app.route('/exp')
def index_explicit():
    """ Returns a message created with the method make_response an sets status code"""
    res = make_response({"message":'This is an answer with an explicit status code'})
    res.status_code = 200

    return res

@app.route("/data")
def get_data():
    """ If data, then notifies length """
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

@app.route('/name_search')
def name_search():
    """ Searches by query, returns person """
    query = request.args.get('q')

    if not query:
        return ({"message":'missing information'}, 422)
    
    for person in data:
        if query.lower() in person['first_name'].lower():
            return person

    return ({"message": "person not found"}, 404)

@app.route("/count")
def count():
    """ Returns number of persons in data """
    try:
        return ({"data count": len(data)}, 200)
    except NameError:
        return ({"message": "data not defined"}, 500)

@app.route('/person/<uuid:uuid>')
def find_by_uuid(uuid):
    """ Given uuid, returns person """
    try:
        for person in data:
            if str(uuid) == person['id']:
                return person
        return ({"message":"Person not found"}, 404)
    except:
        return ({"message": "data not defined"}, 500)

@app.route('/person/<uuid:uuid>', methods =['DELETE'])
def delete_by_uuid(uuid):
    """ Deletes person given uuid """
    try:
        for i,person in enumerate(data):
            if str(uuid) == person['id']:
                del data[i]
                return ({"message":uuid}, 200)
        return ({"message":"Person not found"}, 404)
    except:
        return ({"message": "data not defined"}, 500)

@app.route('/person', methods = ['POST'])
def add_by_uuid():
    """ Receives an obj by body and adds it to data """
    new_person = request.json
    if not new_person:
        return ({"message": "Invalid input parameter"}, 422)
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200

@app.errorhandler(404)
def api_not_found(error):
    """ Handles not defined routes """
    return ({'message':'API not found'}, 404)
