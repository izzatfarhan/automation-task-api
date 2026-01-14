from fastapi import FastAPI

app = FastAPI(title="Automation Task API")

@app.get("/health")
def health_check():
    return {"status" : "ok"}