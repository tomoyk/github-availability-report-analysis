#!/usr/bin/env python3

# 階級の幅を変数として定義
bin_width = 100

input_filename = "result_summary2.txt"
output_filename = "result_summary3.txt"

# 入力ファイルからデータを読み込む（各行は整数が1個ずつ記載されていると仮定）
with open(input_filename, "r") as f:
    # 空行を除外して整数に変換
    data = [int(line.strip()) for line in f if line.strip()]

if not data:
    print("入力ファイルにデータが存在しません。")
    exit(1)

# データの最小値・最大値からビンの範囲を決定
min_val = min(data)
max_val = max(data)

# 下限は min_val を bin_width で割った商に bin_width をかけた値
# 上限は max_val を bin_width で割った商に1を足して bin_width をかけた値
start = (min_val // bin_width) * bin_width
end = ((max_val // bin_width) + 1) * bin_width

# 各ビンの度数を 0 で初期化（キーはビンの下限）
bins = {b: 0 for b in range(start, end, bin_width)}

# 各データを対応するビンにカウント
for x in data:
    # 例: 61 → (61 // 100)*100 = 0, 265 → (265 // 100)*100 = 200 など
    bin_lower = (x // bin_width) * bin_width
    bins[bin_lower] += 1

# 結果を出力ファイルに書き出す
with open(output_filename, "w") as f:
    for b in range(start, end, bin_width):
        # ビンの範囲と度数を出力（例："0 - 100: 4"）
        # f.write(f"{b} - {b + bin_width}: {bins[b]}\n")
        f.write(f"{b} {bins[b]}\n")

