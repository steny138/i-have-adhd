<p align="center">
  <img src="../../logo.png" alt="i-have-adhd" width="140" />
</p>
<p align="center">
  <strong align="center">对 ADHD 友好的输出。无需确诊 ADHD！</strong>
</p>
<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/ayghri/i-have-adhd?style=flat" alt="许可证"></a>
</p>

<p align="center">
  <a href="../../README.md" title="English" aria-label="English">🇬🇧</a> ·
  <strong title="简体中文" aria-label="简体中文">🇨🇳</strong> ·
  <a href="README.pt-BR.md" title="Português (Brasil)" aria-label="Português (Brasil)">🇧🇷</a> ·
  <a href="README.ja.md" title="日本語" aria-label="日本語">🇯🇵</a> ·
  <a href="README.vi.md" title="Tiếng Việt" aria-label="Tiếng Việt">🇻🇳</a> ·
  <a href="README.ko.md" title="한국어" aria-label="한국어">🇰🇷</a>
</p>


## 安装

🔗 [安装说明](../install/INSTALL.zh-CN.md)

## 功能

这是一个让编程助手先给出已验证结论、所需决定或下一步行动，同时不隐藏证据与安全限制的技能。不说“希望这能帮到你！”


## 有什么变化


<table>
<tr>
<td width="50%">

## 之前

> 问得好！让我想一想。你的身份验证流程包含几个环节：中间件、令牌验证和 Cookie 处理。查看 `src/auth.ts` 后，`verifyToken` 函数（大约第 42–58 行）似乎使用了旧版 `jsonwebtoken` API。一种做法是升级这个包并重写该函数。完成修改后，你需要运行身份验证测试，确认没有破坏任何功能。顺便一提，你可能还想整体检查一下依赖版本。希望这能帮到你！如果你想进一步研究，请告诉我。

</td>

<td width="50%">

## 之后

> 身份验证失败点位于 `src/auth.ts:42`：`verifyToken` 使用了旧版 `jsonwebtoken` API。目前尚未进行修改。
>
> - 证据：令牌验证在这个调用点失败。
> - 风险：尚未确认兼容的目标版本。
>
> 下一步：先确认支持的 `jsonwebtoken` 版本，再更新依赖并运行 `npm test -- auth.spec.ts`。

</td>
</tr>
</table>


## 规则

共 10 条规则。完整内容见 [SKILL.md](../../skills/i-have-adhd/SKILL.md)。

1. 先给出已验证的结论、所需决定或下一步行动。
2. 按需补充证据、未知项、风险和验证结果。
3. 只有必须依序执行的操作才使用编号。
4. 保留所有重要信息，并将摘要数量与原始项目逐项核对。
5. 只在有帮助时恢复状态；完成后不要虚构下一项任务。
6. 只有时间会影响决定且有可靠依据时才进行估算。
7. 清楚展示完成内容和验证结果。
8. 客观报告错误，并区分已确认原因与未经证实的推测。
9. 控制离题内容，但不隐藏重要的附带问题。
10. 删除不必要的开场和重复；回答完整后结束。

## 自定义

Fork 此仓库，编辑 `skills/i-have-adhd/SKILL.md`，然后换成你的副本：

```bash
claude plugin uninstall i-have-adhd            # 先移除上游副本：
claude plugin marketplace remove i-have-adhd   # fork 与上游使用相同名称
claude plugin marketplace add <your-username>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

重启 Claude Code，然后再次调用 `/i-have-adhd`。

## 致谢

内容大致参考 J. Russell Ramsay 和 Anthony L. Rostain 所著的 *The Adult ADHD Tool Kit*。本技能针对 LLM 应如何回应进行了改编，而不是教人们如何安排日常生活。

## 许可证

MIT。

如果它让你少滚动一次屏幕、跳过一句“问得好！”，请点亮 Star ⭐
