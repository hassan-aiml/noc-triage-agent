from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

sb = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_KEY"])

result = sb.table("noc_kb_chunks").select("*").limit(5).execute()

print(f"Rows returned: {len(result.data)}")
print("First row alarm_id:", result.data[0]["alarm_id"] if result.data else "empty")