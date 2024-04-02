from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html', active_page='main')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/products')
def products():
    return render_template('products.html', active_page='products')


@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True)
