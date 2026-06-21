"""
# SESSION 2

Problem Set Version 1
Problem 1: Reverse Sentence
Problem 2: Goldilocks Number
Problem 3: Delete Minimum
Problem 4: Sum of Digits
Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
Problem 6: Acronym
Problem 7: Good Things Come in Threes
Problem 8: Exclusive Elements
Problem 9: Merge Strings Alternately
Problem 10: Eeyore's House

Problem Set Version 2
Problem 1: String Array Equivalency
Problem 2: Count Even Strings
Problem 3: Secret Identity
Problem 4: Count Digits
Problem 5: Move Zeroes
Problem 6: Reverse Vowels of a String
Problem 7: Vantage Point
Problem 8: Left and Right Sum Differences
Problem 9: Common Cause
Problem 10: Exposing Superman

"""


def reverse_sentence(sentence):
    """
    Write a function reverse_sentence()
     that takes in a string sentence
    and returns the sentence with the 
    order of the words reversed. 
    The sentence will contain only
    alphabetic characters and spaces
    to separate the words. If there is 
    only one word in the sentence, 
    the function should return the original string.
    """
    sentence = sentence.split()
    if len(sentence) == 1:
        return "".join(sentence)
    return " ".join(reversed(sentence)) 

def goldilocks_approved(nums):
    """
    In the extended universe of fictional bears, 
    Goldilocks finds an enticing list of numbers
    in the Three Bears' house. She doesn't want 
    to take a number that's too high or too low 
    - she wants a number that's juuust right. 
    Write a function goldilocks_approved() that
    takes in the list of distinct positive integers 
    nums and returns any number from the list that 
    is neither the minimum nor the maximum value
    in the array, or -1 if there is no such number.

    Return the selected integer.
    """
    minimum, maximum = min(nums), max(nums)
    for number in nums:
        if number != minimum and number != maximum:
            return number
    return -1

def delete_minimum_elements(hunny_jar_sizes):
    """
    Pooh is eating all of his hunny jars
    in order of smallest to largest. 
    Given a list of integers hunny_jar_sizes,
    write a function delete_minimum_elements()
    that continuously removes the minimum
    element until the list is empty. Return
    a new list of the elements of hunny_jar_sizes
    in the order in which they were removed.
    """
    result = []
    hunny_jar_sizes.sort(reverse=True)
    while hunny_jar_sizes:
        result.append(hunny_jar_sizes.pop())
    return result


def sum_of_digits(num):
    """
    Write a function sum_of_digits() that accepts 
    an integer num and returns the sum of num's digits.
    """
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return sum(digits)

def final_value_after_operations(operations):
    """
    Tigger has developed a new programming language
     Tiger with only four operations and one variable tigger.

    bouncy and flouncy both increment the value of the
    variable tigger by 1.
    trouncy and pouncy both decrement the value of the
    variable tigger by 1.
    Initially, the value of tigger is 1 because he's 
    the only tigger around! Given a list of strings 
    operations containing a list of operations, 
    return the final value of tigger after performing 
    all the operations.
    """
    tigger = 1
    for operation in operations:
        if operation == 'bouncy' or operation == 'flouncy':
            tigger += 1
        elif operation == "trouncy" or operation == 'pouncy':
            tigger -= 1
    return tigger

def is_acronym(words, s):
    """
    Given an array of strings words and a string s,
    implement a function is_acronym() that returns
    True if s is an acronym of words and returns 
    False otherwise.

    The string s is considered an acronym of words
    if it can be formed by concatenating the first
    character of each string in words in order. For
    example, "pb" can be formed from ["pooh"", "bear"],
    but it can't be formed from ["bear", "pooh"].
    """
    answer = False
    if len(words) != len(s):
        return False 
    else:
        for i in range(len(words)):
            if words[i].startswith(s[i]):
                answer = True
    return answer

def make_divisible_by_3(nums):
    """
    Write a function make_divisible_by_3()
    that accepts an integer array nums. 
    In one operation, you can add or 
    subtract 1 from any element of nums.
    Return the minimum number of operations
    to make all elements of nums divisible by 3.
    """
    operations = 0
    for number in nums:
        operations += number % 3 if number % 3 <= 1 else abs(3 - (number % 3))
    return operations

def exclusive_elemts(lst1, lst2):
    """
    Given two lists lst1 and lst2,
    write a function exclusive_elemts()
    that returns a new list that contains
    the elements which are in lst1 but not
    in lst2 and the elements that are in lst2 
    but not in lst1.
    """
    return list(set(lst1) - set(lst2)) + list(set(lst2) - set(lst1))

def merge_alternately(word1, word2):
    """
    Write a function merge_alternately()
    that accepts two strings word1 and 
    word2. Merge the strings by adding
    letters in alternating order, starting 
    with word1. If a string is longer 
    than the other, append the additional 
    letters onto the end of the merged string.

    Return the merged string.
    """
