from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


def read_csv_file():
    products = []
    with open("products.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def read_sql_file():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            data = read_json_file()
        elif source == "csv":
            data = read_csv_file()
        elif source == "sql":
            data = read_sql_file()
        else:
            return render_template(
                "product_display.html",
                products=[],
                error="Wrong source"
            )
    except Exception:
        return render_template(
            "product_display.html",
            products=[],
            error="Database error"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

        filtered_products = [product for product in data if product["id"] == product_id]

        if not filtered_products:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

        data = filtered_products

    return render_template(
        "product_display.html",
        products=data,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)