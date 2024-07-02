import os
import shutil
import sys

# コマンド引数取得
args = sys.argv
command = args[0]
arg1 = args[1]
arg2 = args[2]
arg3 = args[3]


# -- reverseコマンド
# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
if arg1 == 'reverse':
    # 指定ファイルの読み込み
    # file = open(arg2 ,"r")
    with open(arg2, 'r') as f:
        content = f.read()
        f.close()

    # 読み込んだファイルの中身を反転
    reverse_content = content[::-1]

    # 指定パスのファイルへ反転した文字列を格納
    with open(arg3, 'w') as f:
        f.write(reverse_content)


# --copyコマンド
# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
if arg1 == "copy":
    res = shutil.copy(arg2, arg3)
    print(res)


# --duplicate-contentsコマンド
# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
if arg1 == 'duplicate-contents':
    with open(arg2, 'r') as f:
        content = f.read()
    
    with open(arg2, 'w') as f:
        for i in range(int(arg3)): 
            f.write(content)

# --replace-stringコマンド
# replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
if arg1 == 'replace-string':
    arg4 = args[4]

    with open(arg2, 'r') as f:
        content = f.read()
    
    content = content.replace(arg3,arg4)

    with open(arg3, 'w') as f:
        f.truncate(0)
        f.write(content)