import pytest

from yasbd import BoundaryDetector
from tests.test_data import catalan

@pytest.mark.parametrize("text", catalan.TEST_DATA)
def test_segmentation(text):
    detector = BoundaryDetector(lang="ca", external_lang_packs=["yasbd_ca"])
    assert list(detector.segment(text.replace("|", ""))) == [
        part.strip() for part in text.split("|")
    ]
