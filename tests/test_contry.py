from examples import country
from pydantic_mermaid import MermaidGenerator, Relations


def test_country():
    mg = MermaidGenerator(country)
    chart = mg.generate_chart(root="Country", relations=Relations.Dependency)
    with open("./examples/country.md", mode="w") as f:
        f.write(chart)
        f.close()
