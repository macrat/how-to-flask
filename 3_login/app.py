import flask


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'this is secret password'


@app.route('/')
def index():
    return '''
    <a href="/mypage">マイページへ</a><br>
    <br>
    <form action="/login">
        ユーザー名: <input name="name"><br>
        パスワード: <input name="password" type="password"><br>
        <input type="submit" value="ログイン">
    </form>
    '''


@app.route('/login')
def login():
    flask.session['name'] = flask.request.args.get('name')

    return 'ようこそ {}さん<br><a href="/mypage">マイページへ</a>'.format(flask.session['name'])

@app.route('/mypage')
def mypage():
    if 'name' in flask.session:
        return '{}さんのページ<br><br><a href="/logout">ログアウト</a> <a href="/">トップページ</a>'.format(flask.session['name'])
    else:
        return 'ログインしてください<br><br><a href="/">トップページ</a>'


@app.route('/logout')
def logout():
    del flask.session['name']

    return 'ログアウトしました<br><a href="/">トップページへ戻る</a>'


if __name__ == '__main__':
    app.run(debug=True)
