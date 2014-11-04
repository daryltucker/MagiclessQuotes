#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daryl Tucker"

import sublime, sublime_plugin

class RemoveMagicFromMagicCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        replacements = [
            [u'[’‘]{1}',u'\''],
            [u'[“”]{1}',u'"'],
            [u'[…]{1}',u'...'],
            [u'[—]{1}',u'---'],
            [u'[–]{1}',u'--'],
            [u'[•]{1}',u'*'],
            #[u' & ',u' &amp; '],
        ]

        for replacement in replacements:
            x = self.view.find_all(replacement[0])
            for position in x:
                self.view.replace(edit, position, replacement[1])
        self.view.end_edit(edit)

class RunMagic(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command('remove_magic_from_magic')
