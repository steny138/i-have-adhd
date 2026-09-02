<p align="center">
  <img src="../../logo.png" alt="i-have-adhd" width="140" />
</p>
<p align="center">
  <strong align="center">ADHD 친화적인 출력. ADHD 진단은 필요 없어요!</strong>
</p>
<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/ayghri/i-have-adhd?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="../../README.md" title="English" aria-label="English">🇬🇧</a> ·
  <a href="README.zh-CN.md" title="简体中文" aria-label="简体中文">🇨🇳</a> ·
  <a href="README.pt-BR.md" title="Português (Brasil)" aria-label="Português (Brasil)">🇧🇷</a> ·
  <a href="README.ja.md" title="日本語" aria-label="日本語">🇯🇵</a> ·
  <a href="README.vi.md" title="Tiếng Việt" aria-label="Tiếng Việt">🇻🇳</a> ·
  <strong title="한국어" aria-label="한국어">🇰🇷</strong>
</p>


## 설치

🔗 [설치 안내](../install/INSTALL.ko.md)

## 무슨 일을 하나

검증된 결과, 필요한 결정 또는 다음 행동을 먼저 보여 주면서 근거와 안전 조건을 숨기지 않도록 하는 스킬입니다. "도움이 되었기를!" 같은 군더더기는 없습니다.


## 무엇이 달라지는가


<table>
<tr>
<td width="50%">

## 사용 전

> 좋은 질문이네요! 한번 생각해볼게요. 인증 흐름에는 미들웨어, 토큰 검증, 쿠키 처리 같은 여러 부분이 있어요. `src/auth.ts`를 살펴보면 `verifyToken` 함수(42~58번째 줄 근처)가 구버전 `jsonwebtoken` API를 쓰는 것 같아요. 한 가지 방법은 패키지를 업데이트하고 그 함수를 다시 작성하는 거예요. 변경 후에는 인증 테스트를 돌려서 문제가 없는지 확인해야 해요. 아, 그리고 하나 더, 전체 의존성 버전도 살펴보시면 좋을 것 같아요. 도움이 되었기를! 더 깊이 파고 싶으시면 알려주세요.

</td>

<td width="50%">

## 사용 후

> 인증 실패 지점은 `src/auth.ts:42`입니다. `verifyToken`이 이전 `jsonwebtoken` API를 사용합니다. 아직 변경하지 않았습니다.
>
> - 근거: 토큰 검증이 이 호출 지점에서 실패합니다.
> - 위험: 호환되는 대상 버전은 아직 확인되지 않았습니다.
>
> 다음 단계: 의존성을 업데이트하고 `npm test -- auth.spec.ts`를 실행하기 전에 지원되는 `jsonwebtoken` 버전을 확인합니다.

</td>
</tr>
</table>


## 규칙

10가지 규칙. 전문은 [SKILL.md](../../skills/i-have-adhd/SKILL.md)에 있습니다.

1. 검증된 결과, 필요한 결정 또는 다음 행동을 먼저 제시합니다.
2. 필요한 근거, 미확인 사항, 위험과 검증 결과를 이어서 제시합니다.
3. 순서대로 실행해야 하는 단계에만 번호를 붙입니다.
4. 중요한 정보를 생략하지 않고 요약 수치를 원본 항목과 대조합니다.
5. 필요할 때만 상태를 복원하고, 남은 일이 없으면 다음 작업을 만들지 않습니다.
6. 시간이 결정에 영향을 주고 신뢰할 근거가 있을 때만 추정합니다.
7. 완료 내용과 검증 결과를 분명히 보여 줍니다.
8. 오류를 담담하게 보고하고 확인된 원인과 미확인 원인을 구분합니다.
9. 중요한 부수 문제를 숨기지 않으면서 주제 이탈을 통제합니다.
10. 불필요한 서론과 반복을 제거하고 답변이 끝나면 종료합니다.

## 커스터마이즈

저장소를 포크해 `skills/i-have-adhd/SKILL.md`를 수정한 다음, 본인 복사본으로 교체하세요:

```bash
claude plugin uninstall i-have-adhd            # 먼저 업스트림 버전 제거
claude plugin marketplace remove i-have-adhd   # 포크와 업스트림이 같은 이름을 씁니다
claude plugin marketplace add <your-username>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

Claude Code를 재시작한 뒤 `/i-have-adhd`를 다시 호출하세요.

## 크레딧

J. Russell Ramsay와 Anthony L. Rostain의 *The Adult ADHD Tool Kit*을 느슨하게 참고했습니다. 사람이 하루를 어떻게 꾸려야 하는가가 아니라 **LLM이 어떻게 응답해야 하는가**에 맞춰 재해석했습니다.

## 라이선스

MIT.

"좋은 질문이네요!" 없는 답변을 한 번이라도 받았다면 Star ⭐ 부탁드립니다.
