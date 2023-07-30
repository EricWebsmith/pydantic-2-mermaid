# we avoid pydantic_1_mermaid and pydantic_2_mermaid so that we can use both versions
from pydantic_mermaid.__main__ import main  # noqa F401
from pydantic_mermaid.mermaid_generator import MermaidGenerator  # noqa F401
from pydantic_mermaid.models import *  # noqa F401
