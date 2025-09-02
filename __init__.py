# __init__.py – package entry for LoRAWeightAxisXY
try:
    from .lora_weight_axis_xy import (
        NODE_CLASS_MAPPINGS as _NCM,
        NODE_DISPLAY_NAME_MAPPINGS as _NDM,
    )
    NODE_CLASS_MAPPINGS = dict(_NCM)
    NODE_DISPLAY_NAME_MAPPINGS = dict(_NDM)
    print("[LoRAWeightAxisXY] Nodes registered:", ", ".join(NODE_DISPLAY_NAME_MAPPINGS.values()))
except Exception as e:
    print("[LoRAWeightAxisXY] Failed to import node:", e)
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
