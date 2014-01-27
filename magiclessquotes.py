#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daryl Tucker"

import sublime, sublime_plugin

class RemoveMagicFromMagic(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        replacements = [
            [u'[’‘`]{1}',u'\''],
            [u'[“”]{1}',u'"'],
            [u'[…]{1}',u'...'],
            [u'[—]{1}',u'---'],
            [u'[–]{1}',u'--'],
            [u'[•]{1}',u'*'],
            [u' & ',u' &amp; '],
        ]
        edit = view.begin_edit()
        for replacement in replacements:
            x = view.find_all(replacement[0])
            for position in x:
                view.replace(edit, position, replacement[1])
        view.end_edit(edit)
