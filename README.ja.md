# 🧠 my-second-brain

[한국어](README.md) · [English](README.en.md) · **日本語**

AIと一緒に仕事を記録し、必要な文脈を探し、繰り返す作業をスキルにまとめるワークスペースのテンプレートです。Codexアプリ、またはClaude DesktopのCodeでフォルダーを開いて使います。

> 人が仕事を進めて判断し、AIが記録を整理・維持します。

**初めての方は[架空の業務を1件記録するガイド](docs/getting-started.ja.md)から始めてください。** 外部サービスへの接続は不要です。

## できること

- **記録する：** 完了した作業、決定事項、次の行動を週次ログに残します。
- **探す：** 過去のログやテーマ別メモリから仕事の文脈を取り出します。
- **繰り返す：** 定型作業を再利用できるスキルにまとめます。
- **作る：** 文書、プレゼンテーション、スクリプトなどを同じ場所で作成します。作業によっては追加ツールが必要です。

## 始め方

```bash
git clone https://github.com/tiger-dreams/my-second-brain.git
cd my-second-brain
```

この公開リポジトリでは架空の資料で試してください。実際の業務記録は別の**非公開リポジトリ**で管理し、記録前にリモートURLを確認してください。公開リポジトリのForkも公開されます。

1. Codexアプリ、またはClaude DesktopのCodeでダウンロードしたフォルダーを開きます。VS Codeや拡張機能は不要です。
2. AIに次のように依頼します。

```text
AGENTS.mdとCLAUDE.mdを読み、初めて使うワークスペースとして設定してください。
設定の質問は1つずつしてください。回答と業務ログは日本語で書いてください。
```

3. 役割、定型業務、使用ツール、MCPの有無、使用言語を伝えると、AIがプロフィールを整理します。`[SETUP_REQUIRED]`は初期設定の目印です。
4. [開始ガイド](docs/getting-started.ja.md)の架空の業務でログを確認します。

AIにはフォルダーの読み取り・編集権限が必要です。インストール、ログイン、料金プラン、実行権限は各ツールの案内に従ってください。削除、インストール、公開、送信は対象と実行結果の見込みを確認してから行います。

## CodexとClaudeの共通ルール

Codexは[`AGENTS.md`](AGENTS.md)から始め、Claudeは[`CLAUDE.md`](CLAUDE.md)内の`@AGENTS.md`で共通ルールを読み込みます。Codexもリポジトリの指示に従って`CLAUDE.md`のプロフィールを読みます。

| 基準 | 動作 |
|---|---|
| 対象の確認 | 編集前にパス、リモートホスト、所有者/リポジトリ、ブランチを確認します。 |
| 共通ルールの集約 | `AGENTS.md`を正本とし、他の文書から参照します。 |
| メイン・サブチャット | 各会話で行った意味のある作業を、個別の記録依頼なしでログに残します。 |
| 簡潔なログ | 結果 → 残る作業・返答待ちの相手 → 根拠リンクの順で書きます。 |
| 重複の防止 | 最新ログを読み、同じ項目を更新し、他の会話の記録を保ちます。 |
| 後続作業の確認 | 完了・承認の根拠を確認し、実際に残る作業だけを追加します。 |

これらはAIが指示を読み、ファイルを編集できる場合に適用されます。サブチャットにログの編集権限がなければ、保存できなかった内容を報告します。ログへの記録権限は、外部への送信や外部ツールの変更権限を与えるものではありません。

## 保存先

```text
my-second-brain/
├── AGENTS.md                       # 共通の運用ルール
├── CLAUDE.md                       # 初期設定・プロフィール・ツール別案内
├── MEMORY.md                       # テーマ別メモリの索引
├── docs/
│   ├── getting-started.md          # 韓国語ガイド
│   ├── getting-started.en.md       # 英語ガイド
│   ├── getting-started.ja.md       # 日本語ガイド
│   ├── weekly-logs/                # 月曜日の日付を使う週次ログ
│   └── skills-guide/               # スキルの作成・利用ガイド
├── .agents/skills/                 # Codex用の相対シンボリックリンク
└── .claude/
    ├── memory/                     # 継続して使う好みや仕事の文脈
    └── skills/                     # スキルの原本
```

業務上の出来事は`docs/weekly-logs/weekly_log_YYYY-MM-DD.md`、長く使う文脈は`.claude/memory/`に整理します。スキルは`.claude/skills/`で編集し、Codex用のコピーは作りません。

## 週次ログの使い方

会話中に意味のある作業が完了した場合や、ユーザーから実施済みの仕事を伝えられた場合に記録します。単純な質疑応答や成果の残らない検索は除きます。下書き、送信済み、返信待ちを区別し、長い調査過程は別の資料にリンクします。

```text
案内文の下書きを作成しました。まだ送信しておらず、レビュー待ちです。
今週のログに、下書きの完了とレビュー待ちを区別して記録してください。
```

```markdown
- [x] [TODO] 案内文の下書き作成完了。レビュー待ち。[下書き](相対パス)
```

ソースタグは`[JIRA-123]`、`[SLACK]`、`[MAIL]`、`[MEET]`、`[TODO]`を使い、確認できる識別子とリンクを添えます。ファイル名にはその週の月曜日、本文には実際の作業日を使います。前週の未完了項目は状態を保って引き継ぎます。

ユーザーが中央ログを指定した場合は、そこに記録します。未接続の外部サービスから自動で情報を収集したり、会話終了後も記録し続けたりするものではありません。詳細は[共通ログルール](AGENTS.md#logging-strategy)を参照してください。

## 同梱スキル

| スキル | 用途 | 開始ドキュメント |
|---|---|---|
| `anyweb-reader` | 通常の取得に失敗したWebページを読む | [SKILL.md](.claude/skills/anyweb-reader/SKILL.md) |
| `pptx` | PowerPointの作成・編集・ソース同期 | [スライド作成ガイド](.claude/skills/pptx/deck-generation.md) |
| `walkthrough-video` | 画面操作・ナレーション・字幕付き動画の制作 | [利用ガイド](docs/skills-guide/walkthrough-video.md) |

スキルは依存ツールを自動インストールしません。動画は対象サービスに合わせて入力、画面操作、制作スクリプトを用意します。[スキル作成ガイド](docs/skills-guide/how-to-create-skills.md)から定型業務を追加できます。

## 言語と文書管理

READMEと開始ガイドは韓国語・英語・日本語に対応しています。設定時に回答と記録の言語を選べます。個別の依頼で言語を指定した場合は、その指定を優先します。その他の文書とスキルは現在、韓国語または英語です。

更新時は[翻訳の管理基準](docs/i18n.md)に従って3言語の主要な案内をそろえます。共通運用ルールの正本は`AGENTS.md`です。

## 外部サービスとの接続

Slack、メール、Jira、カレンダーを読むには、各アプリでMCPと権限を別途設定します。このリポジトリを取得するだけではアカウントは接続されません。Claudeの`.mcp.json`とCodexの設定形式は異なります。認証情報はローカルで管理してください。

## 参考

- [LLM Wiki — Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Codexの指示](https://developers.openai.com/codex/guides/agents-md) · [スキル](https://developers.openai.com/codex/skills) · [MCP](https://developers.openai.com/codex/mcp)
- [Claude Codeドキュメント](https://code.claude.com/docs/en/overview) · [Claude DesktopのCode](https://code.claude.com/docs/en/desktop-quickstart)
