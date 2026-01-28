from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()

    if "career" in user_message:
        reply = "Feeling anxious about career is very common. Try focusing on one small skill at a time. You are not late."
    elif "anxious" in user_message or "stress" in user_message:
        reply = "I’m sorry you’re feeling anxious. Take a deep breath. You are doing your best."
    elif "sad" in user_message:
        reply = "It’s okay to feel sad sometimes. You don’t have to handle everything alone."
    else:
        reply = "I’m here to listen. Please tell me more about how you feel."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)