import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load Environment
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

if not all([SUPABASE_KEY, SUPABASE_URL, SUPABASE_JWT_SECRET]):
    raise EnvironmentError("One or more env variables are missing!")

# Initialize supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)