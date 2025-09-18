import pytest
import subprocess
import json

def test_axiomhive_cli_help():
    result = subprocess.run(['python', 'axiomhive_cli.py', '--help'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'AXIOMHIVE ARC CLI Wrapper' in result.stdout

def test_cli_submission():
    result = subprocess.run(['python', 'axiomhive_cli.py', '--task_json', 'sample_arc.json', '--output', 'test_sub.json'], capture_output=True, text=True)
    assert result.returncode == 0
    assert json.load(open('test_sub.json'))['outputs']
