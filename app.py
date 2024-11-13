from flask import Flask, request, jsonify, render_template
import mail_send

app = Flask(__name__)
sender = mail_send.EmailSender('********@mail****', '*************', '********@mail.***')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_application():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    #Отправка письма
    if sender.send_mail('********@mail.ru', subject='Новая заявка', body=f'Имя {name}\nmail: {email}\n\n{message}') == 'failed':
        return jsonify({'status': 'failed'}), 500
    else:
        return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=80)
