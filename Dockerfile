# Step 1: Install Poetry and Other Depencies
FROM python:3.11-slim-bookworm
WORKDIR /app
COPY pyproject.toml /app/
RUN poetry install

# Step 2: Environment Variables
ENV PORT=8000
ENV WORKERS=2
EXPOSE ${PORT}

# Step 3: Copy Source Code
COPY . .

# Step 4: Run the server
CMD ["poetry", "run", "python", "main.py"]