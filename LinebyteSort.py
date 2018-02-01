import sublime
import sublime_plugin

LINE_ENDING_CHARACTER = '\n'


def sort_lines(input_lines):
    return sorted(input_lines, key=lambda x:len(x))

class LinebytesortCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        regions = self.view.sel()

        if len(regions) == 1 and regions[0].empty():
            # Selection is empty, use the entire buffer.
            regions = [sublime.Region(0, self.view.size())]

        for region in regions:
            input_lines = [self.view.substr(r) for r in self.view.lines(region)]
            # print(input_lines)
            sorted_lines = sort_lines(input_lines)

            output = LINE_ENDING_CHARACTER.join(sorted_lines)

            # If the end of the region had a line ending character, we re-add
            # it here
            if self.view.substr(region).endswith(LINE_ENDING_CHARACTER):
                output += LINE_ENDING_CHARACTER

            self.view.replace(edit, region, output)
