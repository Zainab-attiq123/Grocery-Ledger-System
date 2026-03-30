from fastapi import HTTPException
import crud

def login(db, username, password):
    user = crud.get_user(db, username)

    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}