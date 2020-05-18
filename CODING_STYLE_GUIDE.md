# Summary
References: POCU Java Coding Standards, Google

## Main Coding Standards
1. Lower case for moudle/package names
    ```python
    import awesome_module
    ```
2. No wildcard imports
    ```python
    import awesome_module.*
    ```
3. Use Pascal for classes
    ```python
    class AwesomeClass(object):
        # ...
    ```
4. Add `_` if protected, `__` if private, none if public
    ```python
    class AwesomeClass(object):
        def __init__(self, name: str, age: int, height: float):
            self.name = name    # public
            self._age = age     # protected
            self.__height = height  # private
        def public_method(self) -> None:
            # ...
        def _protected_method(self) -> None:
            # ...
        def __private_method(self) -> None:
            # ...
    ```
5. Use underscores for methods
    ```python
    class AwesomeClass(object):
        # ...
        def awesome_method(self) -> int:
            return 0
    ```

6. Use underscores for local variables and method parameters
    ```python
    awesome_local_variable = 3
    
    def awesome_function(number: int) -> int:
        return number
    ```

7. Use verb-object pair for method names
    ```python
    class AwesomeClass(object):
        def __init__(self, name: str):
            self.__name = name;
    
        def get_name(self) -> str:
            return self.__name
    ```

8. Use ALL_CAPS_SEPARATED_BY_UNDERSCORE for constants
    ```python
    class AwesomeClass(object):
        @constant
        def AWESOME_CONSTANT_PI(self):
            return 3.14159
    ```

9. Use underscores for member variables
    ```python
    class AwesomeClass(object):
        def __init__(self, awesome_variable: str):
            self.awesome_variable = awesome_variable
    ```

10. Methods with return values must have a name describing the value returned
    ```python
    class AwesomeClass(object):
        def __init__(self, name: str):
            self.__name = name;
    
        def get_name(self) -> str:  # get "name"
            return self.__name
    ```

11. Use descriptive variable names unless using a trivial index for a loop
    ```python
    i = 3   # NO
    index = 3   # YES
    
    ch = 'c'    # NO
    character = 'c' # YES
    
    for i in range(10): # YES
    ```

12. Acronyms shouldn't be capitalized if not a constant
    ```python
    ID = "awesome"  # NO
    id = "awesome"  # YES
    
    HTTP = "0.0.0.1"    # NO
    http = "0.0.0.1"    # YES
    ```

13. Use properties for getter/setter
    ```python
    class AwesomeClass(object):
        def __init__(self, name: str, age: int, height: float):
            self.name = name    # public
            self._age = age     # protected
            self.__height = height  # private
        
        @property   # getter. must precede setter
        def name(self) -> str:
            return self.__name
    
        @name.setter
        def name(self, name: str) -> None:
            self.__name = name
    ```

14. Declare local variables as close as possible to the first line where it is being used

15. If a case should not happen, use assert to intentionally fail it.
    ```python
    if expr1:
        # ...
    elif expr2:
        # ...
    else
        assert(False)    # shouldn't happen
    ```

16. Names of recursive methods end with recursive
    ```python
    def fibonacci_recursive(index: int) -> int:
        # ...
    ```

17. Class structure:
    1. `__init__`
        1. public member variables
        2. protected member variables
        3. private member variables
    2. public methods
    3. protected methods
    4. private methods

18. Overloading should be avoided mostly
    * NO
        ```python
        def get_data(index: int) -> List[int]:
        def get_data(name: str) -> List[int]:
        ```
    * YES
        ```python
        def get_data_by_index(index: int) -> List[int]:
        def get_data_by_name(name: str) -> List[int]:
        ```
19. Use assert frequently, but with parentheses
    ```python
    assert False    # NO
    assert(False)  # YES
    ```

20. Use type annotations wherever possible
    ```python
    def returns_integer(number: int) -> int:    # OK
        return number
    def returns_something(number):              # NO
        return number
    ```

21. Prefer not to allow `None` parameters in your method

22. If `None` parameter is used, postfix the parameter name with `or_none`
    ```python
    import typing import Union
    
    def print_name(name_or_none: Union[str, None]) -> None:
        print(name_or_none)
    ```

23. If `None` is returned from any method, postfix the method name with `or _none`
    ```python
    import typing import Union
    
    def get_name_or_none(self) -> Union[str, None]:
        return self.__name
    ```

24. No semicolons
    ```python
    index = 3; name = "Mike"    # NO
    
    index = 3
    name = "Mike"               # YES
    ```
## Code Formatting
1. Use PyCharm's default settings for tabs. ctrl+alt+l

<!--
AUTHORS:
Prefer only GitHub-flavored Markdown in external text.
See README.md for details.
-->

# Google Python Style Guide (revised)


<a id="1-background"></a>

<a id="background"></a>
## 1 Background 

Python is the main dynamic language used at Google. This style guide is a list
of *dos and don'ts* for Python programs.

To help you format code correctly, we've created a [settings file for
Vim](google_python_style.vim). For Emacs, the default settings should be fine.

