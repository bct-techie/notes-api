from fastapi import FastAPI

from delete import router as delete_router
from get import router as get_router
from patch import router as patch_router
from post import router as post_router
from put import router as put_router

app = FastAPI()
app.include_router(post_router)
app.include_router(get_router)
app.include_router(put_router)
app.include_router(patch_router)
app.include_router(delete_router)


@app.get("/health")
def health():
    return {"status": "ok"}
