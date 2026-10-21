from narcotics_platform.screening import ScreeningPipeline

def test_empty_is_unknown():
    r = ScreeningPipeline().screen([])
    assert r.state == 'UNKNOWN'
    assert r.requires_human_review
    assert r.abstained
    assert r.uncertainty == 1.0
    assert r.candidates == []

def test_invalid_only_detections_are_unknown():
    r = ScreeningPipeline().screen([{'label': 'amphetamine', 'confidence': 1.5}])
    assert r.state == 'UNKNOWN'
    assert r.requires_human_review
    assert r.abstained
    assert r.candidates == []

def test_unknown_label_stays_unknown():
    r = ScreeningPipeline().screen([{'label': 'unseen_substance', 'confidence': 0.95}])
    assert r.state == 'HUMAN_REVIEW'
    assert r.candidates[0].label == 'unknown_substance'

def test_candidate_requires_review():
    r = ScreeningPipeline().screen([{'label': 'methamphetamine_crystal', 'confidence': 0.91}])
    assert r.state == 'HUMAN_REVIEW'