Many teams use the [yapf](https://github.com/google/yapf/)
auto-formatter to avoid arguing over formatting.


<a id="s2-python-language-rules"></a>
<a id="2-python-language-rules"></a>

<a id="python-language-rules"></a>
## 2 Python Language Rules 

<a id="s2.2-imports"></a>
<a id="22-imports"></a>

<a id="imports"></a>
### 2.2 Imports

> only for packages/modules

Use `import` statements for packages and modules only, not for individual
classes or functions. Note that there is an explicit exemption for imports from
the [typing module](#typing-imports).

<a id="s2.2.1-definition"></a>
<a id="221-definition"></a>

<a id="imports-definition"></a>

#### 2.2.4 Decision 

* Use `import x` for importing packages and modules.
* Use `from x import y` where `x` is the package prefix and `y` is the module
name with no prefix.
* Use `from x import y as z` if two modules named `y` are to be imported or if
`y` is an inconveniently long name.
* Use `import y as z` only when `z` is a standard abbreviation (e.g., `np` for
`numpy`).

For example the module `sound.effects.echo` may be imported as follows:

```python
from sound.effects import echo
...
echo.EchoFilter(input, output, delay=0.7, atten=4)
```

Do not use relative names in imports. Even if the module is in the same package,
use the full package name. This helps prevent unintentionally importing a
package twice.

Imports from the [typing module](#typing-imports) and the
[six.moves module](https://six.readthedocs.io/#module-six.moves)
are exempt from this rule.

<a id="s2.3-packages"></a>
<a id="23-packages"></a>

<a id="packages"></a>
### 2.3 Packages 

Import each module using the full pathname location of the module.

<a id="s2.3.1-pros"></a>
<a id="231-pros"></a>

<a id="packages-pros"></a>

#### 2.3.3 Decision 

All new code should import each module by its full package name.

Imports should be as follows:

Yes:

```python
# Reference absl.flags in code with the complete name (verbose).
import absl.flags
from doctor.who import jodie

FLAGS = absl.flags.FLAGS
```

```python
# Reference flags in code with just the module name (common).
from absl import flags
from doctor.who import jodie

FLAGS = flags.FLAGS
```

No: _(assume this file lives in `doctor/who/` where `jodie.py` also exists)_

```python
# Unclear what module the author wanted and what will be imported.  The actual
# import behavior depends on external factors controlling sys.path.
# Which possible jodie module did the author intend to import?
import jodie
```

The directory the main binary is located in should not be assumed to be in
`sys.path` despite that happening in some environments.  This being the case,
code should assume that `import jodie` refers to a third party or top level
package named `jodie`, not a local `jodie.py`.


<a id="s2.4-exceptions"></a>
<a id="24-exceptions"></a>

<a id="exceptions"></a>
### 2.4 Exceptions 

> Don't use them unless necessary.
> 
> If you need to check an error, use assert.

<a id="s2.5-global-variables"></a>
<a id="25-global-variables"></a>

<a id="global-variables"></a>
### 2.5 Global variables 

Avoid global variables.

<a id="s2.5.1-definition"></a>
<a id="251-definition"></a>

<a id="global-variables-definition"></a>
#### 2.5.4 Decision 

Avoid global variables.

While they are technically variables, module-level constants are permitted and
encouraged. For example: `MAX_HOLY_HANDGRENADE_COUNT = 3`. Constants must be
named using all caps with underscores. See [Naming](#s3.16-naming) below.

If needed, globals should be declared at the module level and made internal to
the module by prepending an `_` to the name. External access must be done
through public module-level functions. See [Naming](#s3.16-naming) below.

<a id="s2.6-nested"></a>
<a id="26-nested"></a>

<a id="nested-classes-functions"></a>
### 2.6 Nested/Local/Inner Classes and Functions 

> Avoid them.

<a id="s2.7-list_comprehensions"></a>
<a id="27-list_comprehensions"></a>
<a id="list_comprehensions"></a>
<a id="list-comprehensions"></a>

<a id="comprehensions"></a>
### 2.7 Comprehensions & Generator Expressions 

> Avoid them when it starts to deteriorate the readability.

Okay to use for simple cases.

<a id="s2.7.4-decision"></a>
<a id="274-decision"></a>

<a id="comprehensions-decision"></a>
#### 2.7.4 Decision 

Okay to use for simple cases. Each portion must fit on one line: mapping
expression, `for` clause, filter expression. Multiple `for` clauses or filter
expressions are not permitted. Use loops instead when things get more
complicated.

```python
Yes:
  result = [mapping_expr for value in iterable if filter_expr]

  result = [{'key': value} for value in iterable
            if a_long_filter_expression(value)]

  result = [complicated_transform(x)
            for x in iterable if predicate(x)]

  descriptive_name = [
      transform({'key': key, 'value': value}, color='black')
      for key, value in generate_iterable(some_input)
      if complicated_condition_is_met(key, value)
  ]

  result = []
  for x in range(10):
      for y in range(5):
          if x * y > 10:
              result.append((x, y))

  return {x: complicated_transform(x)
          for x in long_generator_function(parameter)
          if x is not None}

  squares_generator = (x**2 for x in range(10))

  unique_names = {user.name for user in users if user is not None}

  eat(jelly_bean for jelly_bean in jelly_beans
      if jelly_bean.color == 'black')
```

```python
No:
  result = [complicated_transform(
                x, some_argument=x+1)
            for x in iterable if predicate(x)]

  result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

  return ((x, y, z)
          for x in range(5)
          for y in range(5)
          if x != y
          for z in range(5)
          if y != z)
```

<a id="s2.8-default-iterators-and-operators"></a>

<a id="default-iterators-operators"></a>
### 2.8 Default Iterators and Operators 

> Use them

Use default iterators and operators for types that support them, like lists,
dictionaries, and files.

<a id="s2.8.4-decision"></a>
<a id="284-decision"></a>

<a id="default-iterators-operators-decision"></a>
#### 2.8.4 Decision 

Use default iterators and operators for types that support them, like lists,
dictionaries, and files. The built-in types define iterator methods, too. Prefer
these methods to methods that return lists, except that you should not mutate a
container while iterating over it. Never use Python 2 specific iteration
methods such as `dict.iter*()` unless necessary.

```python
Yes:  for key in adict: ...
      if key not in adict: ...
      if obj in alist: ...
      for line in afile: ...
      for k, v in adict.items(): ...
      for k, v in six.iteritems(adict): ...
```

```python
No:   for key in adict.keys(): ...
      if not adict.has_key(key): ...
      for line in afile.readlines(): ...
      for k, v in dict.iteritems(): ...
```

<a id="s2.10-lambda-functions"></a>
<a id="210-lambda-functions"></a>

<a id="lambdas"></a>
### 2.10 Lambda Functions 

Okay for one-liners.

<a id="s2.10.4-decision"></a>
<a id="2104-decision"></a>

<a id="lambdas-decision"></a>
#### 2.10.4 Decision 

Okay to use them for one-liners. If the code inside the lambda function is
longer than 60-80 chars, it's probably better to define it as a regular [nested
function](#lexical-scoping).

For common operations like multiplication, use the functions from the `operator`
module instead of lambda functions. For example, prefer `operator.mul` to
`lambda x, y: x * y`.

<a id="s2.11-conditional-expressions"></a>
<a id="211-conditional-expressions"></a>

<a id="conditional-expressions"></a>
### 2.11 Conditional Expressions 

Okay for simple cases.

<a id="s2.11.4-decision"></a>
<a id="2114-decision"></a>

<a id="conditional-expressions-decision"></a>
#### 2.11.4 Decision 

Okay to use for simple cases. Each portion must fit on one line:
true-expression, if-expression, else-expression. Use a complete if statement
when things get more complicated.

```python
one_line = 'yes' if predicate(value) else 'no'
slightly_split = ('yes' if predicate(value)
                  else 'no, nein, nyet')
the_longest_ternary_style_that_can_be_done = (
    'yes, true, affirmative, confirmed, correct'
    if predicate(value)
    else 'no, false, negative, nay')
```

```python
bad_line_breaking = ('yes' if predicate(value) else
                     'no')
portion_too_long = ('yes'
                    if some_long_module.some_long_predicate_function(
                        really_long_variable_name)
                    else 'no, false, negative, nay')
```

<a id="s2.12-default-argument-values"></a>
<a id="212-default-argument-values"></a>

<a id="default-arguments"></a>
### 2.12 Default Argument Values 

Okay in most cases.

<a id="s2.12.4-decision"></a>
<a id="2124-decision"></a>

<a id="default-arguments-decision"></a>
#### 2.12.4 Decision 

Okay to use with the following caveat:

Do not use mutable objects as default values in the function or method
definition.

```python
Yes: def foo(a, b=None):
         if b is None:
             b = []
Yes: def foo(a, b: Optional[Sequence] = None):
         if b is None:
             b = []
Yes: def foo(a, b: Sequence = ()):  # Empty tuple OK since tuples are immutable
         ...
```

```python
No:  def foo(a, b=[]):
         ...
No:  def foo(a, b=time.time()):  # The time the module was loaded???
         ...
No:  def foo(a, b=FLAGS.my_thing):  # sys.argv has not yet been parsed...
         ...
No:  def foo(a, b: Mapping = {}):  # Could still get passed to unchecked code
         ...
```

<a id="s2.14-truefalse-evaluations"></a>
<a id="214-truefalse-evaluations"></a>

<a id="truefalse-evaluations"></a>
### 2.14 True/False Evaluations 

Use the "implicit" false if at all possible.

<a id="s2.14.4-decision"></a>
<a id="2144-decision"></a>

<a id="truefalse-evaluations-decision"></a>
#### 2.14.4 Decision 

Use the "implicit" false if possible, e.g., `if foo:` rather than `if foo !=
[]:`. There are a few caveats that you should keep in mind though:

-   Always use `if foo is None:` (or `is not None`) to check for a `None`
    value-e.g., when testing whether a variable or argument that defaults to
    `None` was set to some other value. The other value might be a value that's
    false in a boolean context!

-   Never compare a boolean variable to `False` using `==`. Use `if not x:`
    instead. If you need to distinguish `False` from `None` then chain the
    expressions, such as `if not x and x is not None:`.

-   For sequences (strings, lists, tuples), use the fact that empty sequences
    are false, so `if seq:` and `if not seq:` are preferable to `if len(seq):`
    and `if not len(seq):` respectively.

-   When handling integers, implicit false may involve more risk than benefit
    (i.e., accidentally handling `None` as 0). You may compare a value which is
    known to be an integer (and is not the result of `len()`) against the
    integer 0.

    ```python
    Yes: if not users:
             print('no users')

         if foo == 0:
             self.handle_zero()

         if i % 10 == 0:
             self.handle_multiple_of_ten()

         def f(x=None):
             if x is None:
                 x = []
    ```

    ```python
    No:  if len(users) == 0:
             print('no users')

         if foo is not None and not foo:
             self.handle_zero()

         if not i % 10:
             self.handle_multiple_of_ten()

         def f(x=None):
             x = x or []
    ```

-   Note that `'0'` (i.e., `0` as string) evaluates to true.

<a id="s2.15-deprecated-language-features"></a>
<a id="215-deprecated-language-features"></a>

<a id="deprecated-features"></a>
### 2.15 Deprecated Language Features 

> don't

Use string methods instead of the `string` module where possible. Use function
call syntax instead of `apply`. Use list comprehensions and `for` loops instead
of `filter` and `map` when the function argument would have been an inlined
lambda anyway. Use `for` loops instead of `reduce`.

<a id="s2.15.2-decision"></a>
<a id="2152-decision"></a>

<a id="deprecated-features-decision"></a>
#### 2.15.2 Decision 

We do not use any Python version which does not support these features, so there
is no reason not to use the new styles.

```python
Yes: words = foo.split(':')

     [x[1] for x in my_list if x[2] == 5]

     map(math.sqrt, data)    # Ok. No inlined lambda expression.

     fn(*args, **kwargs)
```

```python
No:  words = string.split(foo, ':')

     map(lambda x: x[1], filter(lambda x: x[2] == 5, my_list))

     apply(fn, args, kwargs)
```

<a name="s2.21-typed-code"></a>
<a name="221-type-annotated-code"></a>
<a name="typed-code"></a>

<a id="typed-code"></a>
### 2.21 Type Annotated Code 

> Must

You can annotate Python 3 code with type hints according to
[PEP-484](https://www.python.org/dev/peps/pep-0484/), and type-check the code at
build time with a type checking tool like
[pytype](https://github.com/google/pytype).


Type annotations can be in the source or in a [stub pyi
file](https://www.python.org/dev/peps/pep-0484/#stub-files). Whenever possible,
annotations should be in the source. Use pyi files for third-party or extension
modules.


<a id="s2.21.1-definition"></a>
<a id="2211-definition"></a>

<a id="typed-code-definition"></a>
#### 2.21.1 Definition 

Type annotations (or "type hints") are for function or method arguments and
return values:

```python
def func(a: int) -> List[int]:
```

You can also declare the type of a variable using a special comment:

```python
a = SomeFunc()  # type: SomeType
```

<a id="s2.21.4-decision"></a>
<a id="2214-decision"></a>

<a id="typed-code-decision"></a>
#### 2.21.4 Decision 

You are strongly encouraged to enable Python type analysis when updating code.
When adding or modifying public APIs, include type annotations and enable
checking via pytype in the build system. As static analysis is relatively new to
Python, we acknowledge that undesired side-effects (such as
wrongly
inferred types) may prevent adoption by some projects. In those situations,
authors are encouraged to add a comment with a TODO or link to a bug describing
the issue(s) currently preventing type annotation adoption in the BUILD file or
in the code itself as appropriate.

<a id="s3-python-style-rules"></a>
<a id="3-python-style-rules"></a>

<a id="python-style-rules"></a>
## 3 Python Style Rules 

<a id="s3.1-semicolons"></a>
<a id="31-semicolons"></a>

<a id="semicolons"></a>
### 3.1 Semicolons 

> don't

Do not terminate your lines with semicolons, and do not use semicolons to put
two statements on the same line.

<a id="s3.2-line-length"></a>
<a id="32-line-length"></a>

<a id="line-length"></a>
### 3.2 Line length 

> just keep it clean

Maximum line length is *80 characters*.

Explicit exceptions to the 80 character limit:

-   Long import statements.
-   URLs, pathnames, or long flags in comments.
-   Long string module level constants not containing whitespace that would be
    inconvenient to split across lines such as URLs or pathnames.
-   Pylint disable comments. (e.g.: `# pylint: disable=invalid-name`)

Do not use backslash line continuation except for `with` statements requiring
three or more context managers.

Make use of Python's [implicit line joining inside parentheses, brackets and
braces](http://docs.python.org/reference/lexical_analysis.html#implicit-line-joining).
If necessary, you can add an extra pair of parentheses around an expression.

```python
Yes: foo_bar(self, width, height, color='black', design=None, x='foo',
             emphasis=None, highlight=0)

     if (width == 0 and height == 0 and
         color == 'red' and emphasis == 'strong'):
```

When a literal string won't fit on a single line, use parentheses for implicit
line joining.

```python
x = ('This will build a very long long '
     'long long long long long long string')
```

Within comments, put long URLs on their own line if necessary.

```python
Yes:  # See details at
      # http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
```

```python
No:  # See details at
     # http://www.example.com/us/developer/documentation/api/content/\
     # v2.0/csv_file_name_extension_full_specification.html
```

It is permissible to use backslash continuation when defining a `with` statement
whose expressions span three or more lines. For two lines of expressions, use a
nested `with` statement:

```python
Yes:  with very_long_first_expression_function() as spam, \
           very_long_second_expression_function() as beans, \
           third_thing() as eggs:
          place_order(eggs, beans, spam, beans)
```

```python
No:  with VeryLongFirstExpressionFunction() as spam, \
          VeryLongSecondExpressionFunction() as beans:
       PlaceOrder(eggs, beans, spam, beans)
```

```python
Yes:  with very_long_first_expression_function() as spam:
          with very_long_second_expression_function() as beans:
              place_order(beans, spam)
```

Make note of the indentation of the elements in the line continuation examples
above; see the [indentation](#s3.4-indentation) section for explanation.

In all other cases where a line exceeds 80 characters, and the
[yapf](https://github.com/google/yapf/)
auto-formatter does not help bring the line below the limit, the line is allowed
to exceed this maximum.

<a id="s3.3-parentheses"></a>
<a id="33-parentheses"></a>

<a id="parentheses"></a>
### 3.3 Parentheses 

Use parentheses sparingly.

It is fine, though not required, to use parentheses around tuples. Do not use
them in return statements or conditional statements unless using parentheses for
implied line continuation or to indicate a tuple.

```python
Yes: if foo:
         bar()
     while x:
         x = bar()
     if x and y:
         bar()
     if not x:
         bar()
     # For a 1 item tuple the ()s are more visually obvious than the comma.
     onesie = (foo,)
     return foo
     return spam, beans
     return (spam, beans)
     for (x, y) in dict.items(): ...
```

```python
No:  if (x):
         bar()
     if not(x):
         bar()
     return (foo)
```

<a id="s3.4-indentation"></a>
<a id="34-indentation"></a>

<a id="indentation"></a>
### 3.4 Indentation 

> Use tabs

<a id="s3.4.1-trailing_comma"></a>
<a id="341-trailing_comma"></a>
<a id="trailing_comma"></a>

<a id="trailing-comma"></a>
### 3.4.1 Trailing commas in sequences of items? 

Trailing commas in sequences of items are recommended only when the closing
container token `]`, `)`, or `}` does not appear on the same line as the final
element. The presence of a trailing comma is also used as a hint to our Python
code auto-formatter [YAPF](https://pypi.org/project/yapf/) to direct it to auto-format the container
of items to one item per line when the `,` after the final element is present.

```python
Yes:   golomb3 = [0, 1, 3]
Yes:   golomb4 = [
           0,
           1,
           4,
           6,
       ]
```

```python
No:    golomb4 = [
           0,
           1,
           4,
           6
       ]
```

<a id="s3.5-blank-lines"></a>
<a id="35-blank-lines"></a>

<a id="blank-lines"></a>
### 3.5 Blank Lines 

Two blank lines between top-level definitions, be they function or class
definitions. One blank line between method definitions and between the `class`
line and the first method. No blank line following a `def` line. Use single
blank lines as you judge appropriate within functions or methods.

<a id="s3.6-whitespace"></a>
<a id="36-whitespace"></a>

<a id="whitespace"></a>
### 3.6 Whitespace 

Follow standard typographic rules for the use of spaces around punctuation.

No whitespace inside parentheses, brackets or braces.

```python
Yes: spam(ham[1], {eggs: 2}, [])
```

```python
No:  spam( ham[ 1 ], { eggs: 2 }, [ ] )
```

No whitespace before a comma, semicolon, or colon. Do use whitespace after a
comma, semicolon, or colon, except at the end of the line.

```python
Yes: if x == 4:
         print(x, y)
     x, y = y, x
```

```python
No:  if x == 4 :
         print(x , y)
     x , y = y , x
```

No whitespace before the open paren/bracket that starts an argument list,
indexing or slicing.

```python
Yes: spam(1)
```

```python
No:  spam (1)
```


```python
Yes: dict['key'] = list[index]
```

```python
No:  dict ['key'] = list [index]
```

No trailing whitespace.

Surround binary operators with a single space on either side for assignment
(`=`), comparisons (`==, <, >, !=, <>, <=, >=, in, not in, is, is not`), and
Booleans (`and, or, not`). Use your better judgment for the insertion of spaces
around arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`, `@`).

```python
Yes: x == 1
```

```python
No:  x<1
```

Never use spaces around `=` when passing keyword arguments or defining a default
parameter value, with one exception: [when a type annotation is
present](#typing-default-values), _do_ use spaces around the `=` for the default
parameter value.

```python
Yes: def complex(real, imag=0.0): return Magic(r=real, i=imag)
Yes: def complex(real, imag: float = 0.0): return Magic(r=real, i=imag)
```

```python
No:  def complex(real, imag = 0.0): return Magic(r = real, i = imag)
No:  def complex(real, imag: float=0.0): return Magic(r = real, i = imag)
```

Don't use spaces to vertically align tokens on consecutive lines, since it
becomes a maintenance burden (applies to `:`, `#`, `=`, etc.):

```python
Yes:
  foo = 1000  # comment
  long_name = 2  # comment that should not be aligned

  dictionary = {
      'foo': 1,
      'long_name': 2,
  }
```

```python
No:
  foo       = 1000  # comment
  long_name = 2     # comment that should not be aligned

  dictionary = {
      'foo'      : 1,
      'long_name': 2,
  }
```


<a id="Python_Interpreter"></a>
<a id="s3.7-shebang-line"></a>
<a id="37-shebang-line"></a>

<a id="shebang-line"></a>
### 3.7 Shebang Line 

> don't

Most `.py` files do not need to start with a `#!` line. Start the main file of a
program with
`#!/usr/bin/python` with an optional single digit `2` or `3` suffix per
[PEP-394](https://www.google.com/url?sa=D&q=http://www.python.org/dev/peps/pep-0394/).

This line is used by the kernel to find the Python interpreter, but is ignored
by Python when importing modules. It is only necessary on a file that will be
executed directly.

<a id="s3.8-comments"></a>
<a id="38-comments-and-docstrings"></a>

<a id="documentation"></a>
### 3.8 Comments and Docstrings 

> the code itself should be a doc

Be sure to use the right style for module, function, method docstrings and
inline comments.

<a id="s3.8.1-comments-in-doc-strings"></a>
<a id="381-docstrings"></a>
<a id="comments-in-doc-strings"></a>

<a id="docstrings"></a>
#### 3.8.1 Docstrings 

Python uses _docstrings_ to document code. A docstring is a string that is the
first statement in a package, module, class or function. These strings can be
extracted automatically through the `__doc__` member of the object and are used
by `pydoc`.
(Try running `pydoc` on your module to see how it looks.) Always use the three
double-quote `"""` format for docstrings (per [PEP
257](https://www.google.com/url?sa=D&q=http://www.python.org/dev/peps/pep-0257/)).
A docstring should be organized as a summary line (one physical line) terminated
by a period, question mark, or exclamation point, followed by a blank line,
followed by the rest of the docstring starting at the same cursor position as
the first quote of the first line. There are more formatting guidelines for
docstrings below.

<a id="s3.8.2-comments-in-modules"></a>
<a id="382-modules"></a>
<a id="comments-in-modules"></a>

<a id="module-docs"></a>
#### 3.8.2 Modules 

Every file should contain license boilerplate.
Choose the appropriate boilerplate for the license used by the project (for
example, Apache 2.0, BSD, LGPL, GPL)

Files should start with a docstring describing the contents and usage of the
module.
```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```


<a id="s3.8.3-functions-and-methods"></a>
<a id="383-functions-and-methods"></a>
<a id="functions-and-methods"></a>

<a id="function-docs"></a>
#### 3.8.3 Functions and Methods 

In this section, "function" means a method, function, or generator.

A function must have a docstring, unless it meets all of the following criteria:

-   not externally visible
-   very short
-   obvious

A docstring should give enough information to write a call to the function
without reading the function's code. The docstring should be descriptive-style
(`"""Fetches rows from a Bigtable."""`) rather than imperative-style (`"""Fetch
rows from a Bigtable."""`), except for `@property` data descriptors, which
should use the <a href="#384-classes">same style as attributes</a>. A docstring
should describe the function's calling syntax and its semantics, not its
implementation. For tricky code, comments alongside the code are more
appropriate than using docstrings.

A method that overrides a method from a base class may have a simple docstring
sending the reader to its overridden method's docstring, such as `"""See base
class."""`. The rationale is that there is no need to repeat in many places
documentation that is already present in the base method's docstring. However,
if the overriding method's behavior is substantially different from the
overridden method, or details need to be provided (e.g., documenting additional
side effects), a docstring with at least those differences is required on the
overriding method.

Certain aspects of a function should be documented in special sections, listed
below. Each section begins with a heading line, which ends with a colon. All
sections other than the heading should maintain a hanging indent of two or four
spaces (be consistent within a file). These sections can be omitted in cases
where the function's name and signature are informative enough that it can be
aptly described using a one-line docstring.

<a id="doc-function-args"></a>
[*Args:*](#doc-function-args)
:   List each parameter by name. A description should follow the name, and be
    separated by a colon and a space. If the description is too long to fit on a
    single 80-character line, use a hanging indent of 2 or 4 spaces (be
    consistent with the rest of the file).

    The description should include required type(s) if the code does not contain
    a corresponding type annotation. If a function accepts `*foo` (variable
    length argument lists) and/or `**bar` (arbitrary keyword arguments), they
    should be listed as `*foo` and `**bar`.

<a id="doc-function-returns"></a>
[*Returns:* (or *Yields:* for generators)](#doc-function-returns)
:   Describe the type and semantics of the return value. If the function only
    returns None, this section is not required. It may also be omitted if the
    docstring starts with Returns or Yields (e.g. `"""Returns row from Bigtable
    as a tuple of strings."""`) and the opening sentence is sufficient to
    describe return value.

<a id="doc-function-raises"></a>
[*Raises:*](#doc-function-raises)
:   List all exceptions that are relevant to the interface. You should not
    document exceptions that get raised if the API specified in the docstring is
    violated (because this would paradoxically make behavior under violation of
    the API part of the API).

```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
```

<a id="s3.8.4-comments-in-classes"></a>
<a id="384-classes"></a>
<a id="comments-in-classes"></a>

<a id="class-docs"></a>
#### 3.8.4 Classes 

Classes should have a docstring below the class definition describing the class.
If your class has public attributes, they should be documented here in an
`Attributes` section and follow the same formatting as a
[function's `Args`](#doc-function-args) section.

```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```

<a id="comments-in-block-and-inline"></a>
<a id="s3.8.5-comments-in-block-and-inline"></a>
<a id="385-block-and-inline-comments"></a>

<a id="comments"></a>
#### 3.8.5 Block and Inline Comments 

The final place to have comments is in tricky parts of the code. If you're going
to have to explain it at the next [code
review](http://en.wikipedia.org/wiki/Code_review), you should comment it
now. Complicated operations get a few lines of comments before the operations
commence. Non-obvious ones get comments at the end of the line.

```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

if i & (i-1) == 0:  # True if i is 0 or a power of 2.
```

To improve legibility, these comments should start at least 2 spaces away from
the code with the comment character `#`, followed by at least one space before
the text of the comment itself.

On the other hand, never describe the code. Assume the person reading the code
knows Python (though not what you're trying to do) better than you do.

```python
# BAD COMMENT: Now go through the b array and make sure whenever i occurs
# the next element is i+1
```

<!-- The next section is copied from the C++ style guide. -->

<a id="s3.8.6-punctuation-spelling-and-grammar"></a>
<a id="386-punctuation-spelling-and-grammar"></a>
<a id="spelling"></a>
<a id="punctuation"></a>
<a id="grammar"></a>

<a id="punctuation-spelling-grammar"></a>
#### 3.8.6 Punctuation, Spelling, and Grammar 

Pay attention to punctuation, spelling, and grammar; it is easier to read
well-written comments than badly written ones.

Comments should be as readable as narrative text, with proper capitalization and
punctuation. In many cases, complete sentences are more readable than sentence
fragments. Shorter comments, such as comments at the end of a line of code, can
sometimes be less formal, but you should be consistent with your style.

Although it can be frustrating to have a code reviewer point out that you are
using a comma when you should be using a semicolon, it is very important that
source code maintain a high level of clarity and readability. Proper
punctuation, spelling, and grammar help with that goal.

<a id="s3.9-classes"></a>
<a id="39-classes"></a>

<a id="classes"></a>
### 3.9 Classes 

> inherit `object`

If a class inherits from no other base classes, explicitly inherit from
`object`. This also applies to nested classes.

```python
Yes: class SampleClass(object):
         pass


     class OuterClass(object):

         class InnerClass(object):
             pass


     class ChildClass(ParentClass):
         """Explicitly inherits from another class already."""

```

```python
No: class SampleClass:
        pass


    class OuterClass:

        class InnerClass:
            pass
```

Inheriting from `object` is needed to make properties work properly in Python 2
and can protect your code from potential incompatibility with Python 3. It also
defines special methods that implement the default semantics of objects
including `__new__`, `__init__`, `__delattr__`, `__getattribute__`,
`__setattr__`, `__hash__`, `__repr__`, and `__str__`.

<a id="s3.10-strings"></a>
<a id="310-strings"></a>

<a id="strings"></a>
### 3.10 Strings 

> use `.format()` strings

Use the `format` method or the `%` operator for formatting strings, even when
the parameters are all strings. Use your best judgment to decide between `+` and
`%` (or `format`) though.

```python
Yes: x = a + b
     x = '%s, %s!' % (imperative, expletive)
     x = '{}, {}'.format(first, second)
     x = 'name: %s; score: %d' % (name, n)
     x = 'name: {}; score: {}'.format(name, n)
     x = f'name: {name}; score: {n}'  # Python 3.6+
```

```python
No: x = '%s%s' % (a, b)  # use + in this case
    x = '{}{}'.format(a, b)  # use + in this case
    x = first + ', ' + second
    x = 'name: ' + name + '; score: ' + str(n)
```

Avoid using the `+` and `+=` operators to accumulate a string within a loop.
Since strings are immutable, this creates unnecessary temporary objects and
results in quadratic rather than linear running time. Instead, add each
substring to a list and `''.join` the list after the loop terminates (or, write
each substring to a `io.BytesIO` buffer).

```python
Yes: items = ['<table>']
     for last_name, first_name in employee_list:
         items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
     items.append('</table>')
     employee_table = ''.join(items)
```

```python
No: employee_table = '<table>'
    for last_name, first_name in employee_list:
        employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
    employee_table += '</table>'
```

Be consistent with your choice of string quote character within a file. Pick `'`
or `"` and stick with it. It is okay to use the other quote character on a
string to avoid the need to `\\ ` escape within the string.

```python
Yes:
  Python('Why are you hiding your eyes?')
  Gollum("I'm scared of lint errors.")
  Narrator('"Good!" thought a happy Python reviewer.')
```

```python
No:
  Python("Why are you hiding your eyes?")
  Gollum('The lint. It burns. It burns us.')
  Gollum("Always the great lint. Watching. Watching.")
```

Prefer `"""` for multi-line strings rather than `'''`. Projects may choose to
use `'''` for all non-docstring multi-line strings if and only if they also use
`'` for regular strings. Docstrings must use `"""` regardless.

Multi-line strings do not flow with the indentation of the rest of the program.
If you need to avoid embedding extra space in the string, use either
concatenated single-line strings or a multi-line string with
[`textwrap.dedent()`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)
to remove the initial space on each line:

```python
  No:
  long_string = """This is pretty ugly.
Don't do this.
"""
```

```python
  Yes:
  long_string = """This is fine if your use case can accept
      extraneous leading spaces."""
```

```python
  Yes:
  long_string = ("And this is fine if you can not accept\n" +
                 "extraneous leading spaces.")
```

```python
  Yes:
  long_string = ("And this too is fine if you can not accept\n"
                 "extraneous leading spaces.")
```

```python
  Yes:
  import textwrap

  long_string = textwrap.dedent("""\
      This is also fine, because textwrap.dedent()
      will collapse common leading spaces in each line.""")
```

<a id="s3.11-files-and-sockets"></a>
<a id="311-files-and-sockets"></a>
<a id="files-and-sockets"></a>

<a id="files"></a>
### 3.11 Files and Sockets 

> close them

Explicitly close files and sockets when done with them.

Leaving files, sockets or other file-like objects open unnecessarily has many
downsides:

-   They may consume limited system resources, such as file descriptors. Code
    that deals with many such objects may exhaust those resources unnecessarily
    if they're not returned to the system promptly after use.
-   Holding files open may prevent other actions such as moving or deleting
    them.
-   Files and sockets that are shared throughout a program may inadvertently be
    read from or written to after logically being closed. If they are actually
    closed, attempts to read or write from them will throw exceptions, making
    the problem known sooner.

Furthermore, while files and sockets are automatically closed when the file
object is destructed, tying the lifetime of the file object to the state of the
file is poor practice:

-   There are no guarantees as to when the runtime will actually run the file's
    destructor. Different Python implementations use different memory management
    techniques, such as delayed Garbage Collection, which may increase the
    object's lifetime arbitrarily and indefinitely.
-   Unexpected references to the file, e.g. in globals or exception tracebacks,
    may keep it around longer than intended.

The preferred way to manage files is using the ["with"
statement](http://docs.python.org/reference/compound_stmts.html#the-with-statement):

```python
with open("hello.txt") as hello_file:
    for line in hello_file:
        print(line)
```

For file-like objects that do not support the "with" statement, use
`contextlib.closing()`:

```python
import contextlib

with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
    for line in front_page:
        print(line)
```

<a id="s3.12-todo-comments"></a>
<a id="312-todo-comments"></a>

<a id="todo"></a>
### 3.12 TODO Comments 

Use `TODO` comments for code that is temporary, a short-term solution, or
good-enough but not perfect.

A `TODO` comment begins with the string `TODO` in all caps and a parenthesized
name, e-mail address, or other identifier
of the person or issue with the best context about the problem. This is followed
by an explanation of what there is to do.

The purpose is to have a consistent `TODO` format that can be searched to find
out how to get more details. A `TODO` is not a commitment that the person
referenced will fix the problem. Thus when you create a
`TODO`, it is almost always your name
that is given.

```python
# TODO(kl@gmail.com): Use a "*" here for string repetition.
# TODO(Zeke) Change this to use relations.
```

If your `TODO` is of the form "At a future date do something" make sure that you
either include a very specific date ("Fix by November 2009") or a very specific
event ("Remove this code when all clients can handle XML responses.").

<a id="s3.13-imports-formatting"></a>
<a id="313-imports-formatting"></a>

<a id="imports-formatting"></a>
### 3.13 Imports formatting 

Imports should be on separate lines.

E.g.:

```python
Yes: import os
     import sys
```

```python
No:  import os, sys
```


Imports are always put at the top of the file, just after any module comments
and docstrings and before module globals and constants. Imports should be
grouped from most generic to least generic:

1.  Python future import statements. For example:

    ```python
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    ```

    See [above](#from-future-imports) for more information about those.

2.  Python standard library imports. For example:

    ```python
    import sys
    ```

3.  [third-party](https://pypi.org/) module
    or package imports. For example:

    
    ```python
    import tensorflow as tf
    ```

4.  Code repository
    sub-package imports. For example:

    
    ```python
    from otherproject.ai import mind
    ```

5.  **Deprecated:** application-specific imports that are part of the same
    top level
    sub-package as this file. For example:

    
    ```python
    from myproject.backend.hgwells import time_machine
    ```

    You may find older Google Python Style code doing this, but it is no longer
    required. **New code is encouraged not to bother with this.** Simply treat
    application-specific sub-package imports the same as other sub-package
    imports.

    
Within each grouping, imports should be sorted lexicographically, ignoring case,
according to each module's full package path. Code may optionally place a blank
line between import sections.

```python
import collections
import queue
import sys

from absl import app
from absl import flags
import bs4
import cryptography
import tensorflow as tf

from book.genres import scifi
from myproject.backend.hgwells import time_machine
from myproject.backend.state_machine import main_loop
from otherproject.ai import body
from otherproject.ai import mind
from otherproject.ai import soul

# Older style code may have these imports down here instead:
#from myproject.backend.hgwells import time_machine
#from myproject.backend.state_machine import main_loop
```


<a id="s3.14-statements"></a>
<a id="314-statements"></a>

<a id="statements"></a>
### 3.14 Statements 

Generally only one statement per line.

However, you may put the result of a test on the same line as the test only if
the entire statement fits on one line. In particular, you can never do so with
`try`/`except` since the `try` and `except` can't both fit on the same line, and
you can only do so with an `if` if there is no `else`.

```python
Yes:

  if foo: bar(foo)
```

```python
No:

  if foo: bar(foo)
  else:   baz(foo)

  try:               bar(foo)
  except ValueError: baz(foo)

  try:
      bar(foo)
  except ValueError: baz(foo)
```

<a id="s3.15-access-control"></a>
<a id="315-access-control"></a>
<a id="access-control"></a>

<a id="accessors"></a>
### 3.15 Accessors 

If an accessor function would be trivial, you should use public variables
instead of accessor functions to avoid the extra cost of function calls in
Python. When more functionality is added you can use `property` to keep the
syntax consistent.

On the other hand, if access is more complex, or the cost of accessing the
variable is significant, you should use function calls (following the
[Naming](#s3.16-naming) guidelines) such as `get_foo()` and
`set_foo()`. If the past behavior allowed access through a property, do not
bind the new accessor functions to the property. Any code still attempting to
access the variable by the old method should break visibly so they are made
aware of the change in complexity.

<a id="s3.16-naming"></a>
<a id="316-naming"></a>

<a id="naming"></a>
### 3.16 Naming 

`module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`,
`function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`,
`function_parameter_name`, `local_var_name`.


Function names, variable names, and filenames should be descriptive; eschew
abbreviation. In particular, do not use abbreviations that are ambiguous or
unfamiliar to readers outside your project, and do not abbreviate by deleting
letters within a word.

Always use a `.py` filename extension. Never use dashes.

<a id="s3.16.1-names-to-avoid"></a>
<a id="3161-names-to-avoid"></a>

<a id="names-to-avoid"></a>
#### 3.16.1 Names to Avoid 

-   single character names except for counters or iterators. You may use "e" as
    an exception identifier in try/except statements.
-   dashes (`-`) in any package/module name
-   `__double_leading_and_trailing_underscore__` names (reserved by Python)

<a id="s3.16.2-naming-conventions"></a>
<a id="3162-naming-convention"></a>

<a id="naming-conventions"></a>
#### 3.16.2 Naming Conventions 

-   "Internal" means internal to a module, or protected or private within a
    class.

-   Prepending a single underscore (`_`) has some support for protecting module
    variables and functions (not included with `from module import *`). While
    prepending a double underscore (`__` aka "dunder") to an instance variable
    or method effectively makes the variable or method private to its class
    (using name mangling) we discourage its use as it impacts readability and
    testability and isn't *really* private.

-   Place related classes and top-level functions together in a
    module.
    Unlike Java, there is no need to limit yourself to one class per module.

-   Use CapWords for class names, but lower\_with\_under.py for module names.
    Although there are some old modules named CapWords.py, this is now
    discouraged because it's confusing when the module happens to be named after
    a class. ("wait -- did I write `import StringIO` or `from StringIO import
    StringIO`?")

-   Underscores may appear in *unittest* method names starting with `test` to
    separate logical components of the name, even if those components use
    CapWords. One possible pattern is `test<MethodUnderTest>_<state>`; for
    example `testPop_EmptyStack` is okay. There is no One Correct Way to name
    test methods.

<a id="s3.16.3-file-naming"></a>
<a id="3163-file-naming"></a>

<a id="file-naming"></a>
#### 3.16.3 File Naming 

Python filenames must have a `.py` extension and must not contain dashes (`-`).
This allows them to be imported and unittested. If you want an executable to be
accessible without the extension, use a symbolic link or a simple bash wrapper
containing `exec "$0.py" "$@"`.

<a id="s3.16.4-guidelines-derived-from-guidos-recommendations"></a>
<a id="3164-guidelines-derived-from-guidos-recommendations"></a>

<a id="guidelines-derived-from-guidos-recommendations"></a>
#### 3.16.4 Guidelines derived from Guido's Recommendations 

<table rules="all" border="1" summary="Guidelines from Guido's Recommendations"
       cellspacing="2" cellpadding="2">

  <tr>
    <th>Type</th>
    <th>Public</th>
    <th>Internal</th>
  </tr>

  <tr>
    <td>Packages</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Modules</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code></td>
  </tr>

  <tr>
    <td>Classes</td>
    <td><code>CapWords</code></td>
    <td><code>_CapWords</code></td>
  </tr>

  <tr>
    <td>Exceptions</td>
    <td><code>CapWords</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Functions</td>
    <td><code>lower_with_under()</code></td>
    <td><code>_lower_with_under()</code></td>
  </tr>

  <tr>
    <td>Global/Class Constants</td>
    <td><code>CAPS_WITH_UNDER</code></td>
    <td><code>_CAPS_WITH_UNDER</code></td>
  </tr>

  <tr>
    <td>Global/Class Variables</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code></td>
  </tr>

  <tr>
    <td>Instance Variables</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code> (protected)</td>
  </tr>

  <tr>
    <td>Method Names</td>
    <td><code>lower_with_under()</code></td>
    <td><code>_lower_with_under()</code> (protected)</td>
  </tr>

  <tr>
    <td>Function/Method Parameters</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Local Variables</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

</table>

While Python supports making things private by using a leading double underscore
`__` (aka. "dunder") prefix on a name, this is discouraged. Prefer the use of a
single underscore. They are easier to type, read, and to access from small
unittests. Lint warnings take care of invalid access to protected members.


<a id="s3.17-main"></a>
<a id="317-main"></a>

<a id="main"></a>
### 3.17 Main 

> every .py needs `main`, and its execution code

Even a file meant to be used as an executable should be importable and a mere
import should not have the side effect of executing the program's main
functionality. The main functionality should be in a `main()` function.

In Python, `pydoc` as well as unit tests require modules to be importable. Your
code should always check `if __name__ == '__main__'` before executing your main
program so that the main program is not executed when the module is imported.

```python
def main():
    ...

if __name__ == '__main__':
    main()
```

All code at the top level will be executed when the module is imported. Be
careful not to call functions, create objects, or perform other operations that
should not be executed when the file is being `pydoc`ed.

<a id="s3.18-function-length"></a>
<a id="318-function-length"></a>

<a id="function-length"></a>
### 3.18 Function length 

Prefer small and focused functions.

We recognize that long functions are sometimes appropriate, so no hard limit is
placed on function length. If a function exceeds about 40 lines, think about
whether it can be broken up without harming the structure of the program.

Even if your long function works perfectly now, someone modifying it in a few
months may add new behavior. This could result in bugs that are hard to find.
Keeping your functions short and simple makes it easier for other people to read
and modify your code.

You could find long and complicated functions when working with
some code. Do not be intimidated by modifying existing code: if working with such
a function proves to be difficult, you find that errors are hard to debug, or
you want to use a piece of it in several different contexts, consider breaking
up the function into smaller and more manageable pieces.

<a id="s3.19-type-annotations"></a>
<a id="319-type-annotations"></a>

<a id="type-annotations"></a>
### 3.19 Type Annotations 

> Must

<a id="s3.19.1-general"></a>
<a id="3191-general-rules"></a>

<a id="typing-general"></a>
#### 3.19.1 General Rules 

* Familiarize yourself with [PEP-484](https://www.python.org/dev/peps/pep-0484/).
* In methods, only annotate `self`, or `cls` if it is necessary for proper type
  information. e.g., `@classmethod def create(cls: Type[T]) -> T: return cls()`
* If any other variable or a returned type should not be expressed, use `Any`.
* You are not required to annotate all the functions in a module.
  -   At least annotate your public APIs.
  -   Use judgment to get to a good balance between safety and clarity on the
      one hand, and flexibility on the other.
  -   Annotate code that is prone to type-related errors (previous bugs or
      complexity).
  -   Annotate code that is hard to understand.
  -   Annotate code as it becomes stable from a types perspective. In many
      cases, you can annotate all the functions in mature code without losing
      too much flexibility.


<a id="s3.19.2-line-breaking"></a>
<a id="3192-line-breaking"></a>

<a id="typing-line-breaking"></a>
#### 3.19.2 Line Breaking 

Try to follow the existing [indentation](#indentation) rules.

After annotating, many function signatures will become "one parameter per line".

```python
def my_method(self,
              first_var: int,
              second_var: Foo,
              third_var: Optional[Bar]) -> int:
  ...
```

Always prefer breaking between variables, and not for example between variable
names and type annotations. However, if everything fits on the same line,
go for it.

```python
def my_method(self, first_var: int) -> int:
  ...
```

If the combination of the function name, the last parameter, and the return type
is too long, indent by 4 in a new line.

```python
def my_method(
    self, first_var: int) -> Tuple[MyLongType1, MyLongType1]:
  ...
```

When the return type does not fit on the same line as the last parameter, the
preferred way is to indent the parameters by 4 on a new line and align the
closing parenthesis with the def.

```python
Yes:
def my_method(
    self, other_arg: Optional[MyLongType]
) -> Dict[OtherLongType, MyLongType]:
  ...
```

`pylint` allows you to move the closing parenthesis to a new line and align
with the opening one, but this is less readable.

```python
No:
def my_method(self,
              other_arg: Optional[MyLongType]
             ) -> Dict[OtherLongType, MyLongType]:
  ...
```

As in the examples above, prefer not to break types. However, sometimes they are
too long to be on a single line (try to keep sub-types unbroken).

```python
def my_method(
    self,
    first_var: Tuple[List[MyLongType1],
                     List[MyLongType2]],
    second_var: List[Dict[
        MyLongType3, MyLongType4]]) -> None:
  ...
```

If a single name and type is too long, consider using an
[alias](#typing-aliases) for the type. The last resort is to break after the
colon and indent by 4.

```python
Yes:
def my_function(
    long_variable_name:
        long_module_name.LongTypeName,
) -> None:
  ...
```

```python
No:
def my_function(
    long_variable_name: long_module_name.
        LongTypeName,
) -> None:
  ...
```

<a id="s3.19.3-forward-declarations"></a>
<a id="3193-forward-declarations"></a>

<a id="forward-declarations"></a>
#### 3.19.3 Forward Declarations 

If you need to use a class name from the same module that is not yet defined --
for example, if you need the class inside the class declaration, or if you use a
class that is defined below -- use a string for the class name.

```python
class MyClass(object):

  def __init__(self,
               stack: List["MyClass"]) -> None:
```

<a id="s3.19.4-default-values"></a>
<a id="3194-default-values"></a>

<a id="typing-default-values"></a>
#### 3.19.4 Default Values 

As per
[PEP-008](https://www.python.org/dev/peps/pep-0008/#other-recommendations), use
spaces around the `=` _only_ for arguments that have both a type annotation and
a default value.

```python
Yes:
def func(a: int = 0) -> int:
  ...
```
```python
No:
def func(a:int=0) -> int:
  ...
```

<a id="s3.19.5-none-type"></a>
<a id="3195-nonetype"></a>

<a id="none-type"></a>
#### 3.19.5 NoneType 

In the Python type system, `NoneType` is a "first class" type, and for typing
purposes, `None` is an alias for `NoneType`. If an argument can be `None`, it
has to be declared! You can use `Union`, but if there is only one other type,
use `Optional`.

Use explicit `Optional` instead of implicit `Optional`. Earlier versions of PEP
484 allowed `a: Text = None` to be interpretted as `a: Optional[Text] = None`,
but that is no longer the preferred behavior.

```python
Yes:
def func(a: Optional[Text], b: Optional[Text] = None) -> Text:
  ...
def multiple_nullable_union(a: Union[None, Text, int]) -> Text
  ...
```

```python
No:
def nullable_union(a: Union[None, Text]) -> Text:
  ...
def implicit_optional(a: Text = None) -> Text:
  ...
```

<a id="s3.19.8-comments"></a>
<a id="3198-typing-internal-variables"></a>

<a id="typing-variables"></a>
#### 3.19.8 Typing Variables 

If an internal variable has a type that is hard or impossible to infer, you can
specify its type in a couple ways.

<a id="type-comments"></a>
[*Type Comments:*](#type-comments)
:   Use a `# type:` comment on the end of the line

```python
a = SomeUndecoratedFunction()  # type: Foo
```

[*Annotated Assignments*](#annotated-assignments)
:   Use a colon and type between the variable name and value, as with function
    arguments.

```python
a: Foo = SomeUndecoratedFunction()
```

<a id="s3.19.9-tuples"></a>
<a id="3199-tuples-vs-lists"></a>

<a id="typing-tuples"></a>
#### 3.19.9 Tuples vs Lists 

Unlike Lists, which can only have a single type, Tuples can have either a single
repeated type or a set number of elements with different types. The latter is
commonly used as return type from a function.

```python
a = [1, 2, 3]  # type: List[int]
b = (1, 2, 3)  # type: Tuple[int, ...]
c = (1, "2", 3.5)  # type: Tuple[int, Text, float]
```

<a id="s3.19.11-strings"></a>
<a id="31911-string-types"></a>

<a id="typing-strings"></a>
#### 3.19.11 String types 

> use `str`

The proper type for annotating strings depends on what versions of Python the
code is intended for.

For Python 3 only code, prefer to use `str`. `Text` is also acceptable. Be
consistent in using one or the other.

For Python 2 compatible code, use `Text`. In some rare cases, `str` may make
sense; typically to aid compatibility when the return types aren't the same
between the two Python versions. Avoid using `unicode`: it doesn't exist in
Python 3.

The reason this discrepancy exists is because `str` means different things
depending on the Python version.

```python
No:
def py2_code(x: str) -> unicode:
  ...
```

For code that deals with binary data, use `bytes`.

```python
def deals_with_binary_data(x: bytes) -> bytes:
  ...
```

For Python 2 compatible code that processes text data (`str` or `unicode` in
Python 2, `str` in Python 3), use `Text`. For Python 3 only code that process
text data, prefer `str`.

```python
from typing import Text
...
def py2_compatible(x: Text) -> Text:
  ...
def py3_only(x: str) -> str:
  ...
```

If the type can be either bytes or text, use `Union`, with the appropriate text
type.

```python
from typing import Text, Union
...
def py2_compatible(x: Union[bytes, Text]) -> Union[bytes, Text]:
  ...
def py3_only(x: Union[bytes, str]) -> Union[bytes, str]:
  ...
```

If all the string types of a function are always the same, for example if the
return type is the same as the argument type in the code above, use
[AnyStr](#typing-type-var).

Writing it like this will simplify the process of porting the code to Python 3.

<a id="s3.19.13-conditional-imports"></a>
<a id="31913-conditional-imports"></a>

<a id="typing-conditional-imports"></a>
#### 3.19.13 Conditional Imports

> don't unless you are smart enough

Use conditional imports only in exceptional cases where the additional imports
needed for type checking must be avoided at runtime. This pattern is
discouraged; alternatives such as refactoring the code to allow top level
imports should be preferred.

Imports that are needed only for type annotations can be placed within an
`if TYPE_CHECKING:` block.

-   Conditionally imported types need to be referenced as strings, to be forward
    compatible with Python 3.6 where the annotation expressions are actually
    evaluated.
-   Only entities that are used solely for typing should be defined here; this
    includes aliases. Otherwise it will be a runtime error, as the module will
    not be imported at runtime.
-   The block should be right after all the normal imports.
-   There should be no empty lines in the typing imports list.
-   Sort this list as if it were a regular imports list.
```python
import typing
if typing.TYPE_CHECKING:
  import sketch
def f(x: "sketch.Sketch"): ...
```

<a id="s3.19.14-circular-deps"></a>
<a id="31914-circular-dependencies"></a>

<a id="typing-circular-deps"></a>
#### 3.19.14 Circular Dependencies 

> follow the architecture

Circular dependencies that are caused by typing are code smells. Such code is a
good candidate for refactoring. Although technically it is possible to keep
circular dependencies, the [build system](#typing-build-deps) will not let you
do so because each module has to depend on the other.

Replace modules that create circular dependency imports with `Any`. Set an
[alias](#typing-aliases) with a meaningful name, and use the real type name from
this module (any attribute of Any is Any). Alias definitions should be separated
from the last import by one line.

```python
from typing import Any

some_mod = Any  # some_mod.py imports this module.
...

def my_method(self, var: some_mod.SomeType) -> None:
  ...
```

<a id="typing-generics"></a>
<a id="s3.19.15-generics"></a>
<a id="31915-generics"></a>

<a id="generics"></a>
#### 3.19.15 Generics 

When annotating, prefer to specify type parameters for generic types; otherwise,
[the generics' parameters will be assumed to be `Any`](https://www.python.org/dev/peps/pep-0484/#the-any-type).

```python
def get_names(employee_ids: List[int]) -> Dict[int, Any]:
  ...
```

```python
# These are both interpreted as get_names(employee_ids: List[Any]) -> Dict[Any, Any]
def get_names(employee_ids: list) -> Dict:
  ...

def get_names(employee_ids: List) -> Dict:
  ...
```

If the best type parameter for a generic is `Any`, make it explicit, but
remember that in many cases [`TypeVar`](#typing-type-var) might be more
appropriate:

```python
def get_names(employee_ids: List[Any]) -> Dict[Any, Text]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```

```python
T = TypeVar('T')
def get_names(employee_ids: List[T]) -> Dict[T, Text]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```


<a id="4-parting-words"></a>

<a id="consistency"></a>
## 4 Parting Words 

*BE CONSISTENT*.

If you're editing code, take a few minutes to look at the code around you and
determine its style. If they use spaces around all their arithmetic operators,
you should too. If their comments have little boxes of hash marks around them,
make your comments have little boxes of hash marks around them too.

The point of having style guidelines is to have a common vocabulary of coding so
people can concentrate on what you're saying rather than on how you're saying
it. We present global style rules here so people know the vocabulary, but local
style is also important. If code you add to a file looks drastically different
from the existing code around it, it throws readers out of their rhythm when
they go to read it. Avoid this.


