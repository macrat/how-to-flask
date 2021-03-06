環境を用意する
==============

## Pythonをインストールする
まず初めに、[Python](https://www.python.jp/)のインストールを行ないます。
[README](../README.md#Python)に詳しく書きましたが、Pythonには2系と3系の2つのバージョンがあります。
とくに理由が無い限り、3系の最新版をインストールするようにしてください。

UbuntuでPython3をインストールするには、ターミナルを開いて以下のコマンドを入力します。（ご存知のことと思いますが、行の初めの`$`はあなたが打つべきコマンドであることを示す記号です。この記号自体をあなたが打つ必要はありません。）
``` bash
$ sudo apt install python3
```
パスワードを聞かれますので、入力してください。
そのあと、インストールしても良いかどうか聞かれるので、エンターを押してインストールを続行してください。

また、python用のライブラリを管理してくれる便利なツールである[pip](https://pypi.python.org/pypi/pip)というソフトウェアもインストールしておきます。
Ubuntuでは、以下のコマンドをターミナルに入力することでインストール出来ます。
``` bash
$ sudo apt install python3-pip
```
再びインストールしても良いかどうか聞かれますので、エンターを押して続行してください。

これで、開発に必要なPythonの環境が整いました。

## Flaskをインストールする
Webアプリを開発するためのフレームワークである[Flask](http://flask.pocoo.org/)をインストールします。

pipが入っている環境であれば、以下のコマンドをターミナルに入力すればFlaskをインストールすることが出来ます。
``` bash
$ sudo pip3 install flask
```

環境によっては、`pip3`ではなく`pip`というコマンドを使わなければいけないかもしれません。

## 次になにをすれば良いか
これで開発環境の準備が整いました。
[次のステップ](../1_hello-world/)に進んで、構築した環境が実際に動作するかどうか確かめてみましょう。
