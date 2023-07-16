import json
from quart import Quart, jsonify, send_file
import quart_cors
from LiteratureClient import DB

app = quart_cors.cors(
    Quart(__name__), allow_origin="https://chat.openai.com"
)

@app.route("/list_all/<string:grade>/<string:type>", methods=["POST"])
async def list_all(grade, type):
    db = DB(grade, type)
    all_books = {'list all': db.list_all()}
    all_books['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade'
    all_books['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade'
    return jsonify(all_books)

@app.route("/get_books/<string:grade>/<string:type>/<string:author>/", methods=["POST"])
async def get_books(grade, type, author):
    db = DB(grade, type)
    books = {'books': db.get_books(author)}
    index = db.authors.index(author)
    books['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    books['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    return jsonify(books)

@app.route("/get_presentation/<string:grade>/<string:type>", methods=["POST"])
async def get_presentation(grade, type):
    db = DB(grade, type)
    presentation = db.get_presentation()
    presentation['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/pres'
    presentation['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/pres'
    return jsonify(presentation)

@app.route("/get_bio/<string:grade>/<string:type>/<string:author>", methods=["POST"])
async def get_bio(grade, type, author):
    db = DB(grade, type)
    bio = db.get_bio(author)
    index = db.authors.index(author)
    bio['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    bio['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    return jsonify(bio)

@app.route("/get_content/<string:grade>/<string:type>/<string:author>/<string:name>", methods=["POST"])
async def get_content(grade, type, author, name):
    db = DB(grade, type)
    content = db.get_content(author, name)
    index = db.authors.index(author)
    book_index = db.get_books(author).index(name)
    content['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    content['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    return jsonify(content)

@app.route("/get_rnd/<string:grade>/<string:type>", methods=["POST"])
async def get_rnd(grade, type):
    db = DB(grade, type)
    rnd = db.get_rnd()
    index = db.authors.index(db.rnd_auth)
    book_index = db.get_books(db.rnd_auth).index(db.rnd_book)
    rnd['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    rnd['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    return jsonify(rnd)

@app.route("/logo.jpg", methods=["GET"])
async def plugin_logo():
    filename = 'logo.jpg'
    return await send_file(filename, mimetype='image/png')

@app.route("/.well-known/ai-plugin.json", methods=["GET"])
async def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
    return text, 200, {"Content-Type": "application/json"}

@app.route("/openapi.yaml", methods=["GET"])
async def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
    return text, 200, {"Content-Type": "text/yaml"}

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
