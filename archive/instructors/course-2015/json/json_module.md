

##### An introduction to the JSON Module in Python


#### 0. Today's deep dive: Playing more with python's types and conversions (10 min)

please enter the python interactive interpreter: 
    ```$python
    ```    
    in the interpreter:    

    ```python
    number_list = range(11)

    string_list = list()
    for num in number_list:
      string_list.append(str(num))

    print(string_list)
    print(number_list)

    string_list[:5]
    number_list[:-3]

    string_nums = '5' + '4'
    integer_conversion = int(string_nums)

    string_float = '3.25' + '1.02'
    float_conversion = float(string_float)
    ```

  a. where are these referenced in [the official python docs?](https://docs.python.org/2/library/index.html) 

#### 1. Review JSON format (20 min)

  a. http://www.json.org/    
  b. Values: string, number, object, array, true, false, null    
  c. Root Object must be a container: object, array
  d. json lint webapp at [http://jsonlint.com/](http://jsonlint.com/)


#### 2. Explain Python Data Types & Containers' relationship to JSON library (15 min) 

  a. Json to Python Standard Translation: https://docs.python.org/2/library/json.html#encoders-and-decoders  
  b. note about: '' versus u'' versus r''  (string types in Python 2)     
  c. briefly learning how to reference and read the official python documentation    

#### 3. Sample JSON (15 min)

  a. We are going to load in the data from the file "abcde.json" in the examples folder       
  b. if you really prefer to later, get a json encoded object from [this url](https://raw.githubusercontent.com/PyClass/PyClassLessons/master/lessons/json_module/examples/abcdef.json) using a 3rd party module of python's called the "requests" module        
  c. The egregiously hard way to get the same data: use urllib to open and parse data from https://raw.githubusercontent.com/PyClass/PyClassLessons/master/lessons/json_module/examples/abcdef.json    
 


#### 4. Using json library functions (20 min)
   
  a. to the docs! [json module](https://docs.python.org/2/library/json.html) in stdlib      
  b. Functions: load, dump, loads, dumps    
  c. loads and dumps are 'load string' and 'dump string'   
  d. Quick Detour into a great pythonic idiom - The 'with' keyword - specifically for file objects.    
  ```python
    with open('../abcde.json') as f:        
    for line in f:
        print line     
  ```
  e. Json load and loads will provide UTF-8 data, u'data', which is OK! Just treat it like a string without the u''    


5. Additional Resources

  a. Command line: $ python -m json.tool file.ext    
  b. Here's an example of json.loads() on a string variable: https://docs.python.org/2/library/json.html#repeated-names-within-an-object    
  c. Unicode characters (uXXXX): http://www.unicode.org/charts/    
  d. Duck Typing - http://en.wikipedia.org/wiki/Duck_typing    
  (don't explicly use types in your functions/checks)    

