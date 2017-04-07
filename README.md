# Syntax Manager for Sublime Text 2/3

It helps in applying settings to given syntaxes and extensions.

I don't understand why Sublime Text makes it so difficult to apply the same setting across several different syntaxes.
For example, if someone want to enable `auto_match_enabled` for `python` and `c`, they has to create two files:
- `Packages/User/Python.sublime-settings`
- `Packages/User/C.sublime-settings`

Then, in each of the files, add:

        "auto_match_enabled": true


This plugin makes it easier by considering following setting in Syntax Manger:


        "syntaxmgr_settings": [
            {
                "scopes": ["source.c", "source.python"],
                "settings": {
                    "auto_match_enabled" : true
                }
            }
        ]

## Installation

Package Control!

## Usage

Open `Preference` -> `Syntax Manager`. Below is a sample of what you can specify in the settings file.
For each item, you need to provide at least one of the filters

- `scopes` 
- `scopes_excluded` 
- `extensions`
- `platforms`
- `first_line_match`

```js
{
    "syntaxmgr_settings": [
        {
            // platforms, can be osx, windows or linux
            "platforms": ["linux", "windows"],
            "settings": {
                "font_size" : 14
            }
        },
        {
            // match a specific computer based on hostname
            // the hostname can be found by running
            //
            //     import platform
            //     platform.node()
            //
            // at sublime console (ctrl + ` )
            //
            "hostnames": ["some-hostname"],
            "settings": {
                "font_size" : 12
            }
        },
        {
            // apply this setting when first line matches
            // be careful that it is not a list but a string
            "first_line_match": "#!/.*?/sh",
            "settings": {
                // the syntax can be identified by running
                //
                //     view.settings().get("syntax")
                //
                // at sublime console (ctrl + ` )
                //
                "syntax" : "Packages/ShellScript/Shell-Unix-Generic.tmLanguage"
            }
        },
        {
            // the scope of the document can be obtained by pressing
            // cmd+alt+p (mac) or ctrl+alt+shift+p (linux / windows)

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
            // make sure the syntax is applied first and then the settings
            "extensions": ["ltx", "latex", "l"],
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

###Reload Settings

Occasionally, syntax manager may fail to apply settings automatically,
especially when creating new file. Reloading syntax manger will be helpful in
this situation. To reload settings, launch comment palette (`C+shift+p`) and type "Syntax Manager: Reload Settings".
