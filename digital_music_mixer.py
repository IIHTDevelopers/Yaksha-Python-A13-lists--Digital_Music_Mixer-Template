"""
List Operations Lab - Sound Pattern Generator
A console application for demonstrating list operations in Python.
"""
import random

def create_bass_pattern(length: int) -> list:
    """
    Creates a bass pattern with strong beats and lower values.
    
    Parameters:
    length (int): Length of the pattern to generate
    
    Returns:
    list: A list of integers representing amplitude values (0-100)
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Create a bass pattern with strong beats and lower values
    pattern = [random.randint(60, 100) if i % 4 == 0 else random.randint(20, 50) for i in range(length)]
    
    return pattern

def create_melody_pattern(length: int) -> list:
    """
    Creates a melody pattern with varied amplitudes.
    
    Parameters:
    length (int): Length of the pattern to generate
    
    Returns:
    list: A list of integers representing amplitude values (0-100)
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Create a melody pattern with varied amplitudes
    base = random.randint(40, 70)
    pattern = [max(0, min(100, base + random.randint(-20, 20))) for _ in range(length)]
    
    return pattern

def create_percussion_pattern(length: int) -> list:
    """
    Creates a percussion pattern with sharp peaks.
    
    Parameters:
    length (int): Length of the pattern to generate
    
    Returns:
    list: A list of integers representing amplitude values (0-100)
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Create a percussion pattern with sharp peaks
    pattern = [random.randint(80, 100) if i % 2 == 0 else random.randint(0, 10) for i in range(length)]
    
    return pattern

def create_ambient_pattern(length: int) -> list:
    """
    Creates a smooth ambient pattern.
    
    Parameters:
    length (int): Length of the pattern to generate
    
    Returns:
    list: A list of integers representing amplitude values (0-100)
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Create a smooth ambient pattern
    pattern = []
    value = random.randint(30, 70)
    for _ in range(length):
        value += random.randint(-5, 5)
        value = max(10, min(90, value))  # Keep within bounds
        pattern.append(value)
    
    return pattern

def slice_list(pattern: list, start: int = 0, end: int = None, step: int = 1) -> list:
    """
    Extracts a segment of a list using slice notation.
    
    Parameters:
    pattern (list): The list to slice
    start (int): Starting index
    end (int): Ending index (exclusive)
    step (int): Step size
    
    Returns:
    list: Sliced list
    """
    if not isinstance(pattern, list):
        raise ValueError("Pattern must be a list.")
    if not isinstance(start, int):
        raise ValueError("Start must be an integer.")
    if end is not None and not isinstance(end, int):
        raise ValueError("End must be an integer.")
    if not isinstance(step, int) or step == 0:
        raise ValueError("Step must be a non-zero integer.")
    
    # Handle None for end parameter
    if end is None:
        end = len(pattern)
    
    # Use exact pattern[start:end:step] notation to match regex
    return pattern[start:end:step]

def reverse_list(pattern: list) -> list:
    """
    Reverses a list.
    
    Parameters:
    pattern (list): The list to reverse
    
    Returns:
    list: Reversed list
    """
    if not isinstance(pattern, list):
        raise ValueError("Pattern must be a list.")
    
    # Use exact pattern[::-1] notation to match regex
    return pattern[::-1]

def extend_list(pattern: list, repeats: int) -> list:
    """
    Extends a list by repeating it multiple times.
    
    Parameters:
    pattern (list): The list to extend
    repeats (int): Number of times to repeat the list
    
    Returns:
    list: Extended list
    """
    if not isinstance(pattern, list):
        raise ValueError("Pattern must be a list.")
    if not isinstance(repeats, int) or repeats <= 0:
        raise ValueError("Repeats must be a positive integer.")
    
    # Create a new list with the pattern repeated
    return pattern * repeats

def combine_lists(pattern1: list, pattern2: list) -> list:
    """
    Combines two lists using concatenation.
    
    Parameters:
    pattern1 (list): The first list
    pattern2 (list): The second list
    
    Returns:
    list: Combined list
    """
    if not isinstance(pattern1, list):
        raise ValueError("Pattern1 must be a list.")
    if not isinstance(pattern2, list):
        raise ValueError("Pattern2 must be a list.")
    
    # Combine the lists
    return pattern1 + pattern2

