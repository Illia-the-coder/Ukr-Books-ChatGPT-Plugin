import json
import quart
import quart_cors
from quart import request
import json
from quart import Quart, render_template
from LiteratureClient import DB

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/list_all/<string:grade>/<string:type>")
async def list_all(grade, type):
    db = DB(grade, type)
    all_books = {'list all':db.list_all()}
    # all_books.['Main web-site view']=f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grades'
    return quart.Response(response=json.dumps(all_books), mimetype="application/json", status=200)

@app.post("/get_books/<string:grade>/<string:type>")
async def get_books(grade, type):
    db = DB(grade, type)
    books = db.list_all()
    return quart.Response(response=json.dumps(books), mimetype="application/json", status=200)

@app.post("/get_presentation/<string:grade>/<string:type>")
async def get_presentation(grade, type):
    db = DB(grade, type)
    presentation = db.get_presentation()
    return quart.Response(response=json.dumps(presentation), mimetype="application/json", status=200)

@app.post("/get_bio/<string:grade>/<string:type>/<string:author>")
async def get_bio(grade, type, author):
    db = DB(grade, type)
    bio = db.get_bio(author)
    print(bio)
    return quart.Response(response=json.dumps(bio), mimetype="application/json", status=200)

@app.post("/get_content/<string:grade>/<string:type>/<string:author>/<string:name>")
async def get_content(grade, type, author, name):
    db = DB(grade, type)
    content = db.get_content(author, name)
    return quart.Response(response=json.dumps(content), mimetype="application/json", status=200)

@app.post("/get_rnd/<string:grade>/<string:type>")
async def get_rnd(grade, type):
    db = DB(grade, type)
    rnd = db.get_rnd()
    return quart.Response(response=json.dumps(rnd), mimetype="application/json", status=200)

@app.get("/logo.jpg")
async def plugin_logo():
    filename = 'logo.jpg'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(response=text, mimetype="application/json", status=200)

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(response=text, mimetype="text/yaml", status=200)

@app.route('/legal', methods=['GET'])
async def legal():
    return await render_template('LEGAL.html')



def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
