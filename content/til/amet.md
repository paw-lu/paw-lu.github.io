Title: Amet
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Tags: sit, amet
Authors: Paulo S. Costa, Jessica De Silva
Summary: Sed do eiusmod tempor incididunt
lang: en
translation: false
Status: hidden

```python
"""Example syntax highlighting."""
from typing import Iterator


class Math:
    """An example class."""

    @staticmethod
    def fib(n: int) -> Iterator[int]:
        """Fibonacci series up to n."""
        a, b = 0, 1  # Manually set first two terms
        while a < n:
            yield a
            a, b = b, a + b


result = sum(Math.fib(42))
print(f"The answer is {result}")
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Sed vulputate mi sit amet. Mollis
nunc sed id semper risus in hendrerit gravida rutrum. Mi eget mauris pharetra
et ultrices. Eleifend donec pretium vulputate sapien nec sagittis. Bibendum
neque egestas congue quisque. Sed turpis tincidunt id aliquet risus feugiat in
ante. Fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel. In arcu
cursus euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl
condimentum id venenatis a condimentum vitae sapien.
