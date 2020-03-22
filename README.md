# hack-for-corona

国難になにかできないかを考える。

とりあえず世界も日本もわたしには範囲が広すぎるので神奈川県川崎市のためのなにか。

## 神奈川県のデータ集計

Jupyter Notebookでとりあえず感染者の統計量をみて可視化した。

- https://nbviewer.jupyter.org/github/tsu-nera/hack-for-corona/blob/master/notebooks/kanagawa-corona.ipynb

## Data Sources

基本は神奈川県 HP の対策ページから。

- [新型コロナウイルス感染症について \- 神奈川県ホームページ](https://www.pref.kanagawa.jp/docs/ga4/bukanshi/bukan_200114.html)
- [新型コロナウイルス感染症対策　陽性患者数及び陽性患者の属性データ \- 神奈川県ホームページ](https://www.pref.kanagawa.jp/docs/t3u/dst/s0060925.html)
- [新型コロナウイルス感染症対策　専用ダイヤル相談件数 \- 神奈川県ホームページ](https://www.pref.kanagawa.jp/docs/t3u/dst/s0352970.html)
- [新型コロナウイルス感染症対策　帰国者・接触者電話相談センター相談件数 \- 神奈川県ホームページ](https://www.pref.kanagawa.jp/docs/t3u/dst/s9516276.html)
- [新型コロナウイルス感染症対策　医療機関（病院）の状況 \- 神奈川県ホームページ](https://www.pref.kanagawa.jp/docs/t3u/dst/s0361985.html)

神奈川(公式)対策サイト

- [神奈川県 新型コロナウイルス感染症対策サイト](https://www.pref.kanagawa.jp/osirase/1369/)
- [openkawasaki/covid19: 神奈川県 新型コロナウイルス対策サイト](https://github.com/openkawasaki/covid19)

各市の対策ページへのリンク。

- [川崎市：【緊急情報】新型コロナウイルス感染症について](http://www.city.kawasaki.jp/350/page/0000114231.html)
- [新型コロナウイルス感染症に関する情報について　横浜市](https://www.city.yokohama.lg.jp/city-info/koho-kocho/koho/topics/covid-19.html)
- [新型コロナウイルス感染症について｜相模原市](http://www.city.sagamihara.kanagawa.jp/kurashi/kenko/kansenyobo/1018481.html)
- [鎌倉市／新型コロナウイルス感染症について](https://www.city.kamakura.kanagawa.jp/skenkou/covid-19.html)
- [新型コロナウイルスについて \| 厚木市](https://www.city.atsugi.kanagawa.jp/information/d047408.html)

## References

いろいろな取り組みをとりあえず調べる。ここがいろいろまとまってる。

[COVID\-19 GIS Hub](https://coronavirus-disasterresponse.hub.arcgis.com/)

SIGNATEのコンペは面白そう。

- [COVID\-19チャレンジ（フェーズ1） \| SIGNATE \- Data Science Competition](https://signate.jp/competitions/260)

### 日本

- [kaz\-ogiwara/covid19: 新型コロナウイルス（COVID19）の国内における感染の状況を厚生労働省の報道発表資料からビジュアルにまとめた。](https://github.com/kaz-ogiwara/covid19)
- [tokyo\-metropolitan\-gov/covid19: 東京都公式 新型コロナウイルス対策サイト](https://github.com/tokyo-metropolitan-gov/covid19)
- [reustle/covid19japan](https://github.com/reustle/covid19japan)
- [新型コロナ感染 日本国内・世界各国マップ \| ESRI ジャパン](https://www.esrij.com/news/details/124546/?utm_source=esrij&utm_medium=topbanner&utm_campaign=covid19)
- [swsoyee/2019\-ncov\-japan: 🦠 Interactive dashboard of COVID\-19 cases in Japan](https://github.com/swsoyee/2019-ncov-japan)

詳細なデータと可視化サイト。CSVもダウンロード可能。

- [都道府県別新型コロナウイルス感染者数マップ Coronavirus COVID\-19 Japan Case \(2019\-nCoV\)](https://gis.jag-japan.com/covid19jp/)
- [「新型コロナウイルス感染者数マップ」について – J\.A\.G JAPAN](https://jag-japan.com/covid19map-readme/)
- [日本国内における新型コロナウイルス感染症の患者数マップの公開 – J\.A\.G JAPAN](https://jag-japan.com/blog/news/covid-19-map/)

医学的な情報がまとまっている。

- [新型コロナウイルス感染症｜感染症トピックス｜日本感染症学会](http://www.kansensho.or.jp/modules/topics/index.php?content_id=31)

### 世界

- [List of Novel Coronavirus Dashboards](https://www.arcgis.com/sharing/rest/content/items/a1746ada9bff48c09ef76e5a788b5910/resources/1581644001033.jpeg?w=2400)
- [新型コロナウイルス感染状況ダッシュボード \| ESRI ジャパン](https://www.esrij.com/news/details/124059/)
- [SteffanCrowe/CoronaScraper: Scrape the current number of infected in the UK](https://github.com/SteffanCrowe/CoronaScraper)
- [nyem69/coronavirus_data: data from multiple sources](https://github.com/nyem69/coronavirus_data)
- [avischiffmann/Coronavirus\-Dashboard: This is a website I made to track the ongoing Coronavirus \(nCov2019\)](https://github.com/avischiffmann/Coronavirus-Dashboard)
- [Aashish\-Anand/corona\-tracker](https://github.com/Aashish-Anand/corona-tracker)
- [CSSEGISandData/COVID\-19: Novel Coronavirus \(COVID\-19\) Cases, provided by JHU CSSE](https://github.com/CSSEGISandData/COVID-19)
- [Building a Coronavirus tracker app with Spring Boot and Java \- Java Brains Tutorial \- YouTube](https://www.youtube.com/watch?v=8hjNG9GZGnQ)
- [Covid\-19\-data\-science/README_EN\.md at master · wuhan2020/Covid\-19\-data\-science](https://github.com/wuhan2020/Covid-19-data-science/blob/master/README_EN.md)

## Authors

* [tsu-nera](https://twitter.com/tsu_nera)