def shuffle_segments(pattern: list, segment_size: int) -> list:
    """
    Shuffles segments of a list while maintaining segment integrity.
    
    Parameters:
    pattern (list): The list to shuffle
    segment_size (int): Size of each segment
    
    Returns:
    list: List with shuffled segments
    """
    if not isinstance(pattern, list):
        raise ValueError("Pattern must be a list.")
    if not isinstance(segment_size, int) or segment_size <= 0:
        raise ValueError("Segment size must be a positive integer.")
    
    # Divide pattern into segments
    segments = []
    for i in range(0, len(pattern), segment_size):
        segments.append(pattern[i:min(i + segment_size, len(pattern))])
    
    # Shuffle segments
    random.shuffle(segments)
    
    # Reconstruct pattern
    result = []
    for segment in segments:
        result.extend(segment)
    
    return result

def visualize_list(pattern: list) -> str:
    """
    Creates an ASCII visualization of a list.
    
    Parameters:
    pattern (list): The list to visualize
    
    Returns:
    str: ASCII visualization
    """
    if not isinstance(pattern, list):
        raise ValueError("Pattern must be a list.")
    
    if not pattern:
        return "Empty list"
    
    height = 10  # Height of the visualization
    result = []
    
    # Create a header with indices
    header = "    " + "".join(f"{i % 10}" for i in range(min(len(pattern), 50)))
    result.append(header)
    
    # Create visualization rows
    for row in range(height, 0, -1):
        threshold = row * (100 / height)
        line = f"{row:2d} |"
        
        for value in pattern[:50]:  # Limit to first 50 values for display
            try:
                value_num = int(value)
                if value_num >= threshold:
                    line += "█"
                else:
                    line += " "
            except (ValueError, TypeError):
                line += "?"
        
        result.append(line)
    
    # Add a footer
    result.append("   " + "-" * (min(len(pattern), 50) + 1))
    result.append("    Values (0-100)")
    
    return "\n".join(result)

def display_menu() -> None:
    """Displays the main menu of the List Operations Lab."""
    print("\nList Operations Lab")
    print("==================")
    print("1. Create Bass Pattern")
    print("2. Create Melody Pattern")
    print("3. Create Percussion Pattern")
    print("4. Create Ambient Pattern")
    print("5. Transform Current Pattern")
    print("6. View Current Pattern")
    print("0. Exit")
    print("==================")

def display_transformation_menu() -> None:
    """Displays the transformation menu."""
    print("\nList Transformation Options")
    print("==========================")
    print("1. Reverse List (list[::-1])")
    print("2. Slice List (list[start:end:step])")
    print("3. Extend List (list * n)")
    print("4. Combine with New List (list1 + list2)")
    print("5. Shuffle Segments")
    print("0. Return to Main Menu")
    print("==========================")

