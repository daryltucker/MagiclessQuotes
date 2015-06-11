#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin, re

__author__ = "Daryl Tucker"


class RemoveMagicFromMagicCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        replacements = [
            [u'[‘’]', u'\''],
            [u'[“”]', u'"'],
            [u'[…]', u'...'],
            [u'[—]', u'---'],
            [u'[–]', u'--'],
            [u'[•]', u'-']
        ]

        for replacement in replacements:
            region = sublime.Region(0, self.view.size())
            content = self.view.substr(region)
            content = re.sub(replacement[0], replacement[1], content)
            self.view.replace(edit, region, content)

class RunMagic(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command('remove_magic_from_magic')

##############################################################################
