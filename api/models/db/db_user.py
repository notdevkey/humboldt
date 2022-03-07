from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class DbUser:
    user_id: int = 0
    username: str = ""
    email: Optional[str] = None
    password_hash: str = ""
    profile_picture_url: str = ""
    disabled: Optional[bool] = None
