# Strategy:  Iterate over a copy
users = {}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# Loop statements may have an else clause; 
# it is executed when the loop terminates through exhaustion of the iterable (with for) or 
# when the condition becomes false (with while), 
# but not when the loop is terminated by a break statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# The pass statement does nothing. 
# It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

def initlog(*args):
    pass   # Remember to implement this!


# This is documentation string, or docstring.
# There are tools which use docstrings to automatically produce online or printed documentation, 
# or to let the user interactively browse through code
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# def cheeseshop(kind, *arguments, **keywords):
#    print("-- Do you have any", kind, "?")
#    print("-- I'm sorry, we're all out of", kind)
#    for arg in arguments:
#        print(arg)
#    print("-" * 40)
#    for kw in keywords:
#        print(kw, ":", keywords[kw])
#
#cheeseshop("Limburger", "It's very runny, sir.",
#           "It's really very, VERY runny, sir.",
#           shopkeeper="Michael Palin",
#           client="John Cleese",
#           sketch="Cheese Shop Sketch")
#
# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch

#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#      -----------    ----------     ----------
#        |             |                  |
#        |        Positional or keyword   |
#        |                                - Keyword only
#         -- Positional only


# Arbitrary argument list
#def concat(*args, sep="/"):
#     return sep.join(args)
#
# concat("earth", "mars", "venus")
#'earth/mars/venus'
# concat("earth", "mars", "venus", sep=".")
#'earth.mars.venus'