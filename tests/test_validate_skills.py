"""Unit tests for the dependency-free skills validator."""
import sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skills import NAME_RE, parse_frontmatter

class FrontmatterTests(unittest.TestCase):
    def test_valid_frontmatter(self):
        values, body = parse_frontmatter("---\nname: sample-skill\ndescription: A sample skill.\nlicense: CC-BY-4.0\n---\n# Body\n")
        self.assertEqual(values["name"], "sample-skill")
        self.assertIn("# Body", body)
    def test_missing_closing_delimiter(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("---\nname: missing\n")
    def test_duplicate_keys_rejected(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("---\nname: first\nname: second\n---\n")
    def test_name_pattern(self):
        self.assertTrue(NAME_RE.fullmatch("valid-skill-2"))
        self.assertFalse(NAME_RE.fullmatch("-invalid"))
        self.assertFalse(NAME_RE.fullmatch("Invalid Name"))

if __name__ == "__main__":
    unittest.main()
