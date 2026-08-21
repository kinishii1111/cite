from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from cite.state import CiteState
from cite.route import route
from cite.retrieve import retrieve
from cite.grade import grade_docs
from cite.rewrite import rewrite
from cite.generate import generate
from cite.ground import ground


def build_graph():
    builder = StateGraph(CiteState)

    builder.add_node("route", route)
    builder.add_node("retrieve", retrieve)
    builder.add_node("grade_docs", grade_docs)
    builder.add_node("rewrite", rewrite)
    builder.add_node("generate", generate)
    builder.add_node("ground", ground)

    def after_route(state: CiteState) -> str:
        return "generate" if state.get("skip_retrieve") else "retrieve"

    def after_grade(state: CiteState) -> str:
        if state.get("documents"):
            return "generate"
        return "rewrite" if state.get("rewrite_count", 0) < 2 else "generate"

    builder.add_edge(START, "route")
    builder.add_conditional_edges(
        "route", after_route, {"generate": "generate", "retrieve": "retrieve"}
    )
    builder.add_edge("retrieve", "grade_docs")
    builder.add_conditional_edges(
        "grade_docs", after_grade, {"generate": "generate", "rewrite": "rewrite"}
    )
    builder.add_edge("rewrite", "retrieve")
    builder.add_edge("generate", "ground")
    builder.add_edge("ground", END)

    return builder.compile(checkpointer=MemorySaver())
