from fastapi import APIRouter, HTTPException
from app.schemas.book import Book
from app.database import book_collection
from fastapi.encoders import jsonable_encoder
from bson import ObjectId, errors as bson_errors
from fastapi import Path
from app.schemas.book import UpdateBook
from app.utils.bson_utils import serialize_doc

router = APIRouter()

@router.post("/", response_model=Book, status_code=201)
async def create_book(book: Book):
    book_data = jsonable_encoder(book)  # ensures JSON safe format
    result = await book_collection.insert_one(book_data)
    if result.inserted_id:
        return book
    raise HTTPException(status_code=500, detail="Book could not be added")


@router.get("/", response_model=list[Book])
async def get_books():
    books = []
    cursor = book_collection.find()
    async for doc in cursor:
        books.append(Book(**serialize_doc(doc)))
    return books



@router.get("/{book_id}", response_model=Book)
async def get_book_by_id(book_id: str = Path(..., description="The ID of the book")):
    try:
        book = await book_collection.find_one({"_id": book_id})
        if book:
            book["_id"] = str(book["_id"])
            return Book(**serialize_doc(book))
        raise HTTPException(status_code=404, detail="Book not found")
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Invalid book ID format")





@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: str, book_update: UpdateBook):
    update_data = {k: v for k, v in book_update.dict().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = await book_collection.update_one({"_id": book_id}, {"$set": update_data})

    if result.modified_count == 0:
        existing = await book_collection.find_one({"_id": book_id})
        if not existing:
            raise HTTPException(status_code=404, detail="Book not found")
        return Book(**existing)  # Nothing changed, but book exists

    updated_book = await book_collection.find_one({"_id": book_id})
    updated_book["_id"] = str(updated_book["_id"])
    return Book(**updated_book)



@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str):
    result = await book_collection.delete_one({"_id": book_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")

    return None  # 204 No Content requires an empty response


