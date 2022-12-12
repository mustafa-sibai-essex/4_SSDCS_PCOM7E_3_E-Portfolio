4. Testing with Python
Exploring Linters to Support Testing in Python: Question 3
Ensure flake8 is in your virtual box -
    pip install flake8
Run flake8 on pylintTest.py
Review the errors returned. In what way does this error message differ from the error message returned by pylint?

Answer:
flake8 is a little bit nicer. It colour codes the errors with red. 
It also is not as aggressive as pylint. It does not force you to use camelCase or upper case on variables.

---------------

Run flake8 on metricTest.py.
Can you correct each of the errors returned by flake8?

Answer:
The error flake8 returned didn't make any sense since it said invalid character '-' when this was a subtraction that is valid. I suspect the issue is happening due to the line number in the file.

After fixing all the errors, the first error still accord, which said invalid character '-'. It turns out it was correct because it was using this character '–' not this character '-'. The difference is so subtle that you don't notice it at the start. These two characters are not the same even though they look the same. This can happen when you use a different language or Unicode. It turns out flake8 was correct, and I didn't believe it because the error didn't make any sense to me.

---------------

What amendments have you made to the code?

Answer:
A lot of changes. Many, many changes. I removed the line numbers. Then I indented the code where it made sense. Once all that was done, I tackled the subtraction error that made no sense. Once that is fixed, I ran Black formatter on the file, and I was left with only two errors from flake8.

metricTest.py:32:80: E501 line too long (86 > 79 characters)
metricTest.py:40:80: E501 line too long (83 > 79 characters)

These errors can be fixed by moving the line into multiple lines.

Finally, flake8 reported everything to be good.