"""
AluSense AI - Dataset and Standards Module
"""

from .standards import (
    ALLOY_STANDARDS,
    MANUFACTURING_PROCESSES,
    PROCESS_LIMITS,
    PRESET_SCENARIOS,
    get_alloy_details,
    get_process_limits,
    get_presets
)

__all__ = [
    "ALLOY_STANDARDS",
    "MANUFACTURING_PROCESSES",
    "PROCESS_LIMITS",
    "PRESET_SCENARIOS",
    "get_alloy_details",
    "get_process_limits",
    "get_presets",
]
