import sys

if sys.version_info >= (3, 9):
    from types import ModuleType

    import pytest

    from pydantic_mermaid import MermaidGenerator, Relations
    from tests.mock.py_3_9 import annotated_example
    from tests.utils import compare_chart_and_markdown

    @pytest.mark.parametrize(
        ("module", "root", "relations", "expected_path"),
        [
            (annotated_example, "", Relations.Dependency, "tests/mock/py_3_9/annotated_example.md"),
        ],
    )
    def test_gen(module: ModuleType, root: str, relations: Relations, expected_path: str) -> None:
        mg = MermaidGenerator(module)
        chart = mg.generate_chart(root=root, relations=relations)
        compare_chart_and_markdown(chart, expected_path)
