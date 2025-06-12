from flask import Flask, render_template, jsonify

app = Flask(__name__)

ITEMS = [
    {
        'id': 1,
        'title': 'Mathematics Formula',
        'description': 'Qucik reference for common mathematics formulas.',
        'cost': 'Free',
    },
    {
        'id': 2,
        'title': 'JLPT Old Questions',
        'description': 'Practice questions for the JLPT exam.',
        'cost': 'Free',
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'description': 'San Francisco, CA',
        'cost': '$110,000',
    },
    {
        'id': 4,
        'title': 'Web Developer',
        'description': 'San Francisco, CA',
        'cost': '$110,000',
    },
    {
        'id': 5,
        'title': 'Product Manager',
        'description': 'Seattle, WA',
        'cost': '$130,000'
    },
]
@app.route('/')
def home():
    return render_template('home.html', items=ITEMS, name='My notebook')

@app.route('/api/items')
def list_items():
    return jsonify(ITEMS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)