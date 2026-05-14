from typing import Annotated, Literal

from pydantic import BaseModel, Field


class UserQuery(BaseModel):
    query: Annotated[
        str,
        Field(
            min_length=1,
            description="The original question asked by the user.",
        ),
    ]
    user_id: str
    session_id: str | None = None
    intent: Literal["chat", "search", "tool_use", "evaluation"] = "chat"


class RetrievedChunk(BaseModel):
    chunk_id: str
    source: str
    text: Annotated[
        str, Field(min_length=1, description="The retrieved text content. ")
    ]
    score: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="Relevance score between 0.0  and 1.0",
        ),
    ]
    metadata: dict[str, str] = {}


class ToolCall(BaseModel):
    tool_name: Literal["search", "calculator", "retriever", "email", "calendar"]

    arguments: dict[str, str | int | float | bool]

    status: Literal["pending", "running", "success", "failed"] = "pending"

    result: str | None = None


class AgentState(BaseModel):
    user_query: UserQuery

    retrieved_chunks: list[RetrievedChunk] = []

    tool_calls: list[ToolCall] = []

    draft_answer: str | None = None

    final_answer: str | None = None

    step_count: Annotated[
        int,
        Field(
            ge=0,
            description="Number of reasoning/tool-use steps taken by the agent.",
        ),
    ] = 0


class EvaluationResult(BaseModel):
    query_id: str

    answer: str

    faithfulness_score: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="How grounded the answer is in retrieved context.",
        ),
    ]

    helpfulness_score: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="How useful the answer is for the user.",
        ),
    ]

    passed: bool

    feedback: str | None = None


if __name__ == "__main__":
    user_query = UserQuery(
        query="What is RAG?",
        user_id="user_123",
        session_id="session_abc",
        intent="search",
    )

    chunk = RetrievedChunk(
        chunk_id="chunk_001",
        source="rag_notes.md",
        text="RAG stands for Retrieval-Augmented Generation.",
        score=0.92,
        metadata={"page": "1", "topic": "RAG"},
    )

    # bad_chunk = RetrievedChunk(
    #     chunk_id="chunk_bad",
    #     source="bad_source.md",
    #     text="Invalid score example.",
    #     score=1.5,
    # )

    tool_call = ToolCall(
        tool_name="retriever",
        arguments={"query": "What is RAG?", "top_k": 3},
        status="success",
        result="Found 3 relevant chunks.",
    )

    agent_state = AgentState(
        user_query=user_query,
        retrieved_chunks=[chunk],
        tool_calls=[tool_call],
        draft_answer="RAG combines retrieval with generation.",
        final_answer=(
            "RAG stands for Retrieval-Augmented Generation. "
            "It retrieves relevant context before generating an answer."
        ),
        step_count=2,
    )

    evaluation = EvaluationResult(
        query_id="query_001",
        answer=agent_state.final_answer or "",
        faithfulness_score=0.95,
        helpfulness_score=0.9,
        passed=True,
        feedback="Answer is grounded and beginner-friendly.",
    )

    print("USER QUERY:")

    print(user_query)

    print("\nRETRIEVED CHUNK:")

    print(chunk)

    # print(bad_chunk)

    print("\nTOOL CALL:")

    print(tool_call)

    print("\nAGENT STATE AS DICT:")

    print(agent_state.model_dump())

    print("\nEVALUATION:")

    print(evaluation)
