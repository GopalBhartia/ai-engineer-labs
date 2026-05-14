from typing import Annotated, Literal, Protocol, TypedDict


# basic type hint
def greet_user(name: str) -> str:
    return f"Hello, {name}!"


# list type hint
def avg_score(scores: list[int]) -> int:
    return sum(scores) // len(scores)


# Optional type hint
def get_user_info(user: dict[str, str]) -> str:
    return f"User {user['name']} is {user['age']} years old."


def find_user_email(userid: int) -> str | None:
    if userid == 1:
        return "gopal@example.com"
    # else:
    #     return None


# Literal type hint
def set_agent_mode(mode: Literal["chat", "search", "tool_use"]) -> str:
    return f"Agent is set to {mode} mode."


# TypedDict type hint
class LearnerProfile(TypedDict):
    name: str
    topic: str
    daily_hours: int
    is_beginner: bool


def summarize_learner(profile: LearnerProfile) -> str:
    return (
        f"{profile['name']} is learning {profile['topic']}. "
        f"They spend {profile['daily_hours']} hours per day on this topic. "
        f"Beginner: {profile['is_beginner']}"
    )


# Protocol type hint
class Tool(Protocol):
    name: str

    def run(self, query: str) -> str:
        ...  # This is called Ellipsis and it is a placeholder,
        #  it means the function is not implemented yet.


class SearchTool:
    name = "search"

    def run(self, query: str) -> str:
        return f"Searching the web for: {query}"


class CalculatorTool:
    name = "calculator"

    def run(self, query: str) -> str:
        return f"Calculating the results for: {query}"


def use_tool(tool: Tool, query: str) -> str:
    return tool.run(query)


# Annotated type hint
UserQuestion = Annotated[str, "The original question asked by the user"]
ConfidenceScore = Annotated[float, "A score between 0.0 and 1.0"]


def answer_question(
    question: UserQuestion,
    confidence: ConfidenceScore,
) -> str:
    return f"Answering: {question} with confidence {confidence}"


message = greet_user("Gopal")
print(message)

scores = [32, 63, 42, 81, 59, 15]
print(avg_score(scores))

user = {"name": "Gopal", "age": 25}
print(get_user_info(user))

email = find_user_email(2)
print(email)

print(set_agent_mode("chat"))
print(set_agent_mode("search"))

learner: LearnerProfile = {
    "name": "Gopal",
    "topic": "Agentic AI Engineering",
    "daily_hours": 6,
    "is_beginner": True,
}
print(summarize_learner(learner))

search_tool = SearchTool()
calculator_tool = CalculatorTool()
print(use_tool(search_tool, "Latest AI trends"))
print(use_tool(calculator_tool, "21 * 32"))

print(answer_question("What is RAG?", 0.92))
