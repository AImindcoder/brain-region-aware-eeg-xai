
"""Basic consistency tests for the EEG channel configuration."""

import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from eeg_xai.channels import (
    AUXILIARY_CHANNELS,
    REGION_CHANNELS,
    SCALP_CHANNELS,
)


class TestEEGChannels(unittest.TestCase):
    def test_expected_region_sizes(self):
        expected = {
            "frontal": 7,
            "central": 3,
            "parietal": 3,
            "temporal": 4,
            "occipital": 2,
        }
        self.assertEqual(
            {name: len(channels) for name, channels in REGION_CHANNELS.items()},
            expected,
        )

    def test_scalp_channels_are_unique(self):
        self.assertEqual(len(SCALP_CHANNELS), 19)
        self.assertEqual(len(set(SCALP_CHANNELS)), 19)

    def test_auxiliary_channels_are_not_scalp_channels(self):
        self.assertTrue(set(AUXILIARY_CHANNELS).isdisjoint(SCALP_CHANNELS))


if __name__ == "__main__":
    unittest.main()
