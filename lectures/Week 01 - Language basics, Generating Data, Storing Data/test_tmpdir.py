"""Examples that demonstrate pytest's temporary-path fixtures."""


def test_needsfiles(tmp_path):
    """Write and read a file inside the automatically managed directory."""

    text_file = tmp_path / "example.txt"
    payload = "sample text"
    text_file.write_text(payload, encoding="utf-8")
    assert text_file.read_text(encoding="utf-8") == payload
