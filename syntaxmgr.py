import sublime, sublime_plugin
import re


class Sobj():
    def __init__(self, S):
        self.scopes = S["scopes"] if "scopes" in S else []
        self.scopes_excluded = S["scopes_excluded"] if "scopes_excluded" in S else []
        self.extensions = S["extensions"] if "extensions" in S else []
        self.platforms = S["platforms"] if "platforms" in S else []
        self.firstlinepat = S["firstline"] if "firstline" in S else []
        self.settings = S["settings"] if "settings" in S else []

    def apply(self, view):
        for key, value in self.settings.items():
            view.settings().set(key, value)

    def check(self, view):
        fname = view.file_name()
        in_scopes = not self.scopes or any([view.score_selector(0, s)>0 for s in self.scopes])
        in_scopes_excluded = any([view.score_selector(0, s)>0 for s in self.scopes_excluded])
        extensions = ["." + e for e in self.extensions]
        in_extensions = not extensions or \
            (fname and fname.lower().endswith(tuple(extensions)))
        in_platforms = not self.platforms or sublime.platform() in [p.lower() for p in self.platforms]
        firstline_matched = True if not self.firstlinepat \
            or re.match(self.firstlinepat, view.substr(view.line(view.text_point(0,0)))) else False
        return in_scopes and in_extensions and not in_scopes_excluded and in_platforms and firstline_matched


class SyntaxMgrListener(sublime_plugin.EventListener):

    def on_load(self, view):
        if view.is_scratch() or view.settings().get('is_widget'): return
        if view.size()==0 and not view.file_name(): return
        if not view.settings().has("syntax_mgr_loaded"):
            view.run_command("syntax_mgr_reload")

    def on_activated(self, view):
        if view.is_scratch() or view.settings().get('is_widget'): return
        if view.size()==0 and not view.file_name(): return
        if not view.settings().has("syntax_mgr_loaded"):
            view.settings().set("syntax_mgr_loaded", True)
            view.run_command("syntax_mgr_reload")


class SyntaxMgrReload(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = sublime.load_settings('SyntaxMgr.sublime-settings').get("syntaxmgr_settings")
        for s in settings:
            S = Sobj(s)
            if S.check(view): S.apply(view)
