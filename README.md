Python/FlaskでなんとなくSNS的なものを作る講座
=============================================

## この資料について
[Python](https://www.python.jp/)/[Flask](http://flask.pocoo.org/)の環境を構築し、簡単なSNS的なものを作成する方法を学ぶ講座の資料です。

この講座はPythonやFlaskを*なんとなく*感じて、自力で学ぶための取っ掛りを持ってもらうためのものです。より詳しく学ぶための方法については[次になにをすれば良いか](./what-to-do-next.md)に記載があります。

プログラミング経験が無い人でも読めるように作っているつもりですが、それでも分かりづらい表現があるかもしれません。この資料単独で読むよりも、気になったら検索してみたり誰かに聞いてみたりしながら読むことをお勧めします。一旦見なかったことにして先に進んで、あとで戻って来てみるというのも手です。

文章中にはなるべく多くのリンクを記すようにしていますが、全てを読む必要はありません。
とくに[Pythonのチュートリアル](http://docs.python.jp/3/tutorial/index.html)は沢山の有益な情報が含まれていますが、難解な表現も多いです。頑張って読もうとするのではなく、"こんなものがあるのか"という程度で問題ありません。

## もくじ
- [Step 0. 環境を用意する](./0_install-requirements/)

  UbuntuにPythonやFlaskなどの必要なソフトウェアをインストールします。

- [Step 1. Hello World](./1_hello-world/)

  毎回固定の文字を表示するだけのシンプルなWebアプリケーションを作り、その動作を追い掛けてみます。

- [Step 2. データを受信する](./2_receive-data/)

  クライアントから受け取ったデータを表示するWebアプリケーションを作成してみます。
  また、入力に応じて挙動を変える方法を学びます。

- [Step 3. ログイン出来るようにする](./3_login/)

  *セッション*というものを用いて、ユーザーを識別したり簡単な情報を保存出来るようにします。
  また、これを使ってサイトにログイン機能を実装してみます。

- [Step 4. 掲示板を作る](./4_discussion-board/)

  少し実用的なアプリケーションとして、掲示板の作成に挑戦してみます。
  ここでは、多数のデータをまとめて扱う方法を学びます。

- [Step 5. データを保存する](./5_database/)

  SQLiteというデータベースの使い方を学びます。
  これを使って、掲示板に投稿されたデータをきちんと保存出来るようにします。

- [Step 6. 見た目を整える](./6_template-engine/)

  テンプレートエンジンの使い方を学び、サイトのデザインを整えます。

- [Step 7. プロフィールを作る](./7_profile-page/)

  ユーザーのプロフィールをサイトに保存出来るようにします。
  ここでは、動的なアドレスの作り方とファイルの扱い方学びます。

- [次になにをすれば良いか](./what-to-do-next.md)

  この講座をひと通り試してみた後、次にやってみるべきだと筆者が思うことが書かれています。

## 用意するもの
### Ubuntu
何はともあれ、開発に使用する環境が必要です。
この資料は[Ubuntu](http://www.ubuntulinux.jp)を使用する前提で作成していますが、他のディストリビューションでも（あるいは他のOSでも）問題ありません。
別のディストリビューションやOSを使用する場合、コマンド等は適宜読み替えてください。

### Python
用意したLinuxには[Python](https://www.python.jp/)がインストールされている必要があります。
[UbuntuにPythonをインストールする方法](./0_install-requirements/#pythonをインストールする)はあとで解説します。

Pythonのバージョンは大きく2系と3系の2つの系統があります。
3系は色々な機能が大幅に強化され、また扱いやすくなったモダンなバージョンですが、残念ながら一部の機能について2系と互換性がありません。このため、互換性のために2系も平行してメンテナンスされている状態です。
ですので、特別な事情があるのでない限り3系を使用することを強くお勧めします。

この資料は3系を使用する想定で作成していますが、ほとんどのコードは2系でも動作するはずです。

### Flask
[Flask](http://flask.pocoo.org/)の最新版を用意してください。
これについても、必要であれば[インストール方法の解説](./0_install-requirements/#flaskをインストールする)を読んでください。

## 最初になにをすれば良いか
[Ubuntu](http://www.ubuntulinux.jp)を用意してください。もしもそれを使いこなす自信があれば、他のOSでも構いません。

Ubuntuのインストールが終わったら、[PythonとFlaskのインストール](./0_install-requirements/)に進んでください。
もしもこれらのインストールが既に済んでいるのであれば、読み飛ばして[Hello World](./1_hello-world/)に進んでも構いません。
