<p align="center">
  <img src="../../logo.png" alt="i-have-adhd" width="140" />
</p>
<p align="center">
  <strong align="center">ADHD に配慮した出力。ADHD の診断は不要です！</strong>
</p>
<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/ayghri/i-have-adhd?style=flat" alt="ライセンス"></a>
</p>

<p align="center">
  <a href="../../README.md" title="English" aria-label="English">🇬🇧</a> ·
  <a href="README.zh-CN.md" title="简体中文" aria-label="简体中文">🇨🇳</a> ·
  <a href="README.pt-BR.md" title="Português (Brasil)" aria-label="Português (Brasil)">🇧🇷</a> ·
  <strong title="日本語" aria-label="日本語">🇯🇵</strong> ·
  <a href="README.vi.md" title="Tiếng Việt" aria-label="Tiếng Việt">🇻🇳</a> ·
  <a href="README.ko.md" title="한국어" aria-label="한국어">🇰🇷</a>
</p>


## インストール

🔗 [インストール手順](../install/INSTALL.ja.md)

## 機能

検証済みの結果、必要な判断、または次の行動を先に示し、根拠や安全上の制約を埋もれさせないためのスキルです。「お役に立てれば幸いです！」は不要です。


## 変わること


<table>
<tr>
<td width="50%">

## 適用前

> 良い質問ですね！考えてみましょう。認証フローには、ミドルウェア、トークン検証、Cookie の処理といういくつかの要素があります。`src/auth.ts` を見ると、`verifyToken` 関数（42～58 行目付近）は古い `jsonwebtoken` API を使っているようです。一つの方法は、パッケージを更新してその関数を書き直すことです。変更後は、認証テストを実行して問題が起きていないことを確認するとよいでしょう。ついでに、依存関係のバージョンも全体的に確認したほうがよいかもしれません。お役に立てれば幸いです！さらに詳しく調べたい場合はお知らせください。

</td>

<td width="50%">

## 適用後

> 認証失敗の箇所は `src/auth.ts:42` です。`verifyToken` が古い `jsonwebtoken` API を使っています。まだ変更は行っていません。
>
> - 根拠：トークン検証はこの呼び出し箇所で失敗しています。
> - リスク：互換性のある対象バージョンは未確認です。
>
> 次の手順：依存関係を更新して `npm test -- auth.spec.ts` を実行する前に、対応する `jsonwebtoken` バージョンを確認します。

</td>
</tr>
</table>


## ルール

ルールは 10 個です。全文は [SKILL.md](../../skills/i-have-adhd/SKILL.md) にあります。

1. 検証済みの結果、必要な判断、または次の行動を最初に示す。
2. 根拠、不明点、リスク、検証結果を必要に応じて重ねる。
3. 順番に実行する手順だけに番号を付ける。
4. 重要な情報を省略せず、要約の件数を元の項目と照合する。
5. 必要な場合だけ状態を戻し、残作業がなければ次の行動を作らない。
6. 時間が判断に影響し、信頼できる根拠がある場合だけ見積もる。
7. 完了内容と検証結果を見える形にする。
8. エラーを淡々と報告し、確認済みの原因と未証明の原因を分ける。
9. 重要な副次的問題を隠さず、脱線を抑える。
10. 冗長な前置きや繰り返しを除き、回答が完了したら終える。

## カスタマイズ

リポジトリを Fork し、`skills/i-have-adhd/SKILL.md` を編集してから、自分のコピーに切り替えます。

```bash
claude plugin uninstall i-have-adhd            # まず上流のコピーを削除：
claude plugin marketplace remove i-have-adhd   # fork と上流では同じ名前が使われる
claude plugin marketplace add <your-username>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

Claude Code を再起動し、`/i-have-adhd` をもう一度呼び出してください。

## クレジット

J. Russell Ramsay と Anthony L. Rostain による *The Adult ADHD Tool Kit* を大まかに参考にしています。人間が一日をどう整理すべきかではなく、LLM がどう応答すべきかに合わせて改変したものです。

## ライセンス

MIT。

「良い質問ですね！」を一度スクロールして読み飛ばさずに済んだなら、Star ⭐ をお願いします。
