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
            for region in self.view.find_all(replacement[0]):
                self.view.replace(edit, region, replacement[1])


class RunMagic(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command('remove_magic_from_magic')

##############################################################################
