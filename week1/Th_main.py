"""

Problem Set Version 2
Problem 1: Batman
Problem 2: Mad Libs
Problem 3: Trilogy
Problem 4: Last
Problem 5: Concatenate
Problem 6: Squared
Problem 7: NaNaNa Batman!
Problem 8: Find the Villain
Problem 9: Odd
Problem 10: Up and Down
Problem 11: Running Sum
Problem 12: Shuffle

"""

def batman():
    """
    Write a function batman() that prints the string
     "I am vengeance. I am the night. I am Batman!".
    """
    print("I am vengeance. I am the night. I am Batman!")

def madlib(verb):
    """
    Write a function madlib() that accepts one parameter, 
    a string verb. The function should print the sentence: 
    "I have one power. I never <verb>. - Batman".
    """
    print(f"I have one power. I never {verb}. - Batman")

def trilogy(year):
    """
    Write a function trilogy() 
    that accepts an integer year 
    and prints the title of the 
    Batman trilogy movie released 
    that year as outlined below.

    Year	Movie Title
    2005	"Batman Begins"
    2008	"The Dark Knight"
    2012	"The Dark Knight Rises"
    
    If the given year does not match 
    one of the years in the table above, 
    print "Christopher Nolan did not 
    release a Batman movie in <year>."

    """
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")

def get_last(items):
    """
    Implement a function get_last() 
    that accepts a list of items 
    items and returns the last item 
    in the list. If the list is empty, return None.
    """
    if not items:
        return None
    print(items[-1])

def concatenate(words):
    """
    Write a function concatenate() that 
    takes in a list of strings words and 
    returns a string 
    concatenated that concatenates all elements in words.
    """
    concatenation = ""
    for string in words:
        concatenation += string 
    print(concatenation)

def squared(numbers):
    """
    Write a function squared() that accepts
     a list of integers numbers as a parameter 
    and squares each item in the list. 
    Return the squared list.
    """
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    print(numbers) 

def nanana_batman(x):
    """
    Write a function nanana_batman() 
    that accepts an integer x and 
    prints the string "nanana batman!" where 
    "na" is repeated x times. Do not use the * operator.
    """
    print(f"{"na" * x} batman!")

def find_villain(crowd, villain):
    """
    Write a function find_villain() 
    that accepts a list crowd and a 
    value villain as parameters and 
    returns a list of all 
    indices where the villain 
    is found hiding in the crowd.
    """
    indices = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            indices.append(i)
    print(indices)

def get_odds(nums):
    """
    Write a function get_odds() 
    that takes in a list of integers 
    nums and returns a 
    new list containing all the odd numbers in nums.
    """
    odds = []
    for number in nums:
        if number % 2 != 0:
            odds.append(number)
    print(odds)

def up_and_down(lst):
    """
    Write a function up_and_down()
     that accepts a list of integers
      lst as a parameter. The function 
      should return the number 
    of odd numbers minus the number of
     even numbers in the list.
    """
    odd, even = 0, 0
    for number in lst:
        if number % 2 == 0:
            even += 1
        elif number % 2 != 0:
            odd += 1
    print(odd - even)


def running_sum(superhero_stats):
    """
    Write a function running_sum() that
    accepts a list of integers superhero_stats
    representing the number of crimes Batman
    has stopped each month in Gotham City.
    The function should modify the list 
    to return the running sum such
    that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]).
    You must modify the list in place; 
    you may not create any new lists as part of your solution.
    """
    running_sum = 0 
    for i in range(len(superhero_stats)):
        running_sum += superhero_stats[i]
        superhero_stats[i] = running_sum 
    print(superhero_stats)


def shuffle(cards):
    """
    Write a function shuffle() 
    that accepts a list cards
     of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. 
    Return the list in the form [x1,y1,x2,y2,...,xn,yn].
    """
    result = []
    other_half = cards[len(cards) // 2: ]
    for i in range(len(cards) // 2):
        result.append(cards[i])
        result.append(other_half[i])
    print(result)


def main():
    batman()

    verb = "give up"
    madlib(verb)

    verb = "nap"
    madlib(verb)

    year = 2008
    trilogy(year)

    year = 1998
    trilogy(year)

    items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
    get_last(items)

    items = []
    get_last(items)

    words = ["vengeance", "darkness", "batman"]
    concatenate(words)

    words = []
    concatenate(words)

    numbers = [1, 2, 3]
    squared(numbers)

    x = 6
    nanana_batman(x)

    x = 0
    nanana_batman(x)

    crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
    villain = 'The Joker'
    find_villain(crowd, villain)

    nums = [1, 2, 3, 4]
    get_odds(nums)

    nums = [2, 4, 6, 8]
    get_odds(nums)

    lst = [1, 2, 3]
    up_and_down(lst)

    lst = [1, 3, 5]
    up_and_down(lst)

    lst = [2, 4, 10, 2]
    up_and_down(lst)

    superhero_stats = [1, 2, 3, 4]
    running_sum(superhero_stats)

    superhero_stats = [1, 1, 1, 1, 1]
    running_sum(superhero_stats)

    superhero_stats = [3, 1, 2, 10, 1]
    running_sum(superhero_stats)

    cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
    shuffle(cards)

    cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
    shuffle(cards)

    cards = [10, 10, 2, 2]
    shuffle(cards)

if __name__ == "__main__":
    main()