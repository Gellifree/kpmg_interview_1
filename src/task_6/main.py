# Solve this task with recursive programming.
# In this exercise you have to find how much cookies can be consumed with the
# given amount of money.


# If you have money, spend it on cookies
# If you have cookies eat them, and collect the wrappers, get more cookies
# and repeat
def eat(money, price, wrap, cookies, cookies_consumed, wrappers_have):
    if(money > price):
        cookies = int(money / price)
        money -= cookies * price
        eat(money, price, wrap, cookies, cookies_consumed, wrappers_have)
    elif(cookies > 0):
        cookies_consumed[0] += cookies
        wrappers_have = cookies
        cookies = int(wrappers_have / wrap)
        wrappers_have = 0
        eat(money, price, wrap, cookies, cookies_consumed, wrappers_have)


# The consumed cookies array with only 1 element is a working, but not pretty
# solution
def main():
    money = 16
    price = 2
    wrap = 2

    cookies = 0
    cookies_consumed = [0]
    wrappers_have = 0
    eat(money, price, wrap, cookies, cookies_consumed, wrappers_have)
    print(f'The number of consumed cookies is {cookies_consumed[0]}.')

if __name__ == '__main__':
    main()
