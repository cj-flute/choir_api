from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
choristers = [
    {'id': 1, 'name': 'John Doe', 'voice_part': 'Tenor'},
    {'id': 2, 'name': 'Jane Smith', 'voice_part': 'Soprano'},
    {'id': 3, 'name': 'Emily Davis', 'voice_part': 'Alto'},
    {'id': 4, 'name': 'Michael Brown', 'voice_part': 'Bass'}
]


@app.route('/api/choristers', methods=['GET'])
def get_choristers():
    return jsonify({'choristers': choristers})


@app.route('/api/choristers/<int:chorister_id>', methods=['GET'])
def get_chorister(chorister_id):
    chorister = next(
        (chorister for chorister in choristers if chorister['id'] == chorister_id), None)
    if chorister is None:
        return jsonify({'error': 'Chorister not found'}), 404
    return jsonify(chorister)


@app.route('/api/choristers', methods=['POST'])
def add_chorister():
    new_chorister = request.get_json()
    new_chorister['id'] = choristers[-1]['id'] + 1 if choristers else 1
    choristers.append(new_chorister)
    return jsonify(new_chorister), 201


@app.route('/api/choristers/<int:chorister_id>', methods=['PUT'])
def update_chorister(chorister_id):
    chorister = next(
        (chorister for chorister in choristers if chorister['id'] == chorister_id), None)
    if chorister is None:
        return jsonify({'error': 'Chorister not found'}), 404
    updated_data = request.get_json()
    chorister.update(updated_data)
    return jsonify(chorister)


@app.route('/api/choristers/<int:chorister_id>', methods=['DELETE'])
def delete_chorister(chorister_id):
    global choristers
    choristers = [
        chorister for chorister in choristers if chorister['id'] != chorister_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
