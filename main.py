from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_signup, dashboard, user_login, notifications

# Initialize FastAPI Instance
app = FastAPI()

# User authorizaton route
app.include_router(dashboard.router)
app.include_router(user_signup.router)
app.include_router(user_login.router)
app.include_router(notifications.router)

# Setting up the origins
origins = [
    "http://localhost:3000"
]

# Configure Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)