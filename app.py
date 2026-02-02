from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []

@app.route("/", methods=["GET", "POST"])
def index():
    global books

    # KİTAP EKLE
    if request.method == "POST":
        name = request.form.get("name")
        author = request.form.get("author")
        year = request.form.get("year")

        books.append({
            "name": name,
            "author": author,
            "year": year
        })

        return redirect(url_for("index"))

    # KİTAP ARA
    query = request.args.get("q")
    search_type = request.args.get("type")

    filtered_books = books

    if query and search_type:
        filtered_books = [
            book for book in books
            if query.lower() in book[search_type].lower()
        ]

    return render_template("index.html", books=filtered_books)


@app.route("/delete/<int:index>")
def delete_book(index):
    if 0 <= index < len(books):
        books.pop(index)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

