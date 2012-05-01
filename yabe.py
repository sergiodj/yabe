# -*- coding: utf-8 -*-
"""
  YABE -- Yet Another Blog Engine

  This is another blog engine, which is basically written for developers
  and coders who want a nice...  blog engine, yeah.  Its main advantages are:

  - You can (should) create your posts using your favorite $EDITOR.  No GUI,
  no WYSIWYG, only your good, old text editor.

  - You can have a comment system.

"""

import sqlite3
from flask import Flask, render_template

app = Flask (__name__)

if __name__ == '__main__':
  app.run ()
