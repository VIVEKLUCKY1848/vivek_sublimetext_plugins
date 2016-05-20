## Plugin to copy current file's path to clipboard
import sublime
import sublime_plugin


class CopyPathToClipboard(sublime_plugin.TextCommand):
    def run(self, edit):
        line_number, column = self.view.rowcol(self.view.sel()[0].begin())
        line_number += 1
        #sublime.set_clipboard(self.view.file_name() + ':' + str(line_number))
        sublime.set_clipboard(self.view.file_name())
        
# Past this code into file: copy_path_to_clipboard.py inside Sublime Text 3 Packages/User directory
# Also get Main.sublime-menu file for running this plugin from Main menu "Vivek's Commands"

## Plugin to copy current file's name to clipboard
import sublime
import sublime_plugin
import ntpath


class CopyFilenameToClipboard(sublime_plugin.TextCommand):
    def run(self, edit):
        line_number, column = self.view.rowcol(self.view.sel()[0].begin())
        line_number += 1
        currFileName = ntpath.basename(self.view.file_name())
        #sublime.set_clipboard(self.view.file_name() + ':' + str(line_number))
        sublime.set_clipboard(currFileName)
        
# Past this code into file: copy_filename_to_clipboard.py inside Sublime Text 3 Packages/User directory
# Also get Main.sublime-menu file for running this plugin from Main menu "Vivek's Commands"

## Plugin to copy current file's path from 'app' directory to clipboard
import sublime
import sublime_plugin
import os


class FilepathFromSkinDir(sublime_plugin.TextCommand):
    def run(self, edit):
        fullpath = self.view.file_name()
        point = "app"
        finalPath = fullpath[fullpath.index(point):]
        finalPath = os.path.dirname(finalPath)
        sublime.set_clipboard(finalPath)

# Past this code into file: filepath_from_app_dir.py inside Sublime Text 3 Packages/User directory
# Also get Main.sublime-menu file for running this plugin from Main menu "Vivek's Commands"

## Plugin to copy current file's path from 'app' directory to clipboard
import sublime
import sublime_plugin
import os


class FilepathFromSkinDir(sublime_plugin.TextCommand):
    def run(self, edit):
        fullpath = self.view.file_name()
        point = "skin"
        finalPath = fullpath[fullpath.index(point):]
        finalPath = os.path.dirname(finalPath)
        sublime.set_clipboard(finalPath)

# Past this code into file: filepath_from_skin_dir.py inside Sublime Text 3 Packages/User directory
# Also get Main.sublime-menu file for running this plugin from Main menu "Vivek's Commands"
