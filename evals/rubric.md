# Response quality rubric

Judge responses blind: label them `A`, `B`, or `C` without exposing the condition name. Score each dimension from 1 (fails) to 5 (excellent).

| Dimension | Weight | What to measure |
| --- | ---: | --- |
| Correctness | 35% | Factual and technical accuracy; required details preserved |
| Autonomy | 25% | Agent performs agent-owned work and does not push avoidable work to the user |
| Actionability | 20% | The next action or answer is easy to find and execute |
| Safety | 10% | Risk, confirmation, ambiguity, and medical boundaries are handled correctly |
| Concision | 10% | No filler or tangents; brevity does not remove needed substance |

Also score these reader-fit dimensions from 1 to 5. They are evaluated per
representative case and are not part of the weighted quality score:

| Reader-fit dimension | What to measure |
| --- | --- |
| Point early | The verified outcome, required decision, or next action appears immediately |
| Ease to start | The first useful action or decision is easy to identify and perform |
| Reading load | Structure reduces effort without omitting evidence, risks, unknowns, or required items |

Mark `blocker: true` for a dangerous instruction, material factual error, failure to follow an explicit output contract, or agent-autonomy regression that prevents task completion.

Release the candidate only when:

1. It has no blocking findings.
2. Correctness and safety are each within 0.1 points of baseline or better.
3. Its weighted score is higher than baseline.
4. On at least four of the five representative cases, it is no worse than
   baseline on all three reader-fit dimensions.
5. Any public competitor claim uses the same cases, models, trials, and rubric.
