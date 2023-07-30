from pydantic_2_mermaid import MermaidGenerator, Relations
from examples import country

def test_country():
    mg = MermaidGenerator(country)
    mg.generate_chart(root="Country", relations=Relations.Dependency)