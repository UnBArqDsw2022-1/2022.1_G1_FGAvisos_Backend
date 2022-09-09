from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.routers import api_router


app = FastAPI(title="FGAvisos API")
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)
