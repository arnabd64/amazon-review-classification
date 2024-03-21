import uvicorn
import os


if __name__ == "__main__":
    uvicorn.run("src.server:app",
                host = "0.0.0.0",
                port = int(os.getenv("PORT")),
                workers = int(os.getenv("WORKERS")),
                loop = 'uvloop',
                http = 'httptools')