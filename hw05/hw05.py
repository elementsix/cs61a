import inspect

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"

    incorrect_passwords = []

    def withdraw(amount, pswd):
        nonlocal balance

        if len(incorrect_passwords) == 3:
            return 'Your account is locked. Attempts: {0}'.format(incorrect_passwords)

        elif pswd == password:
            if amount > balance:
                return 'Insufficient funds'
            balance -= amount
            return balance

        else:
            incorrect_passwords.append(pswd)
            return 'Incorrect password'

    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"

    # old_password and new_password get stored as part of the returned function

    def joint_withdraw(amount, pswd):
        if (pswd == old_password or pswd == new_password):
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, pswd)   # made this new_password earlier, so much pain

    error = withdraw(0, old_password)
    if type(error) == str:
        return error

    return joint_withdraw


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, product, cost):
        self.product = product
        self.cost = cost
        self.stock = 0
        self.balance = 0

    def vend(self):
        if (self.stock == 0):
            return 'Machine is out of stock.'
        elif (self.balance < self.cost):
            return 'You must deposit ${0} more.'.format(self.cost - self.balance)
        elif (self.balance == self.cost):
            self.balance = 0
            self.stock -= 1
            return 'Here is your {0}.'.format(self.product)
        else:
            retval = self.balance - self.cost
            self.balance = 0
            self.stock -= 1
            return 'Here is your {0} and ${1} change.'.format(self.product, retval)

    def deposit(self, amount):
        if (self.stock == 0):
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)

        self.balance += amount
        return 'Current balance: ${0}'.format(self.balance)

    def restock(self, items):
        self.stock += items
        return 'Current {0} stock: {1}'.format(self.product, self.stock)


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, init_object):
        self.init_object = init_object

    def ask(self, *args):

        words_in_request = args[0].split()

        if not args[0].startswith('please'):
            return 'You must learn to say please first.'

        elif len(words_in_request) > 2:
            return 'Thanks for asking, but I know not how to {0}'.format(' '.join(words_in_request[1:]))

        else :
            if isinstance(self.init_object, VendingMachine):

                if hasattr(self.init_object, words_in_request[-1]):
                    task = getattr(self.init_object, words_in_request[-1])

                    if len(inspect.getargspec(task).args) > 1:
                        return task(args[1])
                    else:
                        return task()

                else:
                    return 'Thanks for asking, but I know not how to {0}'.format(words_in_request[-1])


            elif isinstance(self.init_object, MissManners):

                if args[0] == 'please ask':
                    task = getattr(self.init_object.init_object, args[1].split()[-1])

                    if len(inspect.getargspec(task).args) > 1:
                        return task(args[2])
                    else:
                        return task()

                else:
                    return 'Thanks for asking, but I know not how to {0}'.format(args[0].split()[-1])


            elif isinstance(self.init_object, int):

                try: # getattr(self.init_object, words_in_request[-1]):
                    task = getattr(self.init_object, words_in_request[-1])

                    return task(args[1])

                except AttributeError:
                    return 'Thanks for asking, but I know not how to {0}'.format(words_in_request[-1])



