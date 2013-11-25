# Livetex-Tools

Build system from LiveTex.

#### Install via npm:
    npm install livetex-tools


## Principles: 

Build system works with artifacts by means of Make.    
Every command runs according to pattern: %suffix,     
where % is the name of artifact.    


Project should contain in its root directory:

+ **./etc/index.d**     
The list of project files paths relating to SOURCE_PATH in rule.    

+ **./etc/index.jst**   
The structure of compiled code:    
    - requires   
    - %%CONTENT%%   
    - exports   
    and maybe some additional code.   

+ **./etc/config.json**   
Configuration file for Jstuff tool, which generates externs and documentation.   

+ **./Makefile**   
Main file, which includes rules:  
    
    include node_modules/livetex-tools/rules/%%RULE_NAME%%.mk   

## Rules:


### Javascript: js.mk

**1. To create the main script:**

    make

**2. To run the main script with nodejs:** 

    make %.js-run

**3. To assemble code:**  

    make %.js-compile

**4. To check compiled code:**

    make %.js-lint

**5. To compile code and check it with linter:**  

    make %.js-check

**6. To remove the main script:**    

    make %.js-clean

**7. To generates externs for code:**     

    make %-externs


### CSS: css.mk

**1. To create the main css file:**   

    make %.css-compile

**2. To create the main css file for mobile layout:**   

    make %.css-mobile-compile


## License

Modified BSD License
