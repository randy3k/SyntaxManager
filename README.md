Syntax Manager for Sublime Text 2/3
====================
It helps in applying settings to muliple syntaxes and applying syntax to given extensions.


I don't understand why ST makes it so difficult to toogle the same setting across several different syntaxes. 
For example, if someone wants to enable `auto_match_enabled` for `python` and `c`. 
He has to create two files `Packages/User/Python.sublime-settings` and `Packages/User/C.sublime-settings`. 
Then add, in each of the files, 

		"auto_match_enabled": true


This plugin makes it easier by the considering following setting


	    "syntaxmgr_settings": [
	        {
	            "scopes": ["source.c", "source.python"],
	            "settings": {
	                "auto_match_enabled" : true
	            }
	        }
	    ]

###Installation

Package Control!

###Usage

Open `Preference` -> `Syntax Manager Settings`. Below is a sample of what you can specify.
You need to specify either `scopes` or `extensions` for each entry.

```
{
    "syntaxmgr_settings": [
        {
        	// for all source files
            "scopes": ["source"],
            "settings": {
                "trim_trailing_white_space_on_save_scope" : true,
                "auto_match_enabled" : true
            }
        },
        {
        	// for latex files
            "scopes": ["text.tex"],
            "settings": {
	            "auto_match_enabled" : false,
           	    "word_wrap": true,
           	    "rulers": [120]
            }
        },
        {
        	// for comment, all text file, but not latex file
	        "scopes": ["comment", "text", "-text.tex"],
            "settings": {            
		"spell_check": true,
		"color_scheme": "Packages/Color Scheme - Default/Twilight.tmTheme"
            }
        },        
        {
        	// for all non-text file
	        "scopes": ["-text"],
            "settings": {            
			    "spell_check": false
            }
        },
        {
        	// use C++ syntax for all C files
	        "extensions": ["c", "cpp", "c++"],
            "settings": {            
			    "syntax": "Packages/C++/C++.tmLanguage",
			    "spell_check": false			    
            }
        }        
    ]
}
```
