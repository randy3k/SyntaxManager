import sublime, sublime_plugin

class Sobj():
    def __init__(self, view, S):
        self.scopes = S["scopes"] if "scopes" in S else []
        self.extensions = S["extensions"] if "extensions" in S else []
        self.settings = S["settings"] if "settings" in S else []
        self.view =view

    def apply(self):
        view = self.view
        for key, value in self.settings.items():
            view.settings().set(key, value)

    def check(self):
        view = self.view
        fname = view.file_name()
        in_scopes = not self.scopes or any([view.score_selector(0, s)>0 for s in self.scopes])
        extensions = ["." + e for e in self.extensions]
        in_extensions = not extensions or fname.lower().endswith(tuple(extensions))
        return in_scopes and in_extensions


class SyntaxMgrListener(sublime_plugin.EventListener):
    def on_load(self, view):
        if view.is_scratch() or view.settings().get('is_widget'): return
        for S in self.load_settings(view):
            if S.check(): S.apply()

    def load_settings(self, view):
        syntaxmgr_settings = sublime.load_settings('SyntaxMgr.sublime-settings').get("syntaxmgr_settings")
        return [Sobj(view, S) for S in syntaxmgr_settings]


