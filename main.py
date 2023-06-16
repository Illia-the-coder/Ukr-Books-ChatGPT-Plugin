import json
import quart
import quart_cors
from quart import request
from quart import jsonify

from LiteratureClient import DB

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/list_all/<string:grade>/<string:type>")
async def list_all(grade, type):
    db = DB(grade, type)
    all_books = db.list_all()
    return jsonify(all_books)
@app.post("/get_books/<string:grade>/<string:type>")
async def get_books(grade, type):
    db = DB(grade, type)
    books = db.list_all()
    return jsonify(books)

@app.post("/get_presentation/<string:grade>/<string:type>")
async def get_presentation(grade, type):
    db = DB(grade, type)
    presentation = db.get_presentation()
    return jsonify(presentation)

@app.post("/get_bio/<string:grade>/<string:type>/<string:author>")
async def get_bio(grade, type, author):
    db = DB(grade, type)
    bio = db.get_bio(author)
    return jsonify(bio)

@app.post("/get_content/<string:grade>/<string:type>/<string:author>/<string:name>")
async def get_content(grade, type, author, name):
    db = DB(grade, type)
    content = db.get_content(author, name)
    return jsonify(content)

@app.post("/get_rnd/<string:grade>/<string:type>")
async def get_rnd(grade, type):
    db = DB(grade, type)
    rnd = db.get_rnd()
    return jsonify(rnd)

@app.post("/get_adding/<string:grade>/<string:type>/<string:command>")
async def get_adding(grade, type, command):
    db = DB(grade, type)
    adding = db.get_adding(command)
    return jsonify(adding)

@app.get("/logo.jpg")
async def plugin_logo():
    filename = 'logo.jpg'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
