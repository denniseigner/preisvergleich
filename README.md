```
python3.12 -m venv .venv
source .venv/bin/activate
pip install uv
uv pip install -r requirements.txt -r requirements-dev.txt -r requirements-test.txt
pre-commit install
```
