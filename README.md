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

Open `Preference` -> `Syntax Manager`. Below is a sample of what you can specify.
You need to specify either `scopes`, `scopes_excluded` or `extensions` for each entry.


```
{
    "syntaxmgr_settings": [
        {
        	// for c and python files
		"scopes": ["source.c", "source.python"],
		"settings": {
                "trim_trailing_white_space_on_save_scope" : true,
                "auto_match_enabled" : true
            }
        },
        {
        	// all text files
	        "scopes": ["text"],
		"settings": {            
			"spell_check": true,
			"color_scheme": "Packages/Color Scheme - Default/Twilight.tmTheme"
		}
        },
        {
        	// use latex syntex for these extensions
        	// if you apply a syntax to certain extensions and apply some settings to such syntax
        	// make sure you do apply the syntax first and then apply the settings.
        	"extensions": ["ltx", "latex","l"],
		"settings": {            
			"syntax": "Packages/LaTeX/LaTeX.tmLanguage"			    
		}
        },          
        {
        	// for all text files, excluding latex files
	        "scopes": ["text"],
		"scopes_excluded": ["text.tex"],
		"settings": {            
			"spell_check": false
		}
        }      
    ]
}
```
