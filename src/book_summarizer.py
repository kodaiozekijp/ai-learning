







# 1.本の読み込み
book_path = "data/book.txt"
def load_book_content(book_path):
    with open(book_path, "r", encoding="utf-8") as file:
        return file.read()

# 2.内容の要約
target_summary_size = 1000
max_tokens = 4096
division_point = "."
def get_summary_of_book(book_content, target_summary_size, model, division_point):
    pass

#  - 本の内容を段落毎に分割する
#  - chatgptのAPIを利用して分割した段落を要約する
#  　- 分割した段落のトークン数チェック
#      - 入力上限を超えていた場合は、更に分割する
#    - 出力のトークン数チェック
#      - 出力上限を超えていた場合は、出力上限を超えなくなるまで再帰的に要約にかける

def split_text(text, division_point):
    return text.split(division_point)

# 3.要約を結合して、最終的な要約を取得する
# 4.要約を出力する