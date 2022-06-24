# dijkstra_algorithm
ダイクストラ法を使って最短の距離と経路を計算します

## 使い方
```
$ python3 main.py データファイル
```

## 実行例
```
$ python3 main.py route01.data
distance=45.0
0-3-6

$ python3 main.py route02.data
distance=204.0
0-4-3-7-10-14-15-16-19

$ python3 main.py route03.data
distance=213.0
0-4-5-10-15-20-24-25-29

$ python3 main.py route04.data
distance=47.0
0-150-200-240-332-229-300-400-557-466-500-600

$ python3 main.py route05.data
distance=70.0
0-150-200-240-332-229-300-400-557-466-500-600-764-786-700-800
```

データファイルにはhttps://nw.tsuda.ac.jp/lec/dijkstra/ 課題2のデータファイルを使いました。

## データファイル形式

> N R \
> A1 B1 L1 \
> A2 B2 L2 \
> ... \
> AR BR LR \
> S D

最初の行には２個の整数 N と R が含まれる。 N は都市の数を表し、 Rはそれらの都市をつなぐ道の個数を表す。
２行目以降はR行に渡って、２個の整数 Ai, Bi、１個の実数 Li が含まれる(1≦i≦R)。 Ai と Biは道の両端の都市を表し (0≦Ai≦N-1, 0≦Bi≦N-1)、 Liは道の距離を表す。 
その次の行に２個の整数 S, D が含まれる。 S は出発地点の都市を表し、Dは目的地点の都市を表す (0≦S≦N-1, 0≦D≦N-1)。
