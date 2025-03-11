import pytest
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_scenarios(test_obj):
    """Consolidated test for boundary scenarios"""
    try:
        import digital_music_mixer as app
        
        # Test with empty list
        empty_list = []
        assert "Empty list" in app.visualize_list(empty_list), "Should handle empty list visualization"
        assert app.reverse_list(empty_list) == [], "Should handle empty list reversal"
        assert app.extend_list(empty_list, 5) == [], "Should handle empty list extension"
        
        # Test with minimum and maximum allowed values
        min_length = 8
        pattern = app.create_bass_pattern(min_length)
        assert len(pattern) == min_length, "Should create pattern with minimum length"
        
        # Test pattern value ranges
        bass = app.create_bass_pattern(12)
        melody = app.create_melody_pattern(12)
        percussion = app.create_percussion_pattern(12)
        ambient = app.create_ambient_pattern(12)
        
        assert all(0 <= val <= 100 for val in bass), "Bass pattern values should be between 0-100"
        assert all(0 <= val <= 100 for val in melody), "Melody pattern values should be between 0-100"
        assert all(0 <= val <= 100 for val in percussion), "Percussion pattern values should be between 0-100"
        assert all(10 <= val <= 90 for val in ambient), "Ambient pattern values should be between 10-90"
        
        # Test visualization limits (should limit to 50 elements)
        large_list = list(range(100))
        visualization = app.visualize_list(large_list)
        digit_count = sum(1 for c in visualization.split('\n')[0].strip() if c.isdigit())
        assert digit_count <= 50, "Visualization should limit display to 50 elements"
        
        # Test segment shuffling edge cases
        test_list = list(range(10))
        shuffled1 = app.shuffle_segments(test_list, 1)
        shuffled_full = app.shuffle_segments(test_list, 10)
        assert sorted(shuffled1) == sorted(test_list), "Should preserve all elements with segment size 1"
        assert sorted(shuffled_full) == sorted(test_list), "Should preserve all elements with full segment size"
        
        test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])