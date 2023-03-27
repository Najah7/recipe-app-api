# recipe-app-api

# このレポジトリについて
レシピサイトを模倣したAIPを作成しました。<br>
今まで、学んできたDjangoを使って、少し本格的にバックエンド開発を個人でしてみたものをアップロードしたレポジトリです。<br>
なので、Docker、テスト、Swaggerなどを使っています。<br>
しかし、バックエンドにフォーカスしてので、フロントエンドはないです。<br>
なので、もし、Dockerを使って動くモノを確認する場合は、SwaggerのUIで確認してもらう形になります。<br>
※「/api/docs/」：Swaggerのエンドポイント（その後、機能を確認するときにToken認証をする必要もあります）

### このソフトウェアでのToken認証についての説明
Tokenエンドポイント(/api​/user/token/)からTokenを取得してヘッダーに付与する必要があります。<br>
SwaggerのUIの機能を使えばとても簡単にヘッダへの継続化などができます。<br>
※SwaggerのUI機能の使い方については割愛させていただきます
