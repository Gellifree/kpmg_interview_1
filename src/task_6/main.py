# Solve this task with recursive programming.
# In this exercise you have to find how much cookies can be consumed with the
# given amount of money.



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


# TODO: test it with a list of data
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
