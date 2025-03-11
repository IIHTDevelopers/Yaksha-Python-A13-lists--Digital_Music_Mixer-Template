import pytest
import re
import random
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

@pytest.fixture
def sample_list():
    """Create a sample list for testing"""
    return [i for i in range(1, 21)]  # List from 1 to 20

def test_pattern_creation(test_obj):
    """Test all pattern creation functions"""
    try:
        from digital_music_mixer import (
            create_bass_pattern,
            create_melody_pattern,
            create_percussion_pattern,
            create_ambient_pattern
        )
        
        # Test with different lengths
        lengths = [8, 16, 32]
        
        for length in lengths:
            # Test bass pattern
            bass = create_bass_pattern(length)
            assert len(bass) == length, f"Bass pattern should have length {length}"
            assert all(0 <= val <= 100 for val in bass), "All values should be in range 0-100"
            
            # Test melody pattern
            melody = create_melody_pattern(length)
            assert len(melody) == length, f"Melody pattern should have length {length}"
            assert all(0 <= val <= 100 for val in melody), "All values should be in range 0-100"
            
            # Test percussion pattern
            percussion = create_percussion_pattern(length)
            assert len(percussion) == length, f"Percussion pattern should have length {length}"
            assert all(0 <= val <= 100 for val in percussion), "All values should be in range 0-100"
            
            # Test ambient pattern
            ambient = create_ambient_pattern(length)
            assert len(ambient) == length, f"Ambient pattern should have length {length}"
            assert all(10 <= val <= 90 for val in ambient), "All values should be in range 10-90"
        
        # Test pattern characteristics (simplified)
        bass = create_bass_pattern(20)
        percussion = create_percussion_pattern(20)
        
        # At least some bass values at position 0, 4, 8, etc. should be higher
        assert any(bass[i] >= 60 for i in range(0, 20, 4)), "Bass pattern should have higher values at regular intervals"
        
        # Percussion should have alternating high and low values
        highs = [percussion[i] for i in range(0, 20, 2)]
        lows = [percussion[i] for i in range(1, 20, 2)]
        assert any(val >= 80 for val in highs), "Percussion should have high values at even positions"
        assert any(val <= 10 for val in lows), "Percussion should have low values at odd positions"
        
        test_obj.yakshaAssert("TestPatternCreation", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestPatternCreation", False, "functional")
        pytest.fail(f"Pattern creation test failed: {str(e)}")

def test_list_operations(test_obj, sample_list):
    """Test all list operations functions"""
    try:
        from digital_music_mixer import (
            slice_list,
            reverse_list,
            extend_list,
            combine_lists,
            shuffle_segments
        )
        
        # Test slice_list
        original = sample_list.copy()
        
        # Slice with default parameters
        assert slice_list(original, 5) == original[5:], "slice_list with start only should match list[start:]"
        
        # Slice with end
        assert slice_list(original, 5, 10) == original[5:10], "slice_list with start,end should match list[start:end]"
        
        # Slice with step
        assert slice_list(original, 0, 20, 2) == original[0:20:2], "slice_list with start,end,step should match list[start:end:step]"
        
        # Slice with None for end
        assert slice_list(original, 5, None) == original[5:], "slice_list with None end should match list[start:]"
        
        # Test reverse_list
        assert reverse_list(original) == original[::-1], "reverse_list should match list[::-1]"
        
        # Test extend_list
        assert extend_list(original, 2) == original * 2, "extend_list should match list * repeats"
        
        # Test combine_lists
        other_list = [100, 200, 300]
        assert combine_lists(original, other_list) == original + other_list, "combine_lists should match list1 + list2"
        
        # Test shuffle_segments (can only test that length and elements are preserved)
        segment_size = 5
        shuffled = shuffle_segments(original, segment_size)
        assert len(shuffled) == len(original), "shuffle_segments should preserve list length"
        assert sorted(shuffled) == sorted(original), "shuffle_segments should preserve all list elements"
        
        # Verify some segment integrity
        # This is a bit tricky without controlling the random shuffle, so we'll just check a few properties
        found_intact_segment = False
        for i in range(0, len(original) - segment_size + 1, segment_size):
            segment = original[i:i+segment_size]
            # Check if this segment appears intact anywhere in the shuffled list
            for j in range(0, len(shuffled) - segment_size + 1):
                if shuffled[j:j+segment_size] == segment:
                    found_intact_segment = True
                    break
        
        # If shuffling doesn't occur (when only one segment), we should still find the segment intact
        if len(original) <= segment_size:
            assert found_intact_segment, "With only one segment, it should remain intact"
        
        test_obj.yakshaAssert("TestListOperations", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestListOperations", False, "functional")
        pytest.fail(f"List operations test failed: {str(e)}")

def test_visualize_list(test_obj):
    """Test visualization function output format"""
    try:
        from digital_music_mixer import visualize_list
        
        # Test with empty list
        empty_result = visualize_list([])
        assert "Empty list" in empty_result, "Empty list visualization should contain 'Empty list'"
        
        # Test with a sample list
        sample = [50, 25, 75, 100, 0]
        result = visualize_list(sample)
        
        # Check basic structure
        assert "Values (0-100)" in result, "Visualization should include scale information"
        lines = result.split('\n')
        assert len(lines) > 5, "Visualization should have multiple lines"
        
        # Check that all values are represented
        for val in sample:
            # Higher values should produce more filled rows
            filled_rows = len([line for line in lines if "█" in line])
            assert filled_rows > 0, "Visualization should have filled rows for values"
        
        # Test with large list (should limit to 50 elements)
        large_list = list(range(100))
        large_result = visualize_list(large_list)
        max_width = max(len(line) for line in large_result.split('\n'))
        assert max_width <= 60, "Visualization width should be limited for large lists"
        
        test_obj.yakshaAssert("TestVisualizeList", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestVisualizeList", False, "functional")
        pytest.fail(f"Visualization test failed: {str(e)}")

def test_display_functions(test_obj):
    """Test display menu functions output"""
    try:
        import io
        import sys
        from digital_music_mixer import display_menu, display_transformation_menu
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call menu functions
        display_menu()
        menu_output = captured_output.getvalue()
        
        # Reset capture
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call transformation menu
        display_transformation_menu()
        transform_output = captured_output.getvalue()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check main menu content
        assert "List Operations Lab" in menu_output, "Main menu should include 'List Operations Lab'"
        assert "Create Bass Pattern" in menu_output, "Main menu should include bass pattern option"
        assert "Create Melody Pattern" in menu_output, "Main menu should include melody pattern option"
        assert "Create Percussion Pattern" in menu_output, "Main menu should include percussion pattern option"
        assert "Create Ambient Pattern" in menu_output, "Main menu should include ambient pattern option"
        assert "Transform Current Pattern" in menu_output, "Main menu should include transform option"
        assert "Exit" in menu_output, "Main menu should include exit option"
        
        # Check transformation menu content
        assert "List Transformation Options" in transform_output, "Transform menu should include 'List Transformation Options'"
        assert "Reverse List" in transform_output, "Transform menu should include reverse option"
        assert "Slice List" in transform_output, "Transform menu should include slice option"
        assert "Extend List" in transform_output, "Transform menu should include extend option"
        assert "Combine with New List" in transform_output, "Transform menu should include combine option"
        assert "Shuffle Segments" in transform_output, "Transform menu should include shuffle option"
        
        test_obj.yakshaAssert("TestDisplayFunctions", True, "functional")
    except Exception as e:
        sys.stdout = sys.__stdout__  # Reset stdout in case of exception
        test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
        pytest.fail(f"Display functions test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])