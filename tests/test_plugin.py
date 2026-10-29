import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "plugins/buku-program-ai"

class PluginTests(unittest.TestCase):
    def test_manifest(self):
        manifest = json.loads((PACKAGE/"plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "buku-program-ai")
        self.assertEqual(manifest["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        self.assertTrue((PACKAGE/"skills/buku-program/SKILL.md").is_file())

    def test_marketplace_path(self):
        catalog = json.loads((ROOT/".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        entry = catalog["plugins"][0]
        self.assertEqual((ROOT/entry["source"]["path"]).resolve(), PACKAGE.resolve())
        self.assertEqual(entry["policy"]["installation"], "AVAILABLE")

    def test_bundled_images_identical(self):
        for name in ["contoh-helaian-luar.png", "contoh-helaian-dalam.png"]:
            source = (ROOT/"assets"/name).read_bytes()
            bundled = (PACKAGE/"skills/buku-program/assets"/name).read_bytes()
            self.assertEqual(hashlib.sha256(source).digest(), hashlib.sha256(bundled).digest())

    def test_workflow_self_contained(self):
        text = (PACKAGE/"skills/buku-program/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname:"))
        self.assertIn("tanpa meminta pengesahan tambahan", text)
        self.assertNotIn("raw.githubusercontent.com", text)
        self.assertNotIn("drive.google.com", text)
        self.assertNotIn("LANGKAH PERTAMA — GUNAKAN CHATGPT WORK", text)
        for name in ["contoh-helaian-luar.png", "contoh-helaian-dalam.png"]:
            self.assertIn("assets/"+name, text)

if __name__ == "__main__":
    unittest.main()
