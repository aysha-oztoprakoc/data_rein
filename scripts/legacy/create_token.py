import os, sys
sys.path.insert(0, '/home/amdy/odysseus')
from core.database import SessionLocal, ApiToken
import secrets
import bcrypt
import uuid

db = SessionLocal()
raw_token = "ody_" + secrets.token_urlsafe(32)
prefix = raw_token[:8]
hashed = bcrypt.hashpw(raw_token.encode(), bcrypt.gensalt()).decode()

t = ApiToken(
    id=str(uuid.uuid4()),
    name="kad-bridge",
    token_prefix=prefix,
    token_hash=hashed,
    owner="admin",
    scopes="chat,documents:write,documents:read"
)
db.add(t)
db.commit()
print(raw_token)
