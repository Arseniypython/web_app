from flask import Flask, render_template, request

app = Flask(__name__)

def index():
    return render_template('main.html', ok='Проверяем')
def test():
    obj = request.form.items()
    print(obj)
    return render_template('answer.html', post='Проверяем', obj=obj)
app = Flask(__name__)  
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test, methods=['post'])
app.config['SECRET_KEY'] = 'secret_key'

if __name__ == '__main__':
   app.run()