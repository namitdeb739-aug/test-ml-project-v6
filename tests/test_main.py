import pytest

from my_project.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from my-project!" in captured.out
