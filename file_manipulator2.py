import os
import shutil
import sys

# コマンド引数取得
# args = sys.argv
# command = args[0]
# arg1 = args[1]
# arg2 = args[2]
# arg3 = args[3]


# -- reverseコマンド
# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
def reverse(input_path, output_path):
    # if arg1 == 'reverse':
        # 指定ファイルの読み込み
        # file = open(arg2 ,"r")
        with open(input_path, 'r') as f:
            content = f.read()
            f.close()

        # 読み込んだファイルの中身を反転
        reverse_content = content[::-1]

        # 指定パスのファイルへ反転した文字列を格納
        with open(output_path, 'w') as f:
            f.write(reverse_content)


# --copyコマンド
# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
def copy (input_path , output_path):
    # if arg1 == "copy":
    res = shutil.copy(input_path, output_path)
    print(res)


# --duplicate-contentsコマンド
# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
def duplicate_content(input_path , duplicate_num):
# if arg1 == 'duplicate-contents':
    with open(input_path, 'r') as f:
        content = f.read()
    
    with open(input_path, 'w') as f:
        for i in range(int(duplicate_num)): 
            f.write(content)

# --replace-stringコマンド
# replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
def replace_string(input_path, needle, new_string):
# if arg1 == 'replace-string':
    # arg4 = args[4]

    with open(input_path, 'r') as f:
        content = f.read()
    
    content = content.replace(needle,new_string)

    with open(input_path, 'w') as f:
        f.truncate(0)
        f.write(content)


def main():
    # コマンド引数取得
    command = sys.argv[1]

    if command =='reverse':
        # コマンド引数チェック
        if len(sys.argv) != 4:
            print("Usage: reverse <inputpath> <outputpath>")
            return        
        # 引数取得
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        reverse(input_path, output_path)

    elif command =='copy':
        # コマンド引数チェック
        if len(sys.argv) != 4:
            print("Usage: copy <inputpath> <outputpath>")
            return
        # 引数取得
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        copy(input_path, output_path)

    elif command =='duplicate-contents':
        # コマンド引数チェック
        if len(sys.argv) != 4:
            print("Usage: duplicate-contents <inputpath> <n>")
            return
        # 引数取得
        input_path = sys.argv[2]
        duolicate_num = sys.argv[3]
        duplicate_content(input_path, duolicate_num)

    elif command=='replace-string' :
        # コマンド引数チェック
        if len(sys.argv) != 5:
            print("Usage: replace-string <inputpath> <needle> <newstring>")
            return
        # 引数取得
        input_path = sys.argv[2]
        needle = sys.argv[3]
        new_string= sys.argv[4]
        replace_string(input_path, needle, new_string)
        
    else :
        print('unknown command : {command}')

if __name__ == "__main__":
    main()