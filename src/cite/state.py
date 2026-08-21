from typing import TypedDict, Annotated

from langgraph.graph.message import add_messages


class CiteState(TypedDict, total=False):
    messages: Annotated[list, add_messages]
    question: str
    documents: list[str]
    rewrite_count: int
    generation: str
    skip_retrieve: bool