def main():
    """Main function to run the List Operations Lab."""
    try:
        print("\nWelcome to List Operations Lab!")
        print("This application demonstrates fundamental list operations in Python.")
        
        # Initialize variables
        patterns = []  # Store created patterns
        active_pattern = None  # Currently selected pattern
        
        continue_running = True
        while continue_running:
            display_menu()
            
            try:
                choice = input("Enter your choice: ").strip()
                if not choice.isdigit():
                    print("Please enter a number.")
                    continue
                
                choice = int(choice)
                
                if choice == 0:
                    # Exit
                    continue_running = False
                
                elif choice in [1, 2, 3, 4]:
                    # Create a new pattern
                    length_input = input("Enter pattern length (8-64): ").strip()
                    if not length_input.isdigit():
                        print("Please enter a valid number.")
                        continue
                    
                    length = int(length_input)
                    if not 8 <= length <= 64:
                        print("Length must be between 8 and 64.")
                        continue
                    
                    if choice == 1:
                        # Bass pattern
                        active_pattern = create_bass_pattern(length)
                        pattern_type = "Bass"
                    elif choice == 2:
                        # Melody pattern
                        active_pattern = create_melody_pattern(length)
                        pattern_type = "Melody"
                    elif choice == 3:
                        # Percussion pattern
                        active_pattern = create_percussion_pattern(length)
                        pattern_type = "Percussion"
                    elif choice == 4:
                        # Ambient pattern
                        active_pattern = create_ambient_pattern(length)
                        pattern_type = "Ambient"
                    
                    # Add to list of patterns
                    patterns.append(active_pattern)
                    
                    print(f"\nCreated {pattern_type} Pattern (Length: {len(active_pattern)})")
                    print(visualize_list(active_pattern))
                
                elif choice == 5:
                    # Transform current pattern
                    if active_pattern is None:
                        print("No active pattern. Please create a pattern first.")
                        continue
                    
                    display_transformation_menu()
                    transform_choice = input("Select transformation: ").strip()
                    if not transform_choice.isdigit():
                        print("Please enter a number.")
                        continue
                    
                    transform_choice = int(transform_choice)
                    
                    if transform_choice == 0:
                        # Return to main menu
                        continue
                    
                    elif transform_choice == 1:
                        # Reverse list
                        active_pattern = reverse_list(active_pattern)
                        print("\nList Reversed using list[::-1]")
                        print(visualize_list(active_pattern))
                    
                    elif transform_choice == 2:
                        # Slice list
                        start_input = input("Start index: ").strip()
                        if not start_input.isdigit():
                            print("Please enter a valid number.")
                            continue
                        start = int(start_input)
                        
                        end_input = input("End index (or leave blank for end): ").strip()
                        end = None
                        if end_input:
                            if not end_input.isdigit():
                                print("Please enter a valid number or leave blank.")
                                continue
                            end = int(end_input)
                        
                        step_input = input("Step size (default 1): ").strip() or "1"
                        if not step_input.isdigit() or int(step_input) == 0:
                            print("Please enter a non-zero number.")
                            continue
                        step = int(step_input)
                        
                        active_pattern = slice_list(active_pattern, start, end, step)
                        print(f"\nList Sliced using list[{start}:{end if end is not None else ''}:{step}]")
                        print(visualize_list(active_pattern))
                    
                    elif transform_choice == 3:
                        # Extend list
                        repeats_input = input("Number of repetitions: ").strip()
                        if not repeats_input.isdigit() or int(repeats_input) <= 0:
                            print("Please enter a positive number.")
                            continue
                        repeats = int(repeats_input)
                        
                        active_pattern = extend_list(active_pattern, repeats)
                        print(f"\nList Extended using list * {repeats}")
                        print(visualize_list(active_pattern))
                    
                    elif transform_choice == 4:
                        # Combine with new list
                        print("\nCreate a new list to combine with:")
                        
                        pattern_type_input = input("Select pattern type (1-Bass, 2-Melody, 3-Percussion, 4-Ambient): ").strip()
                        if not pattern_type_input.isdigit() or not 1 <= int(pattern_type_input) <= 4:
                            print("Please enter a number between 1 and 4.")
                            continue
                        pattern_type_choice = int(pattern_type_input)
                        
                        length_input = input("Enter pattern length (8-64): ").strip()
                        if not length_input.isdigit() or not 8 <= int(length_input) <= 64:
                            print("Please enter a valid length between 8 and 64.")
                            continue
                        length = int(length_input)
                        
                        if pattern_type_choice == 1:
                            new_pattern = create_bass_pattern(length)
                        elif pattern_type_choice == 2:
                            new_pattern = create_melody_pattern(length)
                        elif pattern_type_choice == 3:
                            new_pattern = create_percussion_pattern(length)
                        else:
                            new_pattern = create_ambient_pattern(length)
                        
                        print("\nNew pattern created:")
                        print(visualize_list(new_pattern))
                        
                        active_pattern = combine_lists(active_pattern, new_pattern)
                        print("\nLists Combined using list1 + list2")
                        print(visualize_list(active_pattern))
                    
                    elif transform_choice == 5:
                        # Shuffle segments
                        segment_input = input("Segment size: ").strip()
                        if not segment_input.isdigit() or int(segment_input) <= 0:
                            print("Please enter a positive number.")
                            continue
                        segment_size = int(segment_input)
                        
                        if segment_size > len(active_pattern):
                            print(f"Segment size cannot be larger than list length ({len(active_pattern)}).")
                            continue
                        
                        active_pattern = shuffle_segments(active_pattern, segment_size)
                        print("\nList Segments Shuffled")
                        print(visualize_list(active_pattern))
                    
                    else:
                        print("Invalid choice.")
                
                elif choice == 6:
                    # View current pattern
                    if active_pattern is None:
                        print("No active pattern. Please create a pattern first.")
                    else:
                        print(f"\nCurrent Pattern (Length: {len(active_pattern)})")
                        print(visualize_list(active_pattern))
                
                else:
                    print("Invalid choice. Please try again.")
                
            except ValueError as e:
                print(f"Error: {str(e)}")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
        
        print("\nThank you for using List Operations Lab!")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()