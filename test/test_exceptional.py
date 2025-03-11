import pytest
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_invalid_input_validation(test_obj):
    """Consolidated test for invalid input validation"""
    try:
        import digital_music_mixer as app
        test_list = [1, 2, 3, 4, 5]
        
        # Test invalid pattern types
        with pytest.raises(ValueError):
            app.reverse_list(None)
            
        with pytest.raises(ValueError):
            app.visualize_list("not a list")
            
        # Test invalid length values
        with pytest.raises(ValueError):
            app.create_bass_pattern(0)  # Zero length
            
        with pytest.raises(ValueError):
            app.create_melody_pattern(-10)  # Negative length
            
        with pytest.raises(ValueError):
            app.create_percussion_pattern("not an integer")  # Non-integer length
            
        # Test invalid slice parameters
        with pytest.raises(ValueError):
            app.slice_list(test_list, "not an integer")  # Non-integer start
            
        with pytest.raises(ValueError):
            app.slice_list(test_list, 0, 5, 0)  # Zero step
            
        # Test invalid extend parameters
        with pytest.raises(ValueError):
            app.extend_list(test_list, -2)  # Negative repeats
            
        # Test invalid shuffle parameters
        with pytest.raises(ValueError):
            app.shuffle_segments(test_list, 0)  # Zero segment size
            
        test_obj.yakshaAssert("TestInvalidInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInvalidInputValidation", False, "exception")
        pytest.fail(f"Invalid input validation test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])