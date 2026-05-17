## 学習ログ

### 2026/04/22
- Udemyコース開始：Mastering OpenAI Python APIs
- Section1（8講義）完了
- 学んだこと：OpenAI概要、ニューラルネットワーク基礎、APIキー作成
- 次回：Section2からコードを書き始める

### 2026/04/23
- Section2 開始
- Chat Completions API で stop パラメータの動作確認
- Responses API には stop が非対応であることを発見・解決
- 幼児語キャラクターのプロンプト動作を確認
- 次回：Section2 の続きから

### 2026/04/24
- Section2 19〜21完了
- Section3 22〜26完了
- プロンプトエンジニアリングの基礎（出力制御・要約・データ抽出・感情分析）
- 次回：27「Zero-Shot vs Few-Shot Prompting」から

- nパラメータでの回答数制限やecho（※現在は廃止）での質問の反映等がある
- Modelsには以下がある
 ・DALL-E: generates and edits images
 ・Whisper: converts audio to text
 ・Codex: understands and generates code
 ・Moderation: detects safe and unsensitive text
 ・GPT-3: understands and generates natural language
 ・GPT-3.5: set of models of that improve upon GPT-3
 ・GPT-4: advanced version of OpenAi's large language model
- Modelによって価格が変わるので、達成したい内容に沿ったモデルを選ぶことが重要
- Prompt Design
 ・Main Instructions: provide clear instructions
 ・Data: any input data(if necessary)
 ・Output Instructions: be specific about your desired output
- Prompt Design の活用例
 ・Summarization Prompts
 ・Data Extraction Prompts
 ・Sentiment Analysis Prompts
 ・Zero-Shot, Few-Shot
 ・Let's think step by step
 ・Transform

 ## 2026/04/25
- Section3 27～29完了
- Section4 30〜35完了
- FlaskではなくFastAPIで進める方針決定
- Flask→FastAPI の対応関係を確認
- 次回：36「Writing the Palette Endpoint」から

## 2026/04/28
- Section4 36完了
- FastAPI Form取得方法確認（Annotated推奨記法）
- get_colors関数実装（OpenAI APIでカラーパレット生成）
- FastAPI POSTエンドポイント完成
- 次回：37「Creating The Form」から

## 2026/04/29
- Section4 37〜41完了
- HTMLフォーム作成
- StaticFiles設定（CSS適用）
- URLSearchParamsでform-data送信の仕組み理解
- 次回：42「Refactoring Our Front-End Code」から

## 2026/05/01
- Section4 42完了（カラーパレットアプリ完成）
- Section5 43〜47完了
- 学んだこと：temperature・top_p・frequency_penalty・presence_penalty・streaming
- Tempature: 高いほど回答のランダム性があがる(0~2)
- Top P: どのトークンが選ばれて、どのトークンが選ばれないかを決めるサンプリング・ウィンドウの幅を設定するようなもの(0~1)
- Frequency Penalty: 繰り返しの可能性、値が大きい程、繰り返す可能性が下がる(-2~2)
- Presence Penalty: 同じ行を逐語的に繰り返す可能性を減らす(-2~2)
- steram: TrueにするとPythonではジェネレーターと呼ばれるものが返される(boolean)
- 次回：48から

## 2026/05/02
- role:system, user, assistantにそれぞれcontentで指示を出すことができる
- Section6 48〜54完了（Chat APIの基礎）
- Section7 55〜59完了（チャットボット完成）
- 次回：60から

## 2026/05/04
- Section8 60〜64完了（コード解析・バグ修正・生成）
- クイックソートのpartition関数を詳細解析
- Section9 65〜66完了（TikToken・トークンカウント）
- Section10 67〜72完了
- シンプルなコードレビュアー：実装済み✅
- インタラクティブなコードレビュアー：視聴のみ

## 2026/05/06
- Section11 73〜78完了（Spotify API連携）
- Premiumアカウント制限によりspotipyは動作未確認
- 残り79〜82は動画視聴のみで完了予定

## 2026/05/10
- Section11 79〜82完了（動画視聴のみ）
- Spotifyプレイリスト生成の全体像を把握
- for...elseの挙動・2段階クエリの仕組みを理解
- Section12 83〜88完了
- Embeddings: Embeddings are numerical representations of text concepts converted to number sequences
  → ベクトルに変換することで類似商品を見つけやすくなったりする
- Embeddingの概念理解（テキスト→数値ベクトル変換）
- 5000本映画のEmbedding可視化プロジェクト導入
- 次回：89「Add your Tenacity Import」から

## 2026/05/12
- Section12 89〜92完了
- 5000本映画のEmbedding生成・Nomic Atlasで2次元可視化
- 類似映画推薦機能の実装✅
- tiktokenでトークン上限対応
- 次回：Section13 93「Expanding GPT-4 Knowledge With Embeddings」から

## 2026/05/13
- Section13 93〜95完了
- 自力でRAGを実装（career_bot.py）
  - ファイル読み込み・段落分割
  - Embedding生成・キャッシュ管理
  - コサイン類似度によるインデックス取得
  - 類似段落検索
  - GPTへのコンテキスト渡しと回答生成
- 詰まったポイントと解決
  - 変数名と関数名の衝突（indices_of_nearest_neighbors）
  - returnがループ内にあった問題
  - モデル定数化による変更への対応
- 動作確認：「目標は？」への回答成功
- 次回：Section14 96から

## 2026/05/15
- Section14 96〜99完了（動画視聴のみ）
  - Reddit APIでコメント収集→センチメント分析→可視化の流れを把握
- Section15 100〜102完了（動画視聴のみ）
  - 本の要約プロジェクトの概要把握
  - トークン上限を超えないようにテキストを分割して要約する設計を理解
- 次回：103「Summarization Logic」から実装へ

## 2026/05/17
- Section15 103〜105完了（動画視聴・コード読解）
- 理解した内容：
  - memoize_to_fileデコレータ（クロージャ・キャッシュ設計）
  - take_tokens（トークン上限での分割ロジック）
  - gpt_summarize（リトライ・Exponential Backoff）
  - summarize（再帰的Map-Reduceパターン）
  - synthesize_summaries（2段階モデル設計）
- 次回：Book Summarizerを実際に手を動かして実装