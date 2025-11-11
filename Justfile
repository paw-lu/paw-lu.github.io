# List all tasks
@_:
    just --list

# Generate site
[group('run')]
content *args:
    uv run pelican content {{ args }}
    
# Open preview for site
[group('run')]
preview:
    open http://127.0.0.1:8000
    just content --autoreload --listen

# Publish the site
[group('run')]
publish:
    just content --settings=publishconf.py

# Lint code
[group('qa')]
lint *args:
    uv run ruff check {{ args }}
    uv run ruff format {{ args }}
    uv run ty check --python .venv {{ args }}
