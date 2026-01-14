from fastapi import FastAPI

app = FastAPI()

@app.get("/tags/{tag_id}")
def get_tag(tag_id: str):
    return {
        "tag_id": tag_id
    }

