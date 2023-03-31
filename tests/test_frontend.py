from contextlib import contextmanager
from time import sleep

import pytest
from playwright.sync_api import Page, expect

LOCAL_TEST = False

PORT = "8503" if LOCAL_TEST else "8699"

@pytest.fixture(scope="module", autouse=True)
def before_module():
    # Run the streamlit app before each module
    with run_streamlit():
        yield

@pytest.fixture(scope="function", autouse=True)
def before_test(page: Page):
    page.goto(f"localhost:{PORT}")


@contextmanager
def run_streamlit():
    """Run the streamlit app at main.py on port 8699"""
    import subprocess

    if LOCAL_TEST:
        try:
            yield 1
        finally:
            pass
    else:
        p = subprocess.Popen(
            [
                "streamlit",
                "run",
                "main.py",
                "--server.port",
                PORT,
                "--server.headless",
                "true",
            ]
        )

        sleep(5)

        try:
            yield 1
        finally:
            p.kill()
