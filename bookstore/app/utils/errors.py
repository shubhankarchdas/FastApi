from fastapi import HTTPException

def not_found(detail="Item not found"):
    raise HTTPException(status_code=404, detail=detail)

def bad_request(detail="Bad request"):
    raise HTTPException(status_code=400, detail=detail)

def unauthorized(detail="Unauthorized"):
    raise HTTPException(status_code=401, detail=detail)

def forbidden(detail="Forbidden"):
    raise HTTPException(status_code=403, detail=detail)
