"""
# SESSION 1

Problem Set Version 1
Problem 1: Hundred Acre Wood
Problem 2: Greeting
Problem 3: Catchphrase
Problem 4: Return Item
Problem 5: Total Honey
Problem 6: Double Trouble
Problem 7: Poohsticks
Problem 8: Pooh's To Do's
Problem 9: Pairs
Problem 10: Split Haycorns
Problem 11: T-I-Double Guh-ER
Problem 12: Thistle Hunt

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

def welcome():
    """ Problem 1. 
    Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
    """
    print("Welcome to The Hundred Acre Wood!")

def greeting(name):
    """
    Write a function greeting() that accepts a single parameter, a string name, and prints the string
    """
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
	

def count_less_than(race_times, threshold):
    # Counter for the elements less than threshold
    counter = 0
    # Iterate through the elements in the array 
    for rt in race_times:
	    # Compare each element to threshold (<)
	    if rt < threshold:
	        # Count the elements that go through
	        counter = counter + 1
    return counter

def print_catchphrase(character):
    """
    Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

    Character    Catchphrase
    "Pooh"       "Oh bother!"
    "Tigger"     "TTFN: Ta-ta for now!"
    "Eeyore"     "Thanks for noticing me."
    "Christopher Robin"  "Silly old bear."
    If the given character does not match one
    of the characters included above,
    print "Sorry! I don't know <character>'s catchphrase!"
    """
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

def get_item(items, x):
    """
    mplement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

    """
    if x < 0 or x >= len(items):
        return None
    print(items[x])

def sum_honey(hunny_jars):
    """
    Winnie the Pooh wants to know 
    how much honey he has. Write a 
    function sum_honey() that accepts 
    a list of integers hunny_jars and 
    returns the sum of all
    elements in the list. Do not use 
    the built-in function sum().
    """
    total = 0
    for honey in hunny_jars:
        total += honey
    print(total)


def doubled(hunny_jars):
    """
    Help Winnie the Pooh 
    double his honey! Write a 
    function doubled() that 
    accepts a list of integers hunny_jars 
    as a parameter and multiplies each 
    element in the list by two. 
    
    Return the doubled list.
    """
    for i in range(len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    print(hunny_jars)

def count_less_than(race_times, threshold):
    """
    Winnie the Pooh and his friends 
    are playing a game called Poohsticks 
    where they drop sticks in a stream and 
    race them. They time how long it takes 
    each player's stick to float under 
    Poohsticks Bridge to score each round.

    Write a function count_less_than() 
    to help Pooh and his friends 
    determine how many players should
     move on to the next round of Poohsticks. 
     count_less_than() should accept a list of 
     integers race_times and an integer threshold 
     and return the number of race times less than threshold.
    """
    less_than_threshold = 0
    for stick in race_times:
        if stick < threshold:
            less_than_threshold += 1
    print(less_than_threshold)


def print_todo_list(tasks):
    """
    Write a function print_todo_list() 
    that accepts a list of strings named 
    tasks. The function should then number
     and print each task on a new line using
    the format:
    """
    print("Pooh's To Dos:")
    for i in range(0, len(tasks)):
        print(f"{i + 1}. {tasks[i]}")

def can_pair(item_quantities):
    """
    Rabbit is very particular about
     his belongings and wants to 
     own an even number of each thing 
     he owns. Write a function can_pair() 
     that accepts a list of integers item_quantities. 
     Return True if 
    each number in item_quantities is even.
     Return False otherwise.
     """
    for item in item_quantities:
        if item % 2 == 0:
            return False
    return True

def split_haycorns(quantity):
    """
    Piglet's has collected a 
    big pile of his favorite food,
     haycorns, and wants to split 
     them evenly amongst his friends. 
     Write a function split_haycorns() 
     to help Piglet determine the number of 
     ways he can split his haycorns into even 
     groups. split_haycorns() accepts a 
     positive integer quantity as a parameter 
     and returns a list of all divisors of quantity.
    """
    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)
    return divisors

def tiggerfy(s):
    """
    Signs in the Hundred Acre Wood have 
    been losing letters 
    as Tigger bounces around stealing any letters 
    he needs to spell out his name. Write a function 
    tiggerfy() that accepts a string s, and returns a new 
    string with the letters t, i, g, e, and r removed from it.
    """
    # create list from string
    remove = set("tiger")
    result = "".join(ch for ch in s if ch.lower() not in remove)
    print(result)


def locate_thistles(items):
    """
    Pooh, Piglet, and Roo are looking for thistles
     to gift their friend Eeyore. Write a function
      locate_thistles() that takes in a list of 
      strings items and returns a list of the 
      indices of any elements with value "thistle". 
      The indices in the resulting list should be 
      ordered from least to greatest.
    """
    value_thistles = []
    for index, item in enumerate(items):
        if item == "thistle":
            value_thistles.append(index)
    print(value_thistles)


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
    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 4
    print(count_less_than(race_times, threshold))

    race_times = []
    threshold = 4
    print(count_less_than(race_times, threshold))

    character = "Pooh"
    print_catchphrase(character)

    character = "Piglet"
    print_catchphrase(character)

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    get_item(items, x)

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5
    get_item(items, x)

    hunny_jars = [2, 3, 4, 5]
    sum_honey(hunny_jars)

    hunny_jars = []
    sum_honey(hunny_jars)

    hunny_jars = [1, 2, 3]
    doubled(hunny_jars)

    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 4
    count_less_than(race_times, threshold)

    race_times = []
    threshold = 4
    count_less_than(race_times, threshold)

    tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(tasks)

    tasks = []
    print_todo_list(tasks)

    item_quantities = [2, 4, 6, 8]
    can_pair(item_quantities)

    item_quantities = [1, 2, 3, 4]
    can_pair(item_quantities)

    item_quantities = []
    can_pair(item_quantities)

    quantity = 6
    split_haycorns(quantity)

    quantity = 1
    split_haycorns(quantity)

    s = "suspicerous"
    tiggerfy(s)

    s = "Trigger"
    tiggerfy(s)

    s = "Hunny"
    tiggerfy(s)

    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    locate_thistles(items)

    items = ["book", "bouncy ball", "leaf", "red balloon"]
    locate_thistles(items)

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

