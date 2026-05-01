from typing import Dict, List

# Subject-specific "Expert Tips" knowledge base
# These are retrieved based on the vision-classified subject.
SUBJECT_KNOWLEDGE = {
    "WILDLIFE": [
        "Focus on the eye: Use 'diffuse or sharpen' with a 'sharpen' preset on the eye region.",
        "Denoising: Prioritize 'denoise (profiled)' in 'wavelets' mode for fine feather/fur detail.",
        "Background: Use a slightly lower contrast in the background to make the subject pop.",
        "AgX Tip: Keep primary attenuation around 10% to preserve the saturation of natural plumage."
    ],
    "LANDSCAPE": [
        "Haze removal: Use 'diffuse or sharpen' with 'add local contrast' to cut through atmospheric haze.",
        "Dynamic Range: Balance exposure for the sky, then use 'color balance rgb' to recover shadows.",
        "Depth: A slight 'local contrast' boost in the foreground helps create a sense of scale.",
        "AgX Tip: Increase contrast to 1.6 for a punchier 'velvia' style landscape look."
    ],
    "MACRO": [
        "Stacking artifacts: Check for edge halos; use 'diffuse or sharpen' sparingly.",
        "Color: Use 'color calibration' to ensure the greens of foliage don't look artificial.",
        "AgX Tip: Use high 'skew' (0.2) to protect delicate highlight details in flowers."
    ]
}

def get_subject_tips(subject: str) -> List[str]:
    """Retrieves expert editing tips for a specific subject category."""
    return SUBJECT_KNOWLEDGE.get(subject.upper(), ["Focus on mid-gray balance and clean tonal transitions."])