def merge_alternately(word1, word2):
    """
    Write a function merge_alternately()
    that accepts two strings word1 and 
    word2. Merge the strings by adding
    letters in alternating order, starting
    with word1. If a string is longer than
    the other, append the additional letters
    onto the end of the merged string.

    Return the merged string.
    """
    res = []
    left, right = 0, 0 
    while left < len(word1) and right < len(word2):
        res.append(word1[left])
        res.append(word2[right])
        left += 1
        right += 1

    if left < len(word1):
        res.extend(word1[left:])
    if right < len(word2):
        res.extend(word2[right:])
    return "".join(res)

def good_pairs(pile1, pile2, k):
    """
    Eeyore has collected two piles of 
    sticks to rebuild his house and 
    needs to choose pairs of sticks 
    whose lengths are the right proportion.
    Write a function good_pairs() 
    that accepts two integer arrays
    pile1 and pile2 where each integer
    represents the length of a stick. 
    The function also accepts a positive 
    integer k. The function should return 
    the number of good pairs.

    A pair (i, j) is called good if pile1[i] is 
    divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 
    and 0 <= j <= len(pile2) - 1
    """
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                count += 1
    return count


def are_equivalent(word1, word2):
    """
    Given two string arrays word1 and word2,
    return True if the two arrays represent 
    the same string, and False otherwise.

    A string is represented by an array if 
    the array elements concatenated in order forms the string.
    """
    return "".join(word1) == "".join(word2)

def count_evens(lst):
    """
    Implement a function count_evens()
    that accepts a list of strings 
    lst as a parameter. The function 
    should return the number of strings 
    with an even length in the list.

    """
    count_even = 0
    for string in lst:
        if len(string) % 2 == 0:
            count_even += 1
    return count_even

def remove_name(people, secret_identity):
    """
    Write a function remove_name() to
    keep Batman's secret identity hidden. 
    The function accepts a list of names 
    people and a string secret_identity 
    and should return the list with any 
    instances of secret_identity removed. 
    The list must be modified in place; 
    you may not create any new lists as 
    part of your solution. 
    Relative order of the remaining 
    elements must be maintained.
    """
    i = 0
    while i < len(people):
        if people[i] == secret_identity:
            del people[i]
        i += 1
    return people

def count_digits(n):
    """
    Given a non-negative integer n,
    write a function count_digits() that returns
    the number of digits in n.
    You may not cast n to a string.
    """
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def move_zeroes(lst):
    """
    Write a function move_zeroes
    that accepts an integer array
    nums and returns a new list 
    with all 0s moved to the end
    of list. The relative order of
    the non-zero elements in the
    original list should be maintained.
    """
    front, back = [], []
    for num in lst:
        if num == 0:
            back.append(num)
        else:
            front.append(num)
    return front + back
    
def reverse_vowels(s):
    """
    Given a string s, reverse
    only all the vowels in the
    string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', 
    and they can appear in both lower
    and upper cases and more than once.
    """
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in "aeiouAEIOU":
            left += 1
        elif s[right] not in "aeiouAEIOU":
            right -= 1
        
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)

def highest_altitude(gain):
    """
    Batman is going on a scouting trip,
    surveying an area where he thinks
    Harley Quinn might commit her next
    crime spree. The area has many hills
    with different heights and Batman wants
    to find the tallest one to get the best
    vantage point. His scout trip consists of 
    n + 1 points at different altitudes. 
    Batman starts his trip at point 0 with altitude 0.

    Write a function highest_altitude() that accepts
    an integer array gain of length n where gain[i]
    is the net gain in altitude between points i​​​​​​ and 
    i + 1 for all (0 <= i < n). Return the highest
     altitude of a point.
    """
    current_max, current_alt = 0, 0
    for i in range(len(gain)):
        current_alt += gain[i]
        if current_alt > current_max:
            current_max = current_alt
    return current_max
        
def left_right_difference(nums):
    """
    Given a 0-indexed integer array
    nums, write a function left_right_difference
    that returns a 0-indexed integer array answer where:

    len(answer) == len(nums)
    answer[i] = left_sum[i] - right_sum[i]
    Where:

    left_sum[i] is the sum of elements to
    the left of the index i in the array nums.
    If there is no such element, left_sum[i] = 0
    right_sum[i] is the sum of elements to the
    right of the index i in the array nums. 
    If there is no such element, right_sum[i] = 0
    """
    left_sum = []
    lr_sum = 0
    rr_sum = 0
    right_sum = []
    for i in range(len(nums)):
        lr_sum += nums[i]
        left_sum.append(lr_sum)
    for i in range(len(nums)-1, -1 ,-1):
        rr_sum += nums[i]
        right_sum.append(rr_sum)
    for i in range(len(left_sum)):
        nums[i] = left_sum[i] - right_sum[::-1][i]
    return nums

def common_elements(lst1, lst2):
    """
    Write a function common_elements()
    that takes in two lists lst1 and lst2 
    and returns a list of the elements that 
    are common to both lists.
    """
    return list(set(lst1) & set(lst2))

