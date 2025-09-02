try:
    from nodes import folder_paths
except Exception:
    import folder_paths

def _linspace(a: float, b: float, n: int):
    if n <= 1:
        return [float(b)]
    step = (b - a) / float(n - 1)
    return [a + i * step for i in range(n)]

class XYInput_LoRA_Weight_Simple:
    @classmethod
    def INPUT_TYPES(cls):
        loras = ["None"] + folder_paths.get_filename_list("loras")
        return {
            "required": {
                "lora_name": (loras,),
                "min_value": ("FLOAT", {"default": 0.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                "max_value": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                "steps":     ("INT",   {"default": 3,   "min": 1,    "max": 200, "step": 1}),
            }
        }

    RETURN_TYPES = ("XY",)
    RETURN_NAMES = ("X or Y",)
    FUNCTION = "build_xy"
    CATEGORY = "Efficiency Nodes/XY Inputs"

    def build_xy(self, lora_name, min_value, max_value, steps):
        if lora_name == "None":
            return (None,)

        vals = _linspace(float(min_value), float(max_value), int(steps))
        vals = [float(f"{v:.2f}") for v in vals]

        xy_type = "LoRA"
        xy_value = [[(lora_name, v, v)] for v in vals]
        return ((xy_type, xy_value),)

NODE_CLASS_MAPPINGS = {
    "XY Input: LoRA Weight (simple)": XYInput_LoRA_Weight_Simple,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "XY Input: LoRA Weight (simple)": "XY Input: LoRA Weight (simple)",
}