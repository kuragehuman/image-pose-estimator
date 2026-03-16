# image-pose-estimator
画像からの3Dポーズ推定

## 使用ライブラリ

- Three.js (MIT License)
- three-vrm (MIT License)
- Kalidokit (MIT License)
- MediaPipe (Apache License 2.0)

## 【開発メモ】

VRMはアップしていません

ボーンを3Dモデルに反映したい

pyrenderではボーン操作はできない(読み込んだモデルがボーン情報を持っていない？)ようなので、three,jsなどを利用して、webサイト上で実装する

batファイルでWebサーバーの起動とpythonでのポーズ取得をどちらも実行する

ポーズ推定もwebブラウザ上でやった方が早いかも？
→やってみたが、現状は肘、手首、腰くらいしか動かない



## 【バージョン指定】

Python 3.11.9

mediapipe 0.10.14