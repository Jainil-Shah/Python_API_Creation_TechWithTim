from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra
    
    return jsonify(user_data), 200

@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    # if request.method == 'POST':
    return jsonify(data), 201

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    data = request.json
    # d = json.loads(data)
    return data['message'], 200
    
    
    
if __name__ == '__main__':
    app.run(debug=True)