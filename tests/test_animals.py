from examples import animals

from src import MermaidGenerator, Relations


def test_animals():
    mg = MermaidGenerator(animals)
    chart = mg.generate_chart(relations=Relations.Inheritance)
    with open("./examples/animals.md", mode="w") as f:
        f.write(chart)
        f.close()


def test_animals_brids():
    mg = MermaidGenerator(animals)
    chart = mg.generate_chart(root='Bird', relations=Relations.Inheritance)
    with open("./examples/animals_birds.md", mode="w") as f:
        f.write(chart)
        f.close()
