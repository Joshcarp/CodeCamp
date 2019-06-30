
"""
This module implements unit testing functionality for validation of output from the python CodeCamp program.

(Haohan Liu 2019-06)
"""


class UnitTest:
    """Implements unit testing functionality for user created methods and     functions."""

    def __init__(self, func_str, noPrint=False, returnOutput=False):
        """Initialise unit testing class with the function to test."""
        assert isinstance(func_str, str), "function input must be of type 'str'"
        self.func = func_str
        self.noPrint = noPrint
        self.returnOutput = returnOutput

        # class states
        self.isTesting = False

    def _nl_(self):
        """Print a new line."""
        print('\n', end='')

    def _hr_(self, key='=', width=80):
        """Print a horizontal rule of 'key=' characters 'width=' long."""
        print(key * width)

    # def _kw_handler_(self, key, val, **kwargs):
    #     """Check conditionality of keyword argument inputs concisely."""
    #     if key in kwargs and kwargs[key] == val:
    #         return True
    #     return False

    def _args2str_(self, args):
        """Return a string containing comma separated items from argument list."""
        # ensure that 'string' inputs are preserved with apostrophes
        str_args = []
        for arg in args:
            if isinstance(arg, str):
                str_args.append(f"'{arg}'")
            else:
                str_args.append(str(arg))
        # return joined string of input arguments
        return ', '.join(x for x in str_args)

    def _kwargs2str_(self, kwargs):
        """Return a string containing comma separated items from key argument list."""
        # ensure that 'string' key val inputs are preserved with apostrophes
        str_kwargs = []
        for k, v in kwargs.items():
            if isinstance(v, str):
                str_kwargs.append((str(k), f"'{v}'"))
            else:
                str_kwargs.append((str(k), str(v)))
        # return joined string of input key arguments
        return ', '.join(f"{k}={v}" for k, v in str_kwargs)

    def _func2str_(self, args, kwargs):
        """Return a string representation of the function tested."""
        if args and kwargs:
            f_pstr = f"{self.func}({self._args2str_(args)}, {self._kwargs2str_(kwargs)})"
        elif args:
            f_pstr = f"{self.func}({self._args2str_(args)})"
        elif kwargs:
            f_pstr = f"{self.func}({self._kwargs2str_(kwargs)})"
        else:
            f_pstr = f"{self.func}()"
        return f_pstr

    def run(self, *args, **kwargs):
        """Run the function and print the function output given a set of arguments the function would naturally take.

        If a return value is desired, pass in key 'returnOutput=True'.
        """
        # evaluate the function with all args and kwargs
        f_str = f"{self.func}(*{args}, **{kwargs})"
        f_out = eval(f_str)

        # create function representation for print output
        f_pstr = self._func2str_(args, kwargs)

        # print output, if not explicitly disabled
        if not self.noPrint and not self.isTesting:
            print(' [IN]', f_pstr)

            # handle printing of string types accurately
            if isinstance(f_out, str):
                print('[OUT]', f"'{f_out}'")
            else:
                print('[OUT]', f_out)
            self._hr_()

        # return output
        if self.returnOutput or self.isTesting:
            return f_out

    def test(self, expected_output, *args, **kwargs):
        """Test the function and compare the output to an expected correct output.

        The expected output is the first argument of the test() method. All other arguments will be passed onto the function tested.
        """
        # set class state
        self.isTesting = True

        # capture test output
        f_out = self.run(*args, **kwargs)

        # return state to default
        self.isTesting = False

        # grab print string of function input
        f_pstr = self._func2str_(args, kwargs)

        # print output, if not explicitly disabled
        if not self.noPrint:
            print(' [IN]', f_pstr)

            # handle printing of string types accurately
            if isinstance(f_out, str):
                print('[OUT]', f"'{f_out}'")
            else:
                print('[OUT]', f_out)

            if isinstance(expected_output, str):
                print('[EXP]', f"'{expected_output}'")
            else:
                print('[EXP]', expected_output)
            self._hr_()

        # return test result in bool
        if f_out == expected_output:
            return True
        return False
