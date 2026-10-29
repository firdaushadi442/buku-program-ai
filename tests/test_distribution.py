import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DistributionTests(unittest.TestCase):
    def test_required_files(self):
        for name in ["README.md", "SKILL.md", "PROMPT-BUKU-PROGRAM.txt", "LICENSE", "SECURITY.md", "CHECKLIST.md", "EVALUATION.md", "templates/maklumat-program.txt", "examples/program-rekaan.txt"]:
            with self.subTest(name=name):
                self.assertTrue((ROOT/name).is_file())
                self.assertTrue((ROOT/name).read_text(encoding="utf-8").strip())

    def test_local_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent/target.split("#")[0]).is_file(), (path.name,target))

    def test_frontmatter(self):
        text=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: buku-program-ai",text)
        self.assertIn("description:",text.split("---")[1])

    def test_prompt_gates(self):
        text=(ROOT/"PROMPT-BUKU-PROGRAM.txt").read_text(encoding="utf-8")
        for stage in range(1,7):
            self.assertIn(f"PERINGKAT {stage}",text)
        for phrase in ["297 × 210 mm", "halaman 4 / kulit belakang di KIRI", "halaman 1 / kulit depan di KANAN", "halaman 2 di KIRI", "halaman 3 di KANAN", "tanpa meminta pengesahan tambahan", "Jangan mereka-reka", "Jika fungsi itu tidak tersedia", "bukan bukti", "LETAK LOGO DI SINI"]:
            self.assertIn(phrase,text)

    def test_no_personal_paths_or_integrations(self):
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in (".md", ".txt"):
                continue
            text=path.read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"[A-Za-z]:[\\/]Users[\\/]|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",text),path.name)
            public_free = text.replace("https://github.com/firdaushadi442/buku-program-ai", "PUBLIC_REPO").replace("https://raw.githubusercontent.com/firdaushadi442/buku-program-ai/", "PUBLIC_RAW/")
            for forbidden in ["photocraft", "3456", "DevToolsActivePort", "firdaushadi442", "SMAUJ"]:
                self.assertNotIn(forbidden.lower(),public_free.lower(),path.name)

    def test_supplied_links_and_approved_images(self):
        for name in ["README.md", "PROMPT-BUKU-PROGRAM.txt"]:
            text = (ROOT/name).read_text(encoding="utf-8")
            self.assertNotIn("drive.google.com", text)
            for filename in ["contoh-helaian-luar.jpg", "contoh-helaian-dalam.jpg"]:
                self.assertIn("https://raw.githubusercontent.com/firdaushadi442/buku-program-ai/main/assets/" + filename, text)
        images = [p for p in ROOT.rglob("*") if ".git" not in p.parts and p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".gif")]
        self.assertEqual({p.relative_to(ROOT).as_posix() for p in images}, {"assets/contoh-helaian-luar.jpg", "assets/contoh-helaian-dalam.jpg"})
        for p in images:
            self.assertTrue(p.read_bytes().startswith(b"\xff\xd8\xff"))
        self.assertTrue((ROOT/"assets/NOTICE.md").is_file())

    def test_limitations_are_explicit(self):
        text=(ROOT/"README.md").read_text(encoding="utf-8")
        self.assertIn("belum diuji hujung-ke-hujung",text)
        self.assertIn("bukan automasi pelayar",text)
        self.assertIn("bukan Custom GPT",text)

if __name__ == "__main__":
    unittest.main()
