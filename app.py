from flask import Flask, render_template, request

app = Flask(__name__)

feedback_list = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        if name and message:
            feedback_list.append({
                "name": name,
                "message": message
            })

    return render_template("index.html", feedbacks=feedback_list)

@app.route("/health")
def health():
    return "Application is healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)