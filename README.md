# Design Document

### 実行方法
- solver_annealing_method.py: TSPの解を出力するプログラム
  - 焼きなまし法と貪欲法を組み合わせたもの  
- output_generator.py: solver_annealing_methodの出力をoutput_{0-6}.csvに出力するプログラム
  - solver_annealing_methodをインポートしているので, ファイル名の変更には注意が必要   

## TSPの実装方針

### 焼きなまし法を用いる
- 参考文献: 「競技プログラミングの鉄則 アルゴリズム力と思考力を高める77の技術」

#### 焼きなまし法とは??
- 山登り法を改良したもの
  -　山登り法
    1. 初期解を適当に生成する
    2. 小さな変更をランダムに行い, スコアが良くなれば採用
    3. 上記を繰り返す

- 山登り法の課題: 小さな変更をしてもスコアが良くならず, 偽の最適解にハマってしまう
  - 本当はより良い解が存在するかもしれないが, 変更が小さいためにたどり着くことができない
  - 少しくらい悪くなっても良いから, 最適解を発見したい！
  - とはいえ, スコアの落差が大きい場合は除外したい...

- 焼きなまし法のアイデア
  - 山登り法の課題を解消する
  - ある程度スコアが悪くなることは許容することにする
  - 貪欲法を初期解として与える
  - (温度関数) T = 30 - 28 * (t / NUM_LOOPS) (0 <= t < NUM_LOOPS)
    - Tは30から28に線形的に変化すする
    - 開始時の温度と終了時の温度を変更すると精度に差が現れる
    - 温度関数の式としてはこの式が一般的らしいが, チューニングの余地あり
         
  - (遷移確率) prev = exp(min((current_score - new_score) / T, 0))
    - current_score >= new_score(スコアが改善する場合): prev = 1
    - current_score < new_score(スコアが改善しない場合): prev < 1 
      - Tが小さくなる, すなわちループが回るほど, 遷移確率は大きくなる
        - ループが回るほど偽の最適解にハマる可能性は高くなる

  - 0以上1未満の数をランダムに生成
    - この数よりも遷移確率が大きい場合のみnew_scoreの状態に遷移する  


