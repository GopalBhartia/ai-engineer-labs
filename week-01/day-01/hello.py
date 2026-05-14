from pathlib import Path


def greet_user(name: str) -> str:
    """Return a greeting message for the user."""
    return f"Hello, {name}! Welcome to your AI Engineer roadmap."


def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parent.parent


def main() -> None:
    message = greet_user("Gopal")
    project_root = get_project_root()

    print(message)
    print(f"Project root: {project_root}")


if __name__ == "__main__":
    main()
