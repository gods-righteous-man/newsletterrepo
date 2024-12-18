from flask import Flask, request, jsonify
from  models import add_subscribers, get_subscribers, log_newsletter, get_newsletters
from email_service import send_email_to_subscribers

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to our Newsletter Backend"


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400
    result = add_subscribers(email)
    return jsonify(result)

@app.route('/subscribers', methods=['GET'])
def subscribers():
    result = get_subscribers()
    return jsonify(result)

@app.route('/log-newsletter', methods=['POST'])
def log_newsletter_route():
    data = request.get_json()
    content = data.get('content')
    subject = data.get('subject')
    if not content:
        return jsonify({"error": "Newsletter content is required"}), 400
    result = log_newsletter(subject , content)
    subscribers = get_subscribers()  # Assuming this fetches all subscribers from the database
    if subscribers:
        send_email_to_subscribers(subject, content)
    return jsonify(result)

@app.route('/newsletters', methods=['GET'])
def newsletters():
    result = get_newsletters()
    return jsonify(result)


@app.route('/send-emails', methods=['POST'])
def send_emails():
    data = request.get_json()
    subject = data.get('subject')
    message = data.get('message')

    if not subject or not message:
        return {"error": "Subject and message are required."}, 400

    result = send_email_to_subscribers(subject, message)
    return result



if __name__ == '__main__':
    app.run(debug=True)

