import sublime
import sublime_plugin
import re


class SyntaxManagerCriteria():
    def __init__(self, S):
        self.S = S

    def apply(self, view):
        settings = self.S.get("settings", [])
        for key, value in settings.items():
            view.settings().set(key, value)

    def match_scopes(self, view):
        scopes = self.S.get("scopes", [])
        scopes_excluded = self.S.get("scopes_excluded", [])

        return (not scopes or any([view.score_selector(0, s) > 0 for s in scopes])) \
            and all([view.score_selector(0, s) == 0 for s in scopes_excluded])

    def match_extensions(self, view):
        extensions = self.S.get("extensions", [])
        if not extensions:
            return True

        fname = view.file_name()
        extensions = ["." + e for e in extensions]
        return fname and fname.lower().endswith(tuple(extensions))

    def match_platform(self, view):
        platforms = self.S.get("platforms", [])
        if not platforms:
            return True

        return sublime.platform() in [p.lower() for p in platforms]

    def match_firstline(self, view):
        firstlinepat = self.S.get("firstline", [])
        if not not firstlinepat:
            return True

        first_line = view.substr(view.line(view.text_point(0, 0)))
        return re.match(firstlinepat, first_line)

    def match(self, view):
        return self.match_scopes(view) and self.match_extensions(view) and \
            self.match_platform(view) and self.match_firstline(view)


class SyntaxMgrListener(sublime_plugin.EventListener):

    def on_load(self, view):
        if view.is_scratch() or view.settings().get('is_widget'):
            return
        if view.size() == 0 and not view.file_name():
            return
        if not view.settings().has("syntax_mgr_loaded"):
            view.run_command("syntax_mgr_reload")

    def on_activated(self, view):
        if view.is_scratch() or view.settings().get('is_widget'):
            return
        if view.size() == 0 and not view.file_name():
            return
        if not view.settings().has("syntax_mgr_loaded"):
            view.settings().set("syntax_mgr_loaded", True)
            view.run_command("syntax_mgr_reload")


class SyntaxMgrReload(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = sublime.load_settings('SyntaxMgr.sublime-settings').get("syntaxmgr_settings", [])
        for s in settings:
            criteria = SyntaxManagerCriteria(s)
            if criteria.match(view):
                criteria.apply(view)
