import uvicorn
from fastapi import FastAPI
from app.controllers.user_controller import user_router
from app.controllers.expense_controller import expense_router
from app.controllers.revenue_controller import revenue_router
from app.controllers.vizualization_controller import visualization_router

# Create an instance of the FastAPI application
app = FastAPI()

# Include the routers with the appropriate prefixes
app.include_router(user_router, prefix='/user')
app.include_router(expense_router, prefix='/expense')
app.include_router(revenue_router, prefix='/revenue')
app.include_router(visualization_router, prefix='/vis')

# Run the application using uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
