import pytest
from dt_ai.ai import synthesize_nudge

def test_synthesize_nudge_basic():
    ai_result = {"audit": "This is a sharp shot of a kingfisher."}
    neighbors = []
    state = {"history": []}
    
    nudge = synthesize_nudge(ai_result, neighbors, state)
    assert "kingfisher" in nudge
    # Check for mentor-like phrases
    assert "session" in nudge.lower() or "mentor" in nudge.lower() or "thoughts" in nudge.lower()

def test_synthesize_nudge_with_neighbors():
    ai_result = {"audit": "Great composition."}
    neighbors = ["IMG_001.ARW", "IMG_002.ARW"]
    state = {"history": []}
    
    nudge = synthesize_nudge(ai_result, neighbors, state)
    assert "adjacent" in nudge.lower() or "neighbors" in nudge.lower() or "peeked" in nudge.lower()

def test_synthesize_nudge_continuation():
    ai_result = {"audit": "Nice highlights."}
    neighbors = []
    state = {"history": [{"image": "prev.ARW"}]}
    
    nudge = synthesize_nudge(ai_result, neighbors, state)
    assert "next" in nudge.lower() or "previous" in nudge.lower() or "continuing" in nudge.lower()
