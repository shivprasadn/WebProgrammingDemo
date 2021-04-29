def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with fuction")
    return wrapper
@announce
def hello():
    print("Hello,World!")

hello()