#################
#    Imports    #
#################
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse
from sqlmodel import Session, SQLModel, select
from models import Category
from database import engine

# Initialize FastAPI app
app = FastAPI()
session = Session(bind=engine)

#################
#    Routes     #
#################
# Root folder (home page)
@app.get("/",response_class=HTMLResponse) # HTMLResponse can be used to return HTML content
async def home():
    #return {"message": "Welcome to the Category API home"}
    return '''<h1>Welcome to the Category API home</h1>
    <a href='http://127.0.0.1:8000/docs'>Use the docs to manage categories.</a>'''


# Get all categories
@app.get("/categories", response_model=list[Category])
async def get_categories():
    with Session(bind=engine) as session:
        categories = session.exec(select(Category)).all()
        return categories


# POst a new category
@app.post("/categories", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(category: Category):
    with Session(bind=engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category
    

# Get a category by ID
@app.get("/categories/{category_id}", response_model=Category)
async def get_category(category_id: int):
    with Session(bind=engine) as session:
        category = session.get(Category, category_id)
        if not category:
            return {"error": "Category not found"}
        return category


# Delete a category by ID
@app.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    with Session(bind=engine) as session:
        category = session.get(Category, category_id)
        if not category:
            return {"error": "Category not found"}
        session.delete(category)
        session.commit()
        return {"message": "Category deleted successfully"}
    
    
# Update a category by ID
@app.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, category: Category):
    with Session(bind=engine) as session:
        existing_category = session.get(Category, category_id)
        if not existing_category:
            return {"error": "Category not found"}
        
        existing_category.name = category.name
        existing_category.description = category.description
        session.add(existing_category)
        session.commit()
        session.refresh(existing_category)
        return existing_category