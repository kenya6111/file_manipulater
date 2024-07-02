# Guess-the-number-game

## 🌱概要
ファイル操作アプリケーション

## ✨デモ


## 📝説明
コマンドラインからファイルの操作を行えます。
以下の操作が可能です。
 - reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
 - copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
 - duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
 - replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

## 🧰前提条件

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
<tr>
  <td rowspan=2>その他</td>
  <td>Git</td>
</tr>
<tr>
  <td>Github</td>
</tr>
</table>

## 📜作成の経緯
⭐️後で記載する!!!

作成した理由を記載する。

## ⭐️こだわった点
 - 各ファイル操作を関数化し、再利用性を向上
 - with句を用いてファイルを安全に閉じるようにした
 - main関数内でコマンド引数の数をチェックし、必要な引数が不足している場合には適切なエラーメッセージを表示してプログラムの実行を停止
 - コマンド引数の処理をmain関数でまとめ、使いやすくしました。
テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。



## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)
