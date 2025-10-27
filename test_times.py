from times import compute_overlap_time, time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

def test_multiple_intervals_both_ranges():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 300)
    range2 = time_range("2010-01-12 10:15:00", "2010-01-12 11:15:00", 2, 300)
    result = compute_overlap_time(range1, range2)
    assert len(result) == 3
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)


def test_ranges_end_start_same_time():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    result = compute_overlap_time(range1, range2)
    expected = [('2010-01-12 11:00:00', '2010-01-12 11:00:00')]
    assert result == expected

def test_backwards_time_range():
    with pytest.raises(ValueError) as excinfo:
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
    assert "End time cannot be before start time" in str(excinfo.value)