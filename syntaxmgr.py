import sublime, sublime_plugin

IS_LOADED = {}

class Sobj():
    def __init__(self, S):
        self.scopes = S["scopes"] if "scopes" in S else []
        self.scopes_excluded = S["scopes_excluded"] if "scopes_excluded" in S else []
        self.extensions = S["extensions"] if "extensions" in S else []
        self.settings = S["settings"] if "settings" in S else []

    def apply(self, view):
        for key, value in self.settings.items():
            view.settings().set(key, value)

    def check(self, view):
        fname = view.file_name()
        in_scopes = not self.scopes or any([view.score_selector(0, s)>0 for s in self.scopes])
        in_scopes_excluded = any([view.score_selector(0, s)>0 for s in self.scopes_excluded])
        extensions = ["." + e for e in self.extensions]
        in_extensions = not extensions or (fname and fname.lower().endswith(tuple(extensions)))
        return in_scopes and in_extensions and not in_scopes_excluded


class SyntaxMgrListener(sublime_plugin.EventListener):
    settings = None

    def on_activated(self, view):
        if view.is_scratch() or view.settings().get('is_widget'): return
        if view.size()==0 and not view.file_name(): return
        if not self.settings: self.settings = self.load_settings()
        if view.id() not in IS_LOADED:
            IS_LOADED.update({view.id() : True})
            for S in self.settings:
                if S.check(view): S.apply(view)

    def load_settings(self):
        syntaxmgr_settings = sublime.load_settings('SyntaxMgr.sublime-settings').get("syntaxmgr_settings")
        return [Sobj(S) for S in syntaxmgr_settings]



