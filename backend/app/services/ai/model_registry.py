import logging
from typing import Any, Dict, Optional

logger = logging.getLogger("terraverse")


class ModelRegistry:
    """Registry manager for tracking, loading, and managing AI/ML models

    for geospatial extraction, building segmentation, and change detection.
    """

    _registry: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def register_model(
        cls,
        model_id: str,
        name: str,
        version: str,
        description: str,
        model_instance: Optional[Any] = None,
    ) -> None:
        """Registers a new model or updates an existing entry in memory."""
        cls._registry[model_id] = {
            "name": name,
            "version": version,
            "description": description,
            "instance": model_instance,
            "status": "LOADED" if model_instance else "AVAILABLE",
        }
        logger.info(f"AI Model registered successfully: {model_id} (v{version})")

    @classmethod
    def get_model(cls, model_id: str) -> Optional[Any]:
        """Retrieves a registered model instance by ID."""
        model_entry = cls._registry.get(model_id)
        if model_entry:
            return model_entry.get("instance")
        return None

    @classmethod
    def list_models(cls) -> Dict[str, Dict[str, Any]]:
        """Returns metadata for all registered models."""
        return {
            model_id: {
                "name": data["name"],
                "version": data["version"],
                "description": data["description"],
                "status": data["status"],
            }
            for model_id, data in cls._registry.items()
        }


ModelRegistry.register_model(
    model_id="building_mask_rcnn_v1",
    name="Building Footprint Mask-RCNN",
    version="1.2.0",
    description="Extracts building footprints from high-res drone/satellite imagery.",
)

ModelRegistry.register_model(
    model_id="parcel_boundary_unet_v2",
    name="Parcel Boundary Segmenter U-Net",
    version="2.0.1",
    description="Detects cadastral boundary lines and fence divisions from aerial orthophotos.",
)
