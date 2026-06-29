"""
Example of running the stateful agent with explicit Runner and SessionService.
This shows how sessions and state are managed under the hood.
"""
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from day1_section3_session_and_state.agent import root_agent


def run_with_session():
    """
    Demonstrates running an agent with explicit session management.

    This is what happens behind the scenes when you run `adk web` or `adk run`.
    """
    # Create an in-memory session service
    # This stores conversation history and state during the session
    session_service = InMemorySessionService()

    # Create a runner with the agent and session service
    runner = Runner(
        agent=root_agent,
        app_name="stateful_app",
        session_service=session_service
    )

    # Now you can use the runner to execute the agent
    # In practice, adk web/run handles this for you
    print("Runner created with InMemorySessionService")
    print("Session will persist state within this conversation")
    print("\nRun with: adk web day1_section3_session_and_state")


if __name__ == "__main__":
    run_with_session()
