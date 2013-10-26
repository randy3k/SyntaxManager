Syntax Manager for Sublime Text 2/3
====================
Manage settings for muliple syntax

I don't understand why ST makes it so difficult to toogle the same setting across several different syntaxes. For example, if someone wants to enable `auto_match_enabled` for `python` and `c`. He has to create two files under `Packages/User/Python.sublime-settings` and `Packages/User/C.sublime-settings`. Then add, in each of the files, 

	"auto_match_enabled": true


This plugin makes this easier by the following setting in the user perferece file


    "syntaxmgr_settings": [
        {
            "scopes": ["source.c", "source.python"],
            "settings": {
                "auto_match_enabled" : true
            }
        }
    ]


###Sample

You can either specific `scopes` or `extensions`

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
        	// for all text file, but not latex file
	        "scopes": ["text", "-text.tex"],
            "settings": {            
			    "spell_check": true
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
            }
        }        
    ]