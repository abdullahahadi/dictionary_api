from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word:str):
    try:
        
        df = pd.read_csv("dictionary.csv")
        definition = df.loc[df["word"] == word]["definition"].iloc[0]

        result_dictionary = {
            "word": word,
            "definition": definition,
            }
        return jsonify(result_dictionary)

    except IndexError as e:
        return jsonify({
            "status":"error",
            "message" :f"word {word} not found"})


if __name__ == "__main__":
    app.run(debug=True)
