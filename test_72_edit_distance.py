from code_72_edit_distance import Solution

def test_example_1():
    s = Solution()
    word1 = "horse"
    word2 = "ros"
    output = 3
    assert s.minDistance(word1,word2) == output

def test_example_2():
    s = Solution()
    word1 = "intention"
    word2 = "execution"
    output = 5
    assert s.minDistance(word1,word2) == output
