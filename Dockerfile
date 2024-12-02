FROM ghcr.io/astral-sh/uv:0.4.27-python3.10-bookworm

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Copy the project into the image
ADD . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Run the server
EXPOSE 8000
CMD [ "uv", "run", "gunicorn", "-b", "0.0.0.0:8000", "main:app" ]
