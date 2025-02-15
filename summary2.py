import re

# 単位ごとの変換（分）
conv = {
    'day': 24 * 60,
    'days': 24 * 60,
    'hour': 60,
    'hours': 60,
    'minute': 1,
    'minutes': 1,
}

# 数字と単位の組み合わせにマッチする正規表現
pattern = re.compile(r'(\d+)\s*(day|days|hour|hours|minute|minutes)', re.IGNORECASE)

# 入力ファイル名（例：input.txt）
with open('result_summary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        total_minutes = 0
        # 正規表現でマッチする部分をすべて処理
        for m in pattern.finditer(line):
            num = int(m.group(1))
            unit = m.group(2).lower()
            total_minutes += num * conv[unit]
        # 変換結果（分のみの数字）を出力
        print(total_minutes)

