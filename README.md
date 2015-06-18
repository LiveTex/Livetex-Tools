# Livetex-Tools

Build system from LiveTex.

#### Install via npm:
    npm -g i livetex-tools


## Principles: 

Build system works with artifacts by means of Make.

Project structure:

  *-|
    `--- etc
    |   |
    |   `----build
    |        |----*.*t    Templates
    |        `----*.*d    Sources lists
    `--- lib              Sources

    
+ **Templates:**
    ```
    TAG     : /*%COMMAND%*/
    COMMAND : any command which can be executed via terminal or make command
              contained in Makefile  
    !note   : it is preferably to use -s flag with make 
    ```

+ **Sources lists:**
Lists of files that can be used as prerequisites for targets in make

## Rules: 

+ **For templates**:        
can be used as COMMAND in TAG   

    ```
    syntax: %.extension-prefix
            %         - name of sources list
            extension - js or css
            prefix    - name of action
    ```
    
**js**: js.mk    

    %.js-compile                    :   glues all js files mentioned in sources list  
                                        into single stream and inserts it instead of TAG
                                        
    %.js-compile-compressed         :   compiles and compresses all js files mentioned  
                                        in sources list by means of google-closure-compiler  
                      !note         :   code shouldn`t dependend on any library
                                        
    %.js-externs-compile-compressed :   compiles and compresses all js files mentioned 
                                        in sources list by means of google-closure-compiler   
                                        with externs taken from ./externs folder   
                                        of each dependency (node_modules)


+ **General**:
can be used as script in NPM  

**js**: js.mk  

    js-check                        -   checks code style of sources mentioned
                                        in sources listswith google-closure-linter
                                    -   checks syntax with google-closure-compiler

    js-build                        -   removes built files and externs
                                    -   assembles js templates
                                    -   extracts externs from built files
