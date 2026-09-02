import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class OmpPackageTest(unittest.TestCase):
    def setUp(self):
        self.package = json.loads((ROOT / "package.json").read_text(encoding="utf8"))

    def test_omp_and_pi_extension_manifests_are_declared(self):
        extension = ["./extensions/i-have-adhd.ts"]
        self.assertEqual({"extensions": extension}, self.package["omp"])
        self.assertEqual(
            {"extensions": extension, "skills": ["./skills"]},
            self.package["pi"],
        )

    def test_skill_remains_explicitly_invoked(self):
        skill = (ROOT / "skills" / "i-have-adhd" / "SKILL.md").read_text(
            encoding="utf8"
        )
        frontmatter = skill.split("---\n", 2)[1]
        self.assertIn("name: i-have-adhd", frontmatter)
        self.assertIn("disable-model-invocation: true", frontmatter)

    def test_codex_marketplace_installs_the_fork(self):
        marketplace = json.loads(
            (ROOT / ".agents" / "plugins" / "marketplace.json").read_text(
                encoding="utf8"
            )
        )

        self.assertEqual(
            "https://github.com/steny138/i-have-adhd.git",
            marketplace["plugins"][0]["source"]["url"],
        )

    def test_skill_mirror_matches_canonical(self):
        canonical = (ROOT / "skills" / "i-have-adhd" / "SKILL.md").read_text(
            encoding="utf8"
        )
        mirror = (
            ROOT / ".cursor" / "skills" / "i-have-adhd" / "SKILL.md"
        ).read_text(encoding="utf8")

        self.assertEqual(canonical, mirror)

    def test_embedded_prompts_do_not_restore_rigid_upstream_rules(self):
        prompt_paths = [
            ROOT / "README.md",
            ROOT / "INSTALL.md",
            ROOT / "skills" / "i-have-adhd" / "agents" / "gemini.toml",
            *sorted((ROOT / ".github" / "install").glob("INSTALL.*.md")),
            *sorted((ROOT / ".github" / "readme").glob("README.*.md")),
        ]
        rigid_phrases = (
            "Restate state every turn",
            "Restate progress each turn",
            "Cap lists at 5 items",
            "End with one concrete next action",
            "Give time estimates in concrete units",
            "ターンごとに現在の状態を言い直す",
            "リストは 5 項目までにする",
            "매 턴마다 현재 상태 다시 알리기",
            "목록은 최대 5개 항목",
            "Reafirme o estado atual a cada turno",
            "Limite listas a 5 itens",
            "Nhắc lại trạng thái hiện tại ở mỗi lượt",
            "Giới hạn danh sách tối đa 5 mục",
            "每轮都重述当前状态",
            "每个列表最多 5 项",
        )

        for path in prompt_paths:
            content = path.read_text(encoding="utf8")
            for phrase in rigid_phrases:
                with self.subTest(path=path, phrase=phrase):
                    self.assertNotIn(phrase, content)

    def test_inventory_prompts_require_summary_count_verification(self):
        prompt_paths = [
            ROOT / "skills" / "i-have-adhd" / "SKILL.md",
            ROOT / ".cursor" / "skills" / "i-have-adhd" / "SKILL.md",
            ROOT / "skills" / "i-have-adhd" / "agents" / "gemini.toml",
            ROOT / "INSTALL.md",
            *sorted((ROOT / ".github" / "install").glob("INSTALL.*.md")),
        ]

        for path in prompt_paths:
            with self.subTest(path=path):
                self.assertIn(
                    "Verify summary counts against source items.",
                    path.read_text(encoding="utf8"),
                )


if __name__ == "__main__":
    unittest.main()
