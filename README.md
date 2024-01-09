<h1 align="center">HyperText Low Level Language<h1>

# Description

HyperText Low Level Language is a low level language similar in looks to `HTML`. It is designed to be easy to read and write, but works low level and translates almost directly into the type of code you write into the terminal with the exception of some tags shown below.

```html

# HTLLL works by using bash commands in order
# The following script will create a directory called testDir, 
# make 5 files in it, use ls, and then delete the directory
# In normal bash this would be: 
# mkdir testDir; cd testDir; touch file1 file2 file3 file4 file5; ls; cd ..; rm -rf testDir
# This will now be written in HTLLL:

# In HTLLL, as you probably suspected, comments use the hash symbol
# Each HTLLL file starts with the <kernel> tag and ends with the </kernel> tag
<kernel>
    # The import tag allows you to import builtin python modules
    <import>
        # And the module tag allows you to specify the module to import
        <module>
            os
        </module>
    </import>
    # To set variables you must use the <envVars> tag
    <envVars>
        # Variables are set using the <var> tag
        <var name="dirToMake">
            # You set the value of the variable in between the <var> tag
            # In this case however, I want the user to be able to set the value
            # So I use the <input> tag
            <input>
                # The input tag has an inner <prompt> tag
                # The prompt tag is the text that will be displayed to the user
                <prompt>
                    Enter the name of the directory to make:
                </prompt>
            </input>
        </var>
        # Get the system ("Linux", "Darwin", "Windows)
        <var name="system">
            # To get a value from a python module you must use the <py> tag
            # The <py> tag has an inner <module> tag and an inner <function> tag or <value> tag
            <py>
                <module>
                    os
                </module>
                # Run the uname() function and bring its return value to scope
                <function>
                    uname
                </function>
                # To get the name of the system you must use the <value> tag
                <value name="sysname">
                    <var sysInfo="system"/>
                </value>
            </py>
        </var>
        # And this sets the value of "system" to the value of os.uname().sysname
    </envVars>
    # Each base tag is a command and all commands run in order
    # To run a command you make a tag with the command name inside
    <mkdir>
        # Allowed inner tags are options and args
        # Options allow things like -r or --version
        <args>
            # To use a variable you must use the <var> tag 
            # and add an "/" at the end to signify its not being set or 
            # that the tag is one without an inner tag.
            # To make the value the literal string "<var name="dirToMake"/>"
            # you must use the <literal> tag
            <var name="dirToMake"/>
        </args>
    </mkdir>
    <cd>
        <args>
            <var name="dirToMake"/>
        </args>
    </cd>
    # The <script> tag allows for if statements, for loops, while loops, and functions
    # All functions must be defined in the envVars tag
    # Script if else statements and for loops can be used in the normal kernel
    <script>
        # In the script tag everything is either python or bash
        # for, while, if, elif, else, and functions are python
        # Everything else is bash
        for i in range(5):
            <touch>
                <args>
                    # To use variables inside of a line you use {$varName}
                    # Again, to use the literal string "{$varName}" you must use the <literal> tag
                    file{$i}
                </args>
            </touch>
    </script>
    # For single line bash commands you are not required to use an end tag
    <ls>
    <cd>
        <args>
            ..
        </args>
    </cd>
    <rm>
        <option>
            -rf
        </option>
        <args>
            <var name="dirToMake"/>
        </args>
    </rm>
</kernel>
```

The special tags are:
- `<input>`: Allows the user to input a value
- `<py>`: Allows you to use python modules
- `<script>`: Allows you to use python and bash
- `<literal>`: Allows you to use the literal string of the inner tag (inner uses are nullified and assumed part of the string literal)
- `<var>`: Allows you to use variables
- `<option>`: Allows you to use options
- `<args>`: Allows you to use arguments
- `<envVars>`: Allows you to set variables
- `<import>`: Allows you to import python modules
- `<module>`: Allows you to specify the module to import and bring it into scope
- `<function>`: Allows you to specify the function to use from the current module in scope
- `<value>`: Allows you to specify the value to use from the current module or function return in scope
- `<kernel>`: The main tag that contains all the other tags

# Installation
To install HTLLL you must have python3 installed. Then you can install HTLLL by running the following command:
```bash
pip3 install htlll_runner
```

# Usage
Once you have installed HTLLL you can run it by running the following command:
```bash
htlll_runner "path/to/file.htlll"
```

