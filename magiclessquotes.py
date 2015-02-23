#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

__author__ = "Daryl Tucker"


class RemoveMagicFromMagicCommand(sublime_plugin.TextCommand):
    def run(self, edit, user_input=None):
        self.edit = edit
        replacements = [
            [u'[’‘]{1}', u'\''],
            [u'[“”]{1}', u'"'],
            [u'[…]{1}', u'...'],
            [u'[—]{1}', u'---'],
            [u'[–]{1}', u'--'],
            [u'[•]{1}', u'*'],
            #[u' & ',u' &amp; '],
        ]

        for replacement in replacements:
            x = self.view.find_all(replacement[0])
            dif = 1 - len(replacement[1])
            m = 0
            for position in x:
                difx = m * dif
                p = list(position)
                pos = sublime.Region(p[0] - difx, p[1] - difx)
                self.view.replace(edit, pos, replacement[1])
                m += 1
        self.view.end_edit(edit)


class RunMagic(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command('remove_magic_from_magic')

##############################################################################
