from pathlib import Path

def test_canonical_files_exist():
    for f in ["README.md", "STATUS.md", "FREEZE.md", "CITATION.cff", "URF-P-0002.tex", "URF-P-0002.pdf"]:
        assert Path(f).exists(), f

def test_no_tracked_latex_build_outputs():
    forbidden = [
        "URF-P-0002.aux",
        "URF-P-0002.fdb_latexmk",
        "URF-P-0002.fls",
        "URF-P-0002.log",
        "URF-P-0002.out",
    ]
    for f in forbidden:
        assert not Path(f).exists(), f

def test_status_matches_identity():
    txt = Path("STATUS.md").read_text()
    assert "URF-P-0002" in txt
    assert "manuscript repository" in txt
