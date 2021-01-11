# 温湿度センサーDHT11 CSV出力ツール(DHT11CSV-TOOL)

## ・概要
```
RaspberryPiに接続した温湿度センサモジュールDHT11を使い温湿度測定結果をcsv出力するツール。
  出力結果は
    1)積み上げ式結果(Result.csv)
    2)最新結果(RecentResult.csv)
  として同一ディレクトリに出力する。
```
## ・フォーマット
```
(年/月/日 時:分:秒,温度,湿度)
 例:
    2019/02/25 21:28:36,24,43
```
## ・前提条件
```
1.RaspberryPiにDHT11が接続されていること。
2.Python3がインストールされていること。
3.DHT11のライブラリを入手していること。
    $ git clone https://github.com/szazo/DHT11_Python.git
```
以上
