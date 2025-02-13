import requests
from bs4 import BeautifulSoup
import time

def main():
    # URLの基本フォーマット（monthとyearをフォーマット文字列で埋め込みます）
    base_url = "https://github.blog/news-insights/company-news/github-availability-report-{month}-{year}/"
    
    # ループで処理したい年と月のリスト（例として2024年と2025年、全12ヶ月）
    years = [2020, 2021, 2022, 2023, 2024, 2025]
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    
    # 各URLに対して順次処理を実施
    for year in years:
        for month in months:
            if year == 2025 and months == "march":
                return
                
            url = base_url.format(month=month, year=year)
            print(f"Scraping {url} ...")
            
            # 結果を格納するリスト
            results = []
            results.append(f"URL: {url}")
            
            try:
                response = requests.get(url)
                # ステータスコードが200でなければその旨を結果に追加
                if response.status_code != 200:
                    results.append(f"  URLが取得できませんでした (status code: {response.status_code})")
                else:
                    soup = BeautifulSoup(response.text, "html.parser")
                    # ページ内の全テキストの中から "lasting" を含む文字列を抽出
                    lasting_texts = soup.find_all(string=lambda text: text and "lasting" in text.lower())
                    if lasting_texts:
                        for text in lasting_texts:
                            results.append(text.strip())
                    else:
                        results.append("  'lasting' を含むテキストは見つかりませんでした。")
            except Exception as e:
                results.append(f"  エラーが発生しました: {e}")
            
            # 結果をファイルに書き込み（ファイル名例: result_2024_january.txt）
            filename = f"result_{year}_{month}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                for line in results:
                    f.write(line + "\n")
            
            print(f"  結果は {filename} に保存されました。")
            
            # 各リクエスト間に5秒待機
            time.sleep(5)

if __name__ == "__main__":
    main()
