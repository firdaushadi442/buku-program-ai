import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ComplianceChecks(unittest.TestCase):
    def test_privacy_disclosures(self):
        text=(ROOT/"PRIVACY.md").read_text(encoding="utf-8")
        for term in ["Kategori data", "tujuan", "Penerima", "Tempoh penyimpanan", "Kawalan pengguna", "OTP/MFA", "GitHub"]:
            self.assertIn(term,text)
    def test_listing_fields_and_icon(self):
        pkg=ROOT/"plugins/buku-program-ai"
        obj=json.loads((pkg/"plugin.json").read_text(encoding="utf-8"))
        i=obj["extensions"]["com.openai"]["interface"]
        self.assertLessEqual(len(i["shortDescription"]),30)
        for key in ["websiteURL","supportURL","privacyPolicyURL","termsOfServiceURL"]:
            self.assertTrue(i[key].startswith("https://"))
        self.assertTrue((pkg/i["logo"]).is_file())
    def test_restricted_data_and_platform_rules(self):
        for path in [ROOT/"PROMPT-BUKU-PROGRAM.txt",ROOT/"plugins/buku-program-ai/skills/buku-program/SKILL.md"]:
            text=path.read_text(encoding="utf-8")
            for term in ["data kad pembayaran", "rekod kesihatan dilindungi", "nombor pengenalan kerajaan", "kod OTP/MFA", "Hormati arahan platform", "Tiada iklan", "jangan ulang, ekstrak, analisis atau pindahkan"]:
                self.assertIn(term,text)
            self.assertNotIn("kecuali saya memintanya dan ia sesuai untuk penerbitan",text)
