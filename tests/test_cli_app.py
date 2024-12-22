import os
import pytest
import subprocess

# Zadanie 3

@pytest.fixture
def setup_files(tmp_path):
    src_file = tmp_path / "source.txt"
    dst_file = tmp_path / "destination.txt"
    src_file.write_text("Dzien dobry!")
    return src_file, dst_file

def test_copy_file(setup_files):
    src_file, dst_file = setup_files
    subprocess.run(["python3", "cli_app.py", "copy", str(src_file), str(dst_file)])
    assert dst_file.exists()
    assert dst_file.read_text() == "Dzien dobry!"

def test_delete_file(setup_files):
    src_file, dst_file = setup_files
    subprocess.run(["python3", "cli_app.py", "delete", str(src_file), str(dst_file)])
    assert not dst_file.exists()