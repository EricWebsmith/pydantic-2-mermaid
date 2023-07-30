from pydantic_2_mermaid.__main__ import main
from pytest import MonkeyPatch

def test_main(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('sys.argv', ['pydantic-2-mermaid', '-m', 'examples.animals', '-o', 'examples/animals.md'])
    main()
    monkeypatch.undo()


def test_main_path(monkeypatch: MonkeyPatch):
    monkeypatch.setattr('sys.argv', ['pydantic-2-mermaid', '-m', './examples/animals.py', '-o', 'examples/animals.md'])
    main()
    monkeypatch.undo()
