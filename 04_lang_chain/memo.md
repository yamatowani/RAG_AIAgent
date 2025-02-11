## LangChainのRAGに関するコンポーネント
- Document loader: データソースからドキュメントを読み込む
- Document transformer: ドキュメントになんらかの変換をかける, チャンクで切り分けるなど
- Embedding model: ドキュメントをベクトル化する
- Vector store: ベクトル化したドキュメントの保存先
- Retriever:  入力されたテキストと関連するドキュメントを検索する

