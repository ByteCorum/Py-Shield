class CFG:
    name = "Py-Shield"
    author = "ByteCorum"
    github = "https://github.com/ByteCorum/Py-Shield"
    version = "v2.0.0.0"

    helpText = f'''
{name}
{version}
                      
options:
code.py         -> main .py file with the entry point to your app
--mode*   (list)-> obfuscation mode
keys:
    hashstr     -> convert all strings and var names into hash
    crypt       -> obfuscation and ecryption using cryptography
    looping     -> looping obfuscation, best to hide the program from AVs (--loops required)
    aes         -> obfuscation and ecryption using aes256
--loops    (int)-> number of obfuscation loops for looping
--dirs     (str)-> obfuscate all in dir
--files    (str)-> files for obfuscation
--output   (str)-> output dir  
--follow imports-> add all imports to the protected script
--install-deps  -> install all dependencis
--help          -> get help
*               -> required option
text;text       -> to add more than one arg to option
                      
example of usage:
py-shield --mode hashstr;crypt code.py'''