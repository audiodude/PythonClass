

try:
    yourmom = "hello"
    print yourmom
except NameError as e:
    print e

# The eval() will allow us to see the compiling error.
try:
    eval(
    """
try:
    ando = 5
except Exception as e:
    print e
    """ 
    )
            
    # and = 5   # Uncommenting prevents this whole script from compiling. 
except Exception as e:
    print e


print "We made it to the end!"
