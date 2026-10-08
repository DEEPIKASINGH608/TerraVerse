import uuid
import time
import random
import string


def generate_uuid() -> str:
    """Generates a standard UUID v4 string."""
    return str(uuid.uuid4())


def generate_parcel_id(prefix: str = "PCL") -> str:
    """Generates a unique canonical parcel identification key."""
    timestamp_part = int(time.time() * 1000) % 1000000
    random_str = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{prefix}-{timestamp_part}-{random_str}"


def generate_conflict_id(prefix: str = "CNF") -> str:
    """Generates a unique spatial/attribute conflict identifier."""
    random_str = "".join(random.choices(string.digits, k=6))
    return f"{prefix}-{random_str}"


def generate_dataset_id(prefix: str = "DS") -> str:
    """Generates a dataset tracking ID."""
    timestamp = time.strftime("%Y%m%d%H%M")
    random_str = "".join(random.choices(string.ascii_uppercase, k=3))
    return f"{prefix}-{timestamp}-{random_str}"