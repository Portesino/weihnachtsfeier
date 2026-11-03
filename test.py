from supabase import create_client

url = "https://cufdtaezyhpgrbxkpepr.supabase.co"
key = "sb_publishable_8oxbymKbZf5sTtaJ39zXZA_xDtP5hZU"

supabase = create_client(url, key)

result = supabase.table("anmeldungen").select("*").execute()

print(result.data)