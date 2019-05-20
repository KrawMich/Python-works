def italic(funkcja):
    def wrapper(*args, **kwargs):
        result = funkcja(*args,**kwargs)
        return f'<i>{result}</i>'
    return wrapper

def bold(funkcja):
    def wrapper(*args, **kwargs):
        result = funkcja(*args,**kwargs)
        return f'<b>{result}</b>'
    return wrapper


@italic
def hello():
    return 'Hello'

@bold
def goodbye():
    return 'Goodbye'

@italic
@bold
def whatever():
    return 'Whatever'


def test_kursywa():
    assert hello() == '<i>Hello</i>'

def test_pogrubienie():
    assert goodbye() == '<b>Goodbye</b>'

def test_polaczony():
    assert whatever() == '<i><b>Whatever</b></i>'

