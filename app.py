from flask import Flask, render_template, jsonify, request
from ai_model import get_answer
import sqlite3
from speech import listen_live
from summarize import get_summary
from tts import speak
from database import init_db, save_note, get_notes
from flask import request, jsonify

app = Flask(__name__)

init_db()  # create database

@app.route('/')
def home():
    return render_template("index.html")

def get_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    conn.close()
    return notes


@app.route('/record', methods=['POST'])
def record():
    data = request.get_json()
    text = data['text']

    summary = get_summary(text)

    # SAVE INTO DATABASE
    save_note(text, summary)

    return jsonify({
        "original": text,
        "summary": summary
    })

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['text']

    answer = get_answer(question)

    return jsonify({"answer": answer})

@app.route('/dashboard')
def dashboard():
    notes = get_notes()
    return render_template("dashboard.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)