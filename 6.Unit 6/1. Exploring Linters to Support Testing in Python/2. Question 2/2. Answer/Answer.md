Ensure pylint is in your virtual box -
    pip install pylint
Run pylint on pylintTest.py
Review each of the code errors returned.
Can you correct each of the errors identified by pylint? Before correcting the code errors, save the pylintTest.py file with a new name (it will be needed again in the next question).

---------------

Answer:
I received the following error
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

I fixed this error by adding parentheses on the print statment

---------------

Answer:
After fixing the error I received a second error saying
NameError: name 'raw_input' is not defined

In python3 raw_input does not exist anymore. I have replaced the function with input instead.
I have also removed the extra parentheses on this line of code

word = (raw_input("Please enter text"))

changed to

word = input("Please enter text")

---------------

Answer:
Next I received these errors from pylint

pylintTest.py:5:0: C0303: Trailing whitespace (trailing-whitespace)
pylintTest.py:12:0: W0311: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
pylintTest.py:13:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
pylintTest.py:14:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:15:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
pylintTest.py:16:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:17:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:18:0: W0311: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
pylintTest.py:19:0: W0311: Bad indentation. Found 6 spaces, expected 12 (bad-indentation)
pylintTest.py:20:0: W0311: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
pylintTest.py:21:0: W0311: Bad indentation. Found 12 spaces, expected 20 (bad-indentation)
pylintTest.py:22:0: W0311: Bad indentation. Found 8 spaces, expected 16 (bad-indentation)
pylintTest.py:23:0: W0311: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
pylintTest.py:24:0: W0311: Bad indentation. Found 10 spaces, expected 20 (bad-indentation)
pylintTest.py:26:0: C0304: Final newline missing (missing-final-newline)
pylintTest.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pylintTest.py:1:0: C0103: Module name "pylintTest" doesn't conform to snake_case naming style (invalid-name)
pylintTest.py:6:0: C0103: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:9:0: C0103: Constant name "letters" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:10:0: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:14:6: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:16:6: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:17:6: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:21:12: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:23:10: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:24:10: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)

I fixed most of them by using Black formater

---------------

Answer:
This what was left

pylintTest.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pylintTest.py:1:0: C0103: Module name "pylintTest" doesn't conform to snake_case naming style (invalid-name)
pylintTest.py:5:0: C0103: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:8:0: C0103: Constant name "letters" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:9:0: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:13:12: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:15:12: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:16:12: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:20:20: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:22:20: C0103: Constant name "x" doesn't conform to UPPER_CASE naming style (invalid-name)
pylintTest.py:23:20: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)

Solutions:
adding a docstring fixes the first error.
renaming the file to pylint_test fixes this issue
making shift upper case fixes this issue
making letters upper case fixes this issue
making encoded upper case fixes this issue
making x upper case fixes this issue

---------------

Answer:
After I made all of these changes the code now works perfectly and pylint reports everything is good