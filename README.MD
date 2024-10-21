# L-CONVERTERS
## What is it?
### converters from smt to smt
## how to install:
    pip install l-converters
####
    OR USE
####
    python -m pip install l-converters
####
    OR USE
####
    git clone https://github.com/Sasha246sasha/l-converters.git
    cd "l-converters" OR cd l-converters
    python setup.py install
## how to use:
    import l_converters
####
    # md text to html text
    print(l_converters.FromMDtoHTML.text_to_text('''# good converter ) ## abc'''))
####
    # md text to html file
    l_converters.FromMDtoHTML.text_to_file('''# good converter ) ## abc''', "res.html")
#### _**! NOW l-converters only convert from MD to HTML !**_