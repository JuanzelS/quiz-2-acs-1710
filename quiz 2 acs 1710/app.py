from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/character")
def character():
    # Get character ID from the form
    character_id = request.args.get("character_id")

    if not character_id:
        return "Character ID is required!", 400

    # Build SWAPI URL
    url = f"https://swapi.py4e.com/api/people/{character_id}/"

    # Fetch data from SWAPI
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        return f"Error: Unable to fetch character data. Status Code {response.status_code}", 400

    # Extract relevant fields
    character_info = {
        "name": data.get("name"),
        "height": data.get("height"),
        "mass": data.get("mass"),
        "hair_color": data.get("hair_color"),
        "eye_color": data.get("eye_color"),
    }

    return render_template("character.html", character=character_info)

if __name__ == "__main__":
    app.run(debug=True)
