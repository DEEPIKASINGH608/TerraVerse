from pathlib import Path
from typing import Any, Dict, Union
import json


class HarmonizationReportGenerator:
    """Generates structured summary reports for land harmonization runs."""

    @staticmethod
    def generate_json_report(metrics: Dict[str, Any], output_path: Union[str, Path]) -> Path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=4)
        return output_path
