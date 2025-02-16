# 出力端末と画像ファイルの設定（幅を1200に設定）
set terminal pngcairo size 1200,600 enhanced font "Helvetica,12"
set output "graph.png"

# タイトルと軸ラベルの設定
set title "Frequency Distribution"
set xlabel "Time to recover"
set ylabel "Count"

# ヒストグラム（ボックス）の見た目の設定
set style fill solid 0.5 border 1
# set boxwidth 1.0

# plot "result_summary3.txt" using 1:2 with boxes title "Frequency"
plot "result_summary3.txt" using ($1+50):2 with boxes title "Frequency"



