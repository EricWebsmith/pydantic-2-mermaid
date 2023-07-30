# we avoid pydantic_1_mermaid and pydantic_2_mermaid so that we can use both versions
from .__main__ import main  # noqa F401
from .mermaid_generator import MermaidGenerator  # noqa F401
from .models import *  # noqa F401
