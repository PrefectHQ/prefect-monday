from prefect import flow

from prefect_monday.tasks import (
    goodbye_prefect_monday,
    hello_prefect_monday,
)


def test_hello_prefect_monday():
    @flow
    def test_flow():
        return hello_prefect_monday()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-monday!"


def goodbye_hello_prefect_monday():
    @flow
    def test_flow():
        return goodbye_prefect_monday()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-monday!"
