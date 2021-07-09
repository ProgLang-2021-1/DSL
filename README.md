
# Domain-specific Language

The sole purpose of this language is to create a language
that allows us to test a dataset with Friedman's test

## Installation

If it is your first time running this project
you should run the following commands. Make sure
you are on a linux machine:

```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
```

## Running tests

To run files, you should first make sure to have
the virtual environment running

1. **Initializing virtual environment**
Ignore this step if you already have run this command.

Run this command to activate your virtual environment:

```bash
  source .venv/bin/activate
```

2. **Running from files**
Locate the file you want to run on `testing/tests`, i.e:

If the file you want to run is named `case4.fri` and is
already located at `testing/tests`. The command you may run
would be the following:

```bash
  python main.py case4.fri
```

The previous command will give you the input and output of each operation,
in case you want to *only see the output* you can make use of
of the third argument. Setting this argument to `false` will
only display output operations, e.g:

```bash
  python main.py case4.fri false
```

3. **Going back to normal**
In order to deactivate your virtual environment you should
run this command:

```bash
  deactivate
```

And now you are good to go.
