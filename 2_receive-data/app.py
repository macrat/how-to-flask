import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return '''
    <form action="/receive">
        入力するだけ: <input name="value">
        <input type="submit">
    </form>
    <form action="/user">
        ユーザー名: <input name="name">
        <input type="submit">
    </form>
    <form action="/calc">
        <input name="number"> + 1
        <input type="submit">
    </form>
    '''


@app.route('/receive')
def receive():
    return '入力されたデータは"' + flask.request.args.get('value') + '"です'


@app.route('/user')
def user():
    name = flask.request.args.get('name')
    if name == 'admin':
        return 'this is admin page'
    else:
        return 'welcome ' + name


@app.route('/calc')
def calc():
    number = flask.request.args.get('number')
    if number.isdigit():
        answer = int(number) + 1
        return str(answer)
    else:
        return '数字を入力してください。'


if __name__ == '__main__':
    app.run()
