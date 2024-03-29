# DiscriminateFruit
リンゴとミカンの画像に対して線形判別分析(LDA)を行う。<br>
画像はRGB値の平均値が抜き出され、3個の特徴量(RGB）に変換される。<br>
3個の特徴量がLDAの入力となる。<br>
評価方法は
- 判別的中率(訓練データ＝テストデータ)
- Leave-one-out 交差検証

## 画像の収集
[pixabay](https://pixabay.com/ja/) からりんご/みかんと検索して10枚ずつ取得した。

## 使い方
1. `data` にデータをアップロード
> 画像サイズ自由

2. `cut_image.py` を実行
> トリミングが必要な場合のみ行う<br>
> 画像にトリミングが実行され、`cutdata` に出力される

3. `preprocessing.py` を実行
> 画像の特徴量がcsvに出力される<br>
> この際、入力のときに参照するディレクトリが `data` か `cut_data` かになってるから必要に応じて変更する<br>
> 出力も `RGBValue.csv` とか `RGBValue_cutdata.csv` とか変更の必要がある

4. `lda.py` を実行
> `Standardization_flag` によって標準化する/しない をスイッチできる
