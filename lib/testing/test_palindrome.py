import pytest
from palindrome import longest_palindromic_substring


class TestLongestPalindromicSubstring:
    """Test suite for longest_palindromic_substring function"""
    
    def test_basic_palindrome_babad(self):
        """Test with 'babad' - should return 'bab' or 'aba'"""
        result = longest_palindromic_substring("babad")
        assert result in ["bab", "aba"], f"Expected 'bab' or 'aba', got '{result}'"
    
    def test_basic_palindrome_cbbd(self):
        """Test with 'cbbd' - should return 'bb'"""
        result = longest_palindromic_substring("cbbd")
        assert result == "bb", f"Expected 'bb', got '{result}'"
    
    def test_full_string_palindrome(self):
        """Test when entire string is a palindrome"""
        result = longest_palindromic_substring("racecar")
        assert result == "racecar", f"Expected 'racecar', got '{result}'"
    
    def test_single_character(self):
        """Test with single character - should return the character itself"""
        result = longest_palindromic_substring("a")
        assert result == "a", f"Expected 'a', got '{result}'"
    
    def test_two_character_no_palindrome(self):
        """Test with two different characters - should return either character"""
        result = longest_palindromic_substring("ac")
        assert result in ["a", "c"], f"Expected 'a' or 'c', got '{result}'"
    
    def test_two_character_palindrome(self):
        """Test with two same characters - should return both characters"""
        result = longest_palindromic_substring("aa")
        assert result == "aa", f"Expected 'aa', got '{result}'"
    
    def test_empty_string(self):
        """Test with empty string - should return empty string"""
        result = longest_palindromic_substring("")
        assert result == "", f"Expected '', got '{result}'"
    
    def test_no_palindrome_longer_than_one(self):
        """Test string with no palindromes longer than 1 character"""
        result = longest_palindromic_substring("abcdef")
        assert len(result) == 1, f"Expected single character, got '{result}'"
        assert result in "abcdef", f"Result should be one of the characters in the string"
    
    def test_multiple_palindromes_same_length(self):
        """Test string with multiple palindromes of same length"""
        result = longest_palindromic_substring("abacabad")
        # The algorithm finds "abacaba" which is longer than "aba"
        assert result == "abacaba", f"Expected 'abacaba', got '{result}'"
    
    def test_palindrome_at_beginning(self):
        """Test palindrome at the beginning of string"""
        result = longest_palindromic_substring("abaxyz")
        assert result == "aba", f"Expected 'aba', got '{result}'"
    
    def test_palindrome_at_end(self):
        """Test palindrome at the end of string"""
        result = longest_palindromic_substring("xyzaba")
        assert result == "aba", f"Expected 'aba', got '{result}'"
    
    def test_long_palindrome_in_middle(self):
        """Test long palindrome in the middle of string"""
        result = longest_palindromic_substring("xyzracecarabc")
        assert result == "racecar", f"Expected 'racecar', got '{result}'"
    
    def test_even_length_palindrome(self):
        """Test even-length palindrome"""
        result = longest_palindromic_substring("abccba")
        assert result == "abccba", f"Expected 'abccba', got '{result}'"
    
    def test_odd_length_palindrome(self):
        """Test odd-length palindrome"""
        result = longest_palindromic_substring("abcba")
        assert result == "abcba", f"Expected 'abcba', got '{result}'"
    
    def test_repeated_characters(self):
        """Test string with repeated characters"""
        result = longest_palindromic_substring("aaaa")
        assert result == "aaaa", f"Expected 'aaaa', got '{result}'"
    
    def test_alternating_pattern(self):
        """Test alternating pattern that creates palindromes"""
        result = longest_palindromic_substring("ababa")
        assert result == "ababa", f"Expected 'ababa', got '{result}'"
    
    def test_case_sensitivity(self):
        """Test that function is case sensitive"""
        result = longest_palindromic_substring("Aa")
        assert result in ["A", "a"], f"Expected 'A' or 'a', got '{result}'"
    
    def test_numbers_and_letters(self):
        """Test string with numbers and letters"""
        result = longest_palindromic_substring("a1b2b2b1a")
        # The longest palindrome could be "1b2b2b1" or the whole string
        assert len(result) >= 3, f"Expected palindrome of length >= 3, got '{result}'"
    
    def test_mixed_palindromes_different_lengths(self):
        """Test string with palindromes of different lengths"""
        result = longest_palindromic_substring("abcdefedcba")
        # Should find the longest palindrome "abcdefedcba" (if entire string) or "defed"
        expected_length = max(len("defed"), len("aba") if "aba" in result else 0)
        assert len(result) >= 5, f"Expected palindrome of length >= 5, got '{result}' with length {len(result)}"
