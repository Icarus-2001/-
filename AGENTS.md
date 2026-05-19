# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

This is a single-file Streamlit app (`app.py`) — "美甲视界" (Nail Art Vision), an AI nail art virtual try-on and intelligent operations prototype. No database, no external AI service integration (placeholders only), no Docker.

### Running the app

```bash
streamlit run app.py --server.port 8501 --server.headless true
```

The app will be available at `http://localhost:8501`.

### Linting

No project-level linter config exists. Use `ruff` for both lint and format checks:

```bash
python3 -m ruff check app.py
python3 -m ruff format --check app.py
```

Note: `ruff format --check` currently reports the file needs reformatting (trailing whitespace in multiline strings). This is a pre-existing state.

### Testing

No automated test suite exists in this repository. Validate changes by importing the module (`python3 -c "import app"`) and running the Streamlit app manually.

### Dependencies

All dependencies are in `requirements.txt` (streamlit, pandas, plotly). Install with:

```bash
pip install -r requirements.txt
```
