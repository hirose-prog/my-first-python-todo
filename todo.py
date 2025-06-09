# todo.py

# ★追加: TODOデータを保存するファイル名
TODO_FILE = 'todos.txt'

def display_todo_list(todos):
    """
    TODOリストを表示する関数
    """
    print("--- TODO リスト ---")
    if not todos:
        print("TODOはありません。")
    else:
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo}") # 番号を付けて表示
    print("--------------------")

def add_todo(todos):
    """
    TODOを追加する関数
    """
    new_todo = input("新しいTODOを入力してください: ")
    todos.append(new_todo)
    print(f"'{new_todo}' を追加しました。")

def delete_todo(todos):
    """
    TODOを削除する関数
    """
    if not todos:
        print("削除できるTODOはありません。")
        return # TODOがないので処理を終了

    display_todo_list(todos) # どのTODOを削除するかユーザーに分かりやすくするため、一度リストを表示する
    try:
        # ユーザーに削除したいTODOの番号を入力してもらう
        todo_index_str = input("削除するTODOの番号を入力してください: ")
        # 入力された文字列を整数に変換
        todo_index = int(todo_index_str) - 1 # 表示は1から始まるが、リストのインデックスは0から始まるため-1する

        # 入力された番号が有効な範囲内かチェック
        if 0 <= todo_index < len(todos):
            deleted_todo = todos.pop(todo_index) # pop()は指定したインデックスの要素を削除し、その値を返す
            print(f"'{deleted_todo}' を削除しました。")
        else:
            print("無効な番号です。リストに表示されている番号を入力してください。")
    except ValueError: # 数字以外の文字が入力された場合の処理
        print("数字を入力してください。")
    except Exception as e: # その他の予期せぬエラー
        print(f"エラーが発生しました: {e}")

# ★追加: ファイルからTODOを読み込む関数
def load_todos(filename):
    todos = []
    try:
        with open(filename, 'r', encoding='utf-8') as f: # 'r'は読み込みモード
            for line in f:
                todos.append(line.strip()) # 行末の改行コードを削除して追加
    except FileNotFoundError:
        # ファイルがない場合は、空のリストを返す（初回起動時など）
        print(f"情報: {filename} が見つかりません。新しいTODOリストを作成します。")
    except Exception as e:
        print(f"TODOの読み込み中にエラーが発生しました: {e}")
    return todos

# ★追加: TODOをファイルに保存する関数
def save_todos(todos, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f: # 'w'は書き込みモード（既存の内容は上書きされる）
            for todo in todos:
                f.write(todo + '\n') # 各TODOの後に改行を追加して書き込む
        print(f"TODOリストを {filename} に保存しました。")
    except Exception as e:
        print(f"TODOの保存中にエラーが発生しました: {e}")


# --- アプリケーションの開始 ---

# ★変更: アプリケーション開始時にTODOをファイルから読み込む
my_todos = load_todos(TODO_FILE)
print("\nアプリケーションを開始します。")
display_todo_list(my_todos) # 読み込んだTODOリストを最初に表示

while True: # アプリケーションを繰り返し実行するためのループ
    print("\n--- メニュー ---")
    print("1. TODOを追加")
    print("2. TODOを表示")
    print("3. TODOを削除")
    print("4. アプリを終了")
    choice = input("選択してください (1/2/3/4): ")
    # print(f"デバッグ: 入力された値 = '{choice}', 型 = {type(choice)}, 長さ = {len(choice)}") # ★この行は削除してもOK

    if choice == '1':
        add_todo(my_todos)
    elif choice == '2':
        display_todo_list(my_todos)
    elif choice == '3':
        delete_todo(my_todos)
    elif choice == '4':
        print("TODOアプリを終了します。")
        save_todos(my_todos, TODO_FILE) # ★追加: アプリ終了時にTODOをファイルに保存
        break
    else:
        print("無効な選択です。1, 2, 3, 4 のいずれかを入力してください。")