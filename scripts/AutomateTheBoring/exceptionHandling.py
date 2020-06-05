'''
Exception handing, pgs 72-73

prevents program from crashing, should an error be encountered

'''


def div42by(divideby):
    try:
        return 42 / divideby
    except  ZeroDivisionError:
        print("Error: You tried to divide by zero.")        # we offer an exception policy, in case of failure
    except:
        print("generalized error handler")
        
print(div42by(2))
print(div42by(12))
print(div42by(22))
print(div42by(21))
print(div42by(0))