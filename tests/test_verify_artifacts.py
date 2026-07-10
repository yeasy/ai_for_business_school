import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.verify_artifacts import verify_pdf, write_checksums


class VerifyArtifactsTests(unittest.TestCase):
    def test_write_checksums_is_portable_and_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            first = directory / "b.pdf"
            second = directory / "a.pdf"
            first.write_bytes(b"second")
            second.write_bytes(b"first")
            manifest = directory / "SHA256SUMS"

            write_checksums([first, second], manifest)

            expected = (
                f"{hashlib.sha256(b'first').hexdigest()}  a.pdf\n"
                f"{hashlib.sha256(b'second').hexdigest()}  b.pdf\n"
            )
            self.assertEqual(manifest.read_text(encoding="utf-8"), expected)

    def test_verify_pdf_rejects_non_pdf_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "book.pdf"
            path.write_bytes(b"not a PDF")
            with self.assertRaises(SystemExit):
                verify_pdf(path, "Expected")

    @mock.patch("tools.verify_artifacts.shutil.which", return_value="/usr/bin/tool")
    @mock.patch("tools.verify_artifacts.command_output")
    def test_verify_pdf_accepts_title_on_cover_when_metadata_is_empty(self, command, _which):
        command.side_effect = ["Pages: 10\n", "Expected Book Title\n"]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "book.pdf"
            path.write_bytes(b"%PDF-1.7\nminimal")
            verify_pdf(path, "Expected Book Title")


if __name__ == "__main__":
    unittest.main()
