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

# 凡例を表示(Logisticのみ表示)
set key at 3500,0.3

# ボーダー
unset border
set border 3

# ログロジスティック関数の定義と初期値
alpha = 51
beta = 1.1
f(x) = 1.0 / (1.0 + (x/alpha)**(-beta))

# フィッティング（x > 0のデータのみ使用）
fit f(x) "github-available-report-analysis-cdf.tsv" using ($1>0?$1:1/0):2 via alpha,beta

plot "github-available-report-analysis-cdf.tsv" using 1:2 with lines \
     lw 4 lt rgb "#1E90FF" notitle, \
     f(x) with lines \
     lw 4 lt rgb "#FF6347" dashtype 2 title "Log-logistic \n({/Symbol b}=1.193, {/Symbol a}=51.41)"

# # PNG
# set terminal png
# set output "fault-scenario-cdf.png"
# set termoption enhanced
# replot
