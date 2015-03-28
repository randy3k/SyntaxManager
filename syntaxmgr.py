import sublime
import sublime_plugin
import re


class Sobj():
    def __init__(self, S):
        self.S = S

    def apply(self, view):
        settings = self.S["settings"] if "settings" in self.S else []
        for key, value in settings.items():
            view.settings().set(key, value)

    def check_scopes(self, view):
        scopes = self.S["scopes"] if "scopes" in self.S else []
        scopes_excluded = self.S["scopes_excluded"] if "scopes_excluded" in self.S else []

        return (not scopes or any([view.score_selector(0, s) > 0 for s in scopes])) \
            and all([view.score_selector(0, s) == 0 for s in scopes_excluded])

    def check_extensions(self, view):
        extensions = self.S["extensions"] if "extensions" in self.S else []
        fname = view.file_name()
        extensions = ["." + e for e in extensions]
        return not extensions or (fname and fname.lower().endswith(tuple(extensions)))

    def check_platform(self, view):
        platforms = self.S["platforms"] if "platforms" in self.S else []
        return not platforms or sublime.platform() in [p.lower() for p in platforms]

    def check_firstline(self, view):
        firstlinepat = self.S["firstline"] if "firstline" in self.S else []
        return not firstlinepat \
            or re.match(firstlinepat, view.substr(view.line(view.text_point(0, 0))))

    def check(self, view):
        return self.check_scopes(view) and self.check_extensions(view) and \
            self.check_platform(view) and self.check_firstline(view)


class SyntaxMgrListener(sublime_plugin.EventListener):

    def load_syntax_mgr(self, view):
        if view.is_scratch() or view.settings().get('is_widget'):
            return

        if view.size() == 0 and not view.file_name():
            return

        if not view.settings().has("syntax_mgr_loaded"):
            view.settings().set("syntax_mgr_loaded", True)
            view.run_command("syntax_mgr_reload")

    def on_load(self, view):
        self.load_syntax_mgr(view)

    def on_activated(self, view):
        self.load_syntax_mgr(view)


class SyntaxMgrReload(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = sublime.load_settings('SyntaxMgr.sublime-settings')
        for s in settings.get("syntaxmgr_settings", []):
            S = Sobj(s)
            if S.check(view):
                S.apply(view)
