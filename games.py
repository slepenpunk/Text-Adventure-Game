class Player:
    """Simple game"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        res = f'{self.name} - {self.score}'
        return res


def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question):
    response = int(input(question))
    return response


if __name__ == '__main__':
    print('You are play that module here, not import it.')