def expose_superman(trust, n):
    """
    Metropolis has a population n,
    with each citizen assigned an
    integer id from 1 to n. There's 
    a rumor that Superman is an ordinary 
    citizen among this group.

    If Superman is an ordinary citizen, then:

    Superman trusts nobody.
    Everybody (except for Superman) trusts Superman.
    There is exactly one citizen that satisfies properties 1 and 2.

    Write a function expose_superman() that accepts a 2D array trust 
    where trust[i] = [ai, bi] representing that the person labeled 
    ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

    Return the label of Superman if he is hiding amongst the population 
    and can be identified, or return -1 otherwise.
    """
    trusts_someone, trusted_by_someone = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
    for a, b in trust:
        trusts_someone[a] += 1
        trusted_by_someone[b] += 1
    for i in range(1, n + 1):
        if trusts_someone[i] == 0 and trusted_by_someone[i] == n - 1:
            return i 
    return -1



def main():
    sentence = "tubby little cubby all stuffed with fluff"
    print(reverse_sentence(sentence))

    sentence = "Pooh"
    print(reverse_sentence(sentence))

    nums = [3, 2, 1, 4]
    print(goldilocks_approved(nums))

    nums = [1, 2]
    print(goldilocks_approved(nums))

    nums = [2, 1, 3]
    print(goldilocks_approved(nums))

    hunny_jar_sizes = [5, 3, 2, 4, 1]
    print(delete_minimum_elements(hunny_jar_sizes))

    hunny_jar_sizes = [5, 2, 1, 8, 2]
    print(delete_minimum_elements(hunny_jar_sizes))

    num = 423
    print(sum_of_digits(num))

    num = 4
    print(sum_of_digits(num))

    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

    words = ["christopher", "robin", "milne"]
    s = "crm"
    print(is_acronym(words, s))

    nums = [1, 2, 3, 4]
    print(make_divisible_by_3(nums))

    nums = [3, 6, 9]
    print(make_divisible_by_3(nums))

    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["piglet", "eeyore", "owl"]
    print(exclusive_elemts(lst1, lst2))

    lst1 = ["pooh", "roo"]
    lst2 = ["piglet", "eeyore", "owl", "kanga"]
    print(exclusive_elemts(lst1, lst2))

    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["pooh", "roo", "piglet"]
    print(exclusive_elemts(lst1, lst2))

    word1 = "wol"
    word2 = "oze"
    print(merge_alternately(word1, word2))

    word1 = "hfa"
    word2 = "eflump"
    print(merge_alternately(word1, word2))

    word1 = "eyre"
    word2 = "eo"
    print(merge_alternately(word1, word2))

    pile1 = [1, 3, 4]
    pile2 = [1, 3, 4]
    k = 1
    print(good_pairs(pile1, pile2, k))

    pile1 = [1, 2, 4, 12]
    pile2 = [2, 4]
    k = 3
    print(good_pairs(pile1, pile2, k))

    word1 = ["bat", "man"]
    word2 = ["b", "atman"]
    print(are_equivalent(word1, word2))

    word1 = ["alfred", "pennyworth"]
    word2 = ["alfredpenny", "word"]
    print(are_equivalent(word1, word2))

    word1  = ["cat", "wom", "an"]
    word2 = ["catwoman"]
    print(are_equivalent(word1, word2))

    lst = ["na", "nana", "nanana", "batman", "!"]
    print(count_evens(lst))

    lst = ["the", "joker", "robin"]
    print(count_evens(lst))

    lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
    print(count_evens(lst))

    people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
    secret_identity = 'Bruce Wayne'
    print(remove_name(people, secret_identity))

    n = 964
    print(count_digits(n))

    n = 0
    print(count_digits(n))

    lst = [1, 0, 2, 0, 3, 0]
    print(move_zeroes(lst))

    s = "robin"
    print(reverse_vowels(s))

    s = "BATgirl"
    print(reverse_vowels(s))

    s = "batman"
    print(reverse_vowels(s))

    gain = [-5, 1, 5, 0, -7]
    print(highest_altitude(gain))

    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(highest_altitude(gain))

    nums = [10, 4, 8, 3]
    print(left_right_difference(nums))

    nums = [1]
    print(left_right_difference(nums))

    lst1 = ["super strength", "super speed", "x-ray vision"]
    lst2 = ["super speed", "time travel", "dimensional travel"]
    print(common_elements(lst1, lst2))

    lst1 = ["super strength", "super speed", "x-ray vision"]
    lst2 = ["martial arts", "stealth", "master detective"]
    print(common_elements(lst1, lst2))

    n = 2
    trust = [[1, 2]]
    print(expose_superman(trust, n))

    n = 3
    trust = [[1, 3], [2, 3]]
    print(expose_superman(trust, n))

    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(expose_superman(trust, n))

if __name__ == "__main__":
    main()