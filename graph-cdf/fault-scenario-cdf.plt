# ファイル名: fault-scenario-cdf.plt

# 入力ファイル名
set datafile separator '\t'  # TSV形式のデータ用に区切り文字を指定

# 出力設定
set terminal pdfcairo font "Helvetica,18" size 3.5in, 2.5in  # フォントサイズを12ptに設定
set output "fault-scenario-cdf.pdf"   # 出力ファイル名
set termoption enhanced

# 軸ラベル
set xlabel "TTR (minutes)"
set ylabel "CDF"

# 軸の範囲設定
set xrange [0:3500]

# 軸のメモリ設定
set xtics 1000
set ytics 0.2
set xtics nomirror
set ytics nomirror

# グラフスタイル
set style data lines  # 折れ線グラフを描画

# 凡例を表示
# set key outside top center
set nokey

# ボーダー
unset border
set border 3

# プロットコマンド
# plot "fault-scenario-cdf.tsv" using 1:2 with lines \
#      lw 4 lt rgb "#FF6347" title "13件の障害シナリオ"

plot "github-available-report-analysis-cdf.tsv" using 1:2 with lines \
     lw 4 lt rgb "#1E90FF" title "GitHub Availability Reports"
