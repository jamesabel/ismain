Sundry
======

A prettier way to test for `main`.

is_main()
---------

Instead of the not-so-pretty:

.. code-block:: python

    if __name__ == "__main__":
        main()


pip install `ismain` from PyPI:

.. code-block:: shell

    $pip install ismain

And use ``is_main()`` from `ismain`:

.. code-block:: python

    from ismain import is_main

    if is_main():
        main()

