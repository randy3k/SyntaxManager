import sublime, sublime_plugin
import os

class TrimListener(sublime_plugin.EventListener):
    def on_load(self, view):
        if view.is_scratch() or view.settings().get('is_widget'): return
        syntaxmgr_settings = sublime.load_settings('SyntaxMgr.sublime-settings').get("syntaxmgr_settings")
        if not syntaxmgr_settings: return

        for ss in syntaxmgr_settings:
            scopes = ss["scopes"] if "scopes" in ss else []
            extensions = ss["extensions"] if "extensions" in ss else []   
            extensions = ["." + e for e in extensions]         
            fname = view.file_name()
            if (not scopes or view.score_selector(0, " ".join(scopes))) and \
               (not extensions or fname.lower().endswith(tuple(extensions))):
                for key, value in ss["settings"].items():
                    view.settings().set(key, value)


