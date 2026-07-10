import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"
FULL_ACTION_SHA = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")
EXPECTED_WORKFLOWS = (
    "ci.yaml",
    "preview-pdf.yml",
    "auto-release.yml",
    "dependabot-automerge.yml",
)


class ReleaseWorkflowTests(unittest.TestCase):
    def workflow_text(self, name):
        path = WORKFLOW_DIR / name
        self.assertTrue(path.is_file(), path)
        return path.read_text(encoding="utf-8")

    def test_actions_are_immutable_and_checkout_drops_credentials(self):
        failures = []
        for name in EXPECTED_WORKFLOWS:
            text = self.workflow_text(name)
            lines = text.splitlines()
            for number, line in enumerate(lines, 1):
                match = re.search(r"\buses:\s*([^\s#]+)(?:\s+#\s*(\S+))?", line)
                if match:
                    action, version = match.groups()
                    if not FULL_ACTION_SHA.fullmatch(action) or not version or not version.startswith("v"):
                        failures.append(f"{name}:{number}: {line.strip()}")
                if "uses: actions/checkout@" in line:
                    step = "\n".join(lines[number - 1 : number + 7])
                    if "persist-credentials: false" not in step:
                        failures.append(f"{name}:{number}: checkout credentials persist")
        self.assertEqual(failures, [])

    def test_build_and_publish_permissions_are_separated(self):
        ci = self.workflow_text("ci.yaml")
        auto = self.workflow_text("auto-release.yml")
        preview = self.workflow_text("preview-pdf.yml")

        self.assertRegex(ci, r"(?ms)^  build:\n    permissions:\n      contents: read\b")
        self.assertRegex(auto, r"(?ms)^  build:\n    permissions:\n      contents: read\b")
        self.assertRegex(
            auto,
            r"(?ms)^  release:.*?permissions:\n      contents: write\n      id-token: write\n      attestations: write\b.*?needs: build",
        )
        self.assertRegex(preview, r"(?ms)^  build:\n    permissions:\n      contents: read\b")
        self.assertRegex(
            preview,
            r"(?ms)^  publish:.*?permissions:\n      contents: write\b.*?needs: build",
        )

    def test_downloads_and_artifacts_have_integrity_gates(self):
        for name in ("ci.yaml", "preview-pdf.yml", "auto-release.yml"):
            text = self.workflow_text(name)
            self.assertIn("MDPRESS_SHA256", text, name)
            self.assertIn("sha256sum -c -", text, name)
            self.assertIn("tools/verify_artifacts.py", text, name)
            self.assertIn("SHA256SUMS", text, name)
            self.assertNotIn("continue-on-error: true", text, name)
        auto = self.workflow_text("auto-release.yml")
        self.assertIn(
            "actions/attest-build-provenance@0f67c3f4856b2e3261c31976d6725780e5e4c373 # v4.1.1",
            auto,
        )

    def test_dependabot_configuration_and_guarded_automerge_exist(self):
        config = ROOT / ".github" / "dependabot.yml"
        self.assertTrue(config.is_file())
        text = config.read_text(encoding="utf-8")
        self.assertIn("github-actions", text)
        workflow = self.workflow_text("dependabot-automerge.yml")
        self.assertIn("dependabot/fetch-metadata@25dd0e34f4fe68f24cc83900b1fe3fe149efef98 # v3.1.0", workflow)


if __name__ == "__main__":
    unittest.main()
