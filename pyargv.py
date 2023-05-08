from sys import argv

ARG_TYPES =('flag', 'function')

class argvHandler:
    def __init__(self):
        self.args = argv
        self.tags = []

    def __checkTagAvailible(self, tag):
        if tag in self.tags:
            raise Exception(f'Tag "{tag}" was already taken')
        else: 
            self.tags.append(tag)

    def __checkTagNecessary(self, tag, necessary):
            if not tag in self.args and necessary:
                raise Exception(f'No "{tag}" tag was find, but it`s necessary')

    def setFlag(self, tag, necessary = False):
        self.__checkTagAvailible(tag)
        self.__checkTagNecessary(tag, necessary)
        def set(func):
            if tag in self.args:
                func()
        return set

    def setFunction(self, tag, necessary = False):
        self.__checkTagAvailible(tag)
        self.__checkTagNecessary(tag, necessary)
        def set(func):
            if tag in self.args:
                if self.args.index(tag) + 1 >= len(self.args):
                    raise Exception(f'Function-tag "{tag}" was given as last argv element')
                else:
                    i=1
                    _inputs = []
                    while not self.args[self.args.index(tag) + i].startswith('-'):
                        _inputs.append(self.args[self.args.index(tag) + i])
                        i += 1
                        if self.args.index(tag) + i == len(self.args):
                            break
                    if len(_inputs) == 0:
                        raise Exception(f'No argument after tag-function "{tag}"')
                    elif len(_inputs) == 1:
                        func(_inputs[0])
                    else:
                        func(_inputs)
        return set


if __name__ == '__main__':
    # python3 pyargvs -f -s hello -m hello world -n include_me
    handler = argvHandler()

    @handler.setFlag('-f')
    def bar():
        print('-f >> ', end='')
        print('Flag-tag simply checks if tag in argv.')

    @handler.setFunction('-s')
    def car(_inputs):
        print('-s >> ', end='')
        print('Single input return as given, not in list.')
        print('   ', _inputs)

    @handler.setFunction('-m')
    def foo(_inputs):
        print('-m >> ', end='')
        print('Multiple inputs return as list.')
        print('   ', _inputs)

    @handler.setFunction('-n', True)
    def foo(_inputs):
        print('-n >> ', end='')
        print('You can set some function-tag as nessesary, so python will raise Exception, if no such tag were provided.')
        print('   ', _inputs)

