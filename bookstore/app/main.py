from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import books

app = FastAPI()

# ✅ Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(books.router, prefix="/books", tags=["Books"])

@app.get("/")
def root():
    return {"message": "Bookstore API is live"}
