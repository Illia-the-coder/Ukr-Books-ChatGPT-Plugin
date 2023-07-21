import os
import json
import quart
import quart_cors
from LiteratureClient import DB
from quart import request
from quart import redirect
import csv
import datetime

app = quart_cors.cors(
    quart.Quart(__name__), allow_origin="https://chat.openai.com"
)

# Define the CSV file path
CSV_FILE_PATH = "requests_log.csv"

def create_csv_file():
    header = ["Timestamp", "Request Type", "Parameters"]
    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def save_request_to_csv(request_type, params):
    now = datetime.datetime.now().isoformat()
    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([now, request_type, json.dumps(params)])

# Check if the CSV file exists, and create it if not
if not os.path.exists(CSV_FILE_PATH):
    create_csv_file()

@app.route("/list_all/<string:grade>/<string:type>", methods=["POST"])
async def list_all(grade, type):
    db = DB(grade, type)
    all_books = {'list all': db.list_all()}
    all_books['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade'
    all_books['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade'
    
    # Log the request to CSV
    save_request_to_csv("list_all", {"grade": grade, "type": type})
    
    return quart.Response(response=json.dumps(all_books), status=200)

@app.route("/get_books/<string:grade>/<string:type>/<string:author>/", methods=["POST"])
async def get_books(grade, type, author):
    db = DB(grade, type)
    books = {'books': db.get_books(author)}
    index = db.authors.index(author)
    books['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    books['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    
    # Log the request to CSV
    save_request_to_csv("get_books", {"grade": grade, "type": type, "author": author})
    
    return quart.Response(response=json.dumps(books), status=200)

@app.route("/get_presentation/<string:grade>/<string:type>", methods=["POST"])
async def get_presentation(grade, type):
    db = DB(grade, type)
    presentation = db.get_presentation()
    presentation['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/pres'
    presentation['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/pres'
    
    # Log the request to CSV
    save_request_to_csv("get_presentation", {"grade": grade, "type": type})
    
    return quart.Response(response=json.dumps(presentation), status=200)

@app.route("/get_bio/<string:grade>/<string:type>/<string:author>", methods=["POST"])
async def get_bio(grade, type, author):
    db = DB(grade, type)
    bio = db.get_bio(author)
    index = db.authors.index(author)
    bio['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    bio['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}'
    
    # Log the request to CSV
    save_request_to_csv("get_bio", {"grade": grade, "type": type, "author": author})
    
    return quart.Response(response=json.dumps(bio), status=200)

@app.route("/get_content/<string:grade>/<string:type>/<string:author>/<string:name>", methods=["POST"])
async def get_content(grade, type, author, name):
    db = DB(grade, type)
    content = db.get_content(author, name)
    index = db.authors.index(author)
    book_index = db.get_books(author).index(name)
    content['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    content['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    
    # Log the request to CSV
    save_request_to_csv("get_content", {"grade": grade, "type": type, "author": author, "name": name})
    
    return quart.Response(response=json.dumps(content), status=200)

@app.route("/get_rnd/<string:grade>/<string:type>", methods=["POST"])
async def get_rnd(grade, type):
    db = DB(grade, type)
    rnd = db.get_rnd()
    index = db.authors.index(db.rnd_auth)
    book_index = db.get_books(db.rnd_auth).index(db.rnd_book)
    rnd['Main web-site view eng'] = f'https://translate.google.com/translate?sl=uk&tl=en&u=https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    rnd['Main web-site view ukr'] = f'https://literature2.illia56.repl.co/{("ukr" if "ukr" in type else "for")}/{grade}_grade/auth_ind={index}/book_ind={book_index}'
    
    # Log the request to CSV
    save_request_to_csv("get_rnd", {"grade": grade, "type": type})
    
    return quart.Response(response=json.dumps(rnd), status=200)

@app.route("/logo.jpg", methods=["GET"])
async def plugin_logo():
    return redirect('https://res.cloudinary.com/dw8hy0djm/image/upload/v1689848999/zssvobkk1ziqj81fme3x.jpg')

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
