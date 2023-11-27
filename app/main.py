import uvicorn
from analyzer import dash_app
from core.settings import settings
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()


@app.get("/")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": settings.DASH_PREFIX, "summary": "Analyzer"},
        ]
    }


app.mount(settings.DASH_PREFIX, WSGIMiddleware(dash_app.server))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, reload=settings.DEBUG_MODE)
