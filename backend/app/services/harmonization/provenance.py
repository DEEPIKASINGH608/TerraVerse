from datetime import datetime
from typing import Any, Dict


class ProvenanceTracker:
    """Tracks historical lineage of spatial parcel transformations."""

    @staticmethod
    def create_lineage_entry(source_department: str, action: str, details: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "source_department": source_department,
            "action": action,
            "details": details,
        }