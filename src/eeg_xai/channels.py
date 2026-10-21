
"""Scalp EEG channel groups used in exploratory regional analyses."""

REGION_CHANNELS = {
    "frontal": ("FP1", "FP2", "F3", "F4", "F7", "F8", "FZ"),
    "central": ("C3", "C4", "CZ"),
    "parietal": ("P3", "P4", "PZ"),
    "temporal": ("T3", "T4", "T5", "T6"),
    "occipital": ("O1", "O2"),
}

SCALP_CHANNELS = tuple(
    channel
    for channels in REGION_CHANNELS.values()
    for channel in channels
)

AUXILIARY_CHANNELS = ("A1", "A2")
