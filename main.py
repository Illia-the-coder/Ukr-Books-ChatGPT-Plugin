import json
import quart
import quart_cors
from quart import request
import json
from quart import Quart, render_template, redirect
from LiteratureClient import DB

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.route("/list_all/<string:grade>/<string:type>", methods=["POST"])
async def list_all(grade, type):
    db = DB(grade, type)
    all_books = {'list all': db.list_all()}
    all_books['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade'
    all_books['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade'
    return quart.jsonify(all_books)

@app.route("/get_books/<string:grade>/<string:type>/<string:author>/", methods=["POST"])
async def get_books(grade, type, author):
    db = DB(grade, type)
    books = {'books': db.get_books(author)}
    index = db.authors.index(author)
    books['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    books['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    return quart.jsonify(books)

@app.route("/get_presentation/<string:grade>/<string:type>", methods=["POST"])
async def get_presentation(grade, type):
    db = DB(grade, type)
    presentation = db.get_presentation()
    presentation['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/pres'
    presentation['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/pres'
    return quart.jsonify(presentation)

@app.route("/get_bio/<string:grade>/<string:type>/<string:author>", methods=["POST"])
async def get_bio(grade, type, author):
    db = DB(grade, type)
    bio = db.get_bio(author)
    index = db.authors.index(author)
    bio['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    bio['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    return quart.jsonify(bio)

@app.route("/get_content/<string:grade>/<string:type>/<string:author>/<string:name>", methods=["POST"])
async def get_content(grade, type, author, name):
    db = DB(grade, type)
    content = db.get_content(author, name)
    index = db.authors.index(author)
    book_index = db.get_books(author).index(name)
    content['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    content['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    return quart.jsonify(content)

@app.route("/get_rnd/<string:grade>/<string:type>", methods=["POST"])
async def get_rnd(grade, type):
    db = DB(grade, type)
    rnd = db.get_rnd()
    index = db.authors.index(DB.rnd_auth)
    book_index = db.get_books(author).index(DB.rnd_book)
    rnd['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    rnd['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    return quart.jsonify(rnd)

@app.route("/logo.jpg", methods=["GET"])
async def plugin_logo():
    filename = 'logo.jpg'
    return await quart.send_file(filename, mimetype='image/png')

@app.route("/.well-known/ai-plugin.json", methods=["GET"])
async def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
    return quart.Response(response=text, mimetype="application/json", status=200)

@app.route("/openapi.yaml", methods=["GET"])
async def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
    return quart.Response(response=text, mimetype="text/yaml", status=200)

# @app.route('/legal', methods=['GET'])
# async def legal():
#     return await quart.render_template('LEGAL.html', status=200)

# @app.route('/')
# async def home():
#     return quart.redirect("https://butter-tangerine-f7b.notion.site/Ukr-Books-ChatGPT-ad1258cbc91b40e5ad78fa89f414dc09?pvs=4", status=200)

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
