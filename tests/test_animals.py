from pydantic_2_mermaid import MermaidGenerator, Relations
from examples import animals

def test_country():
    mg = MermaidGenerator(animals)
    mg.generate_chart(root="Country", relations=Relations.Dependency)