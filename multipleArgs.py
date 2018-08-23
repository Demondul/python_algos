def varargs(arg1, *args):
    print("args is of " + str(type(args)))
    for i in args:
        print(i)
varargs("one", "two", "three",[1,2,3]) # output: args is of <class 'tuple'>
