"""Entry point for running the coordinator."""

import uvicorn
from qianyuan_engine.coordinator import create_app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
