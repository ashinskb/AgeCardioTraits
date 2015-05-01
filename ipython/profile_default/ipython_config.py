# Configuration file for ipython.

c = get_config()

#------------------------------------------------------------------------------
# InteractiveShellApp configuration
#------------------------------------------------------------------------------

# A Mixin for applications that start InteractiveShell instances.
# 
# Provides configurables for loading extensions and executing files as part of
# configuring a Shell environment.
# 
# The following methods should be called by the :meth:`initialize` method of the
# subclass:
# 
#   - :meth:`init_path`
#   - :meth:`init_shell` (to be implemented by the subclass)
#   - :meth:`init_gui_pylab`
#   - :meth:`init_extensions`
#   - :meth:`init_code`

# Run the file referenced by the PYTHONSTARTUP environment variable at IPython
# startup.
# c.InteractiveShellApp.exec_PYTHONSTARTUP = True

# lines of code to run at IPython startup.
# c.InteractiveShellApp.exec_lines = []

# dotted module name of an IPython extension to load.
# c.InteractiveShellApp.extra_extension = ''

# A list of dotted module names of IPython extensions to load.
# c.InteractiveShellApp.extensions = []

# A file to be run
# c.InteractiveShellApp.file_to_run = ''

# If true, IPython will populate the user namespace with numpy, pylab, etc. and
# an ``import *`` is done from numpy and pylab, when using pylab mode.
# 
# When False, pylab mode should not import any names into the user namespace.
# c.InteractiveShellApp.pylab_import_all = True

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.InteractiveShellApp.pylab = None

# Configure matplotlib for interactive use with the default matplotlib backend.
# c.InteractiveShellApp.matplotlib = None

# List of files to run at IPython startup.
# c.InteractiveShellApp.exec_files = []

# Execute the given command string.
# c.InteractiveShellApp.code_to_run = ''

# Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'none',
# 'osx', 'pyglet', 'qt', 'qt4', 'tk', 'wx').
# c.InteractiveShellApp.gui = None

# Should variables loaded at startup (by startup files, exec_lines, etc.) be
# hidden from tools like %who?
# c.InteractiveShellApp.hide_initial_ns = True

# Run the module as a script.
# c.InteractiveShellApp.module_to_run = ''

#------------------------------------------------------------------------------
# TerminalIPythonApp configuration
#------------------------------------------------------------------------------

# TerminalIPythonApp will inherit config from: BaseIPythonApplication,
# Application, InteractiveShellApp

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.TerminalIPythonApp.copy_config_files = False

# A list of dotted module names of IPython extensions to load.
# c.TerminalIPythonApp.extensions = []

# Whether to display a banner upon starting IPython.
# c.TerminalIPythonApp.display_banner = True

# dotted module name of an IPython extension to load.
# c.TerminalIPythonApp.extra_extension = ''

# Start IPython quickly by skipping the loading of config files.
# c.TerminalIPythonApp.quick = False

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.TerminalIPythonApp.verbose_crash = False

# If true, IPython will populate the user namespace with numpy, pylab, etc. and
# an ``import *`` is done from numpy and pylab, when using pylab mode.
# 
# When False, pylab mode should not import any names into the user namespace.
# c.TerminalIPythonApp.pylab_import_all = True

# Set the log level by value or name.
# c.TerminalIPythonApp.log_level = 30

# Run the file referenced by the PYTHONSTARTUP environment variable at IPython
# startup.
# c.TerminalIPythonApp.exec_PYTHONSTARTUP = True

# Configure matplotlib for interactive use with the default matplotlib backend.
# c.TerminalIPythonApp.matplotlib = None

# Execute the given command string.
# c.TerminalIPythonApp.code_to_run = ''

# A file to be run
# c.TerminalIPythonApp.file_to_run = ''

# Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'none',
# 'osx', 'pyglet', 'qt', 'qt4', 'tk', 'wx').
# c.TerminalIPythonApp.gui = None

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.TerminalIPythonApp.pylab = None

# Run the module as a script.
# c.TerminalIPythonApp.module_to_run = ''

# lines of code to run at IPython startup.
# c.TerminalIPythonApp.exec_lines = []

# If a command or file is given via the command-line, e.g. 'ipython foo.py',
# start an interactive shell after executing the file or command.
# c.TerminalIPythonApp.force_interact = False

# The IPython profile to use.
# c.TerminalIPythonApp.profile = 'default'

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.TerminalIPythonApp.ipython_dir = ''

# The date format used by logging formatters for %(asctime)s
# c.TerminalIPythonApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# Suppress warning messages about legacy config files
# c.TerminalIPythonApp.ignore_old_config = False

# Whether to overwrite existing config files when copying
# c.TerminalIPythonApp.overwrite = False

# The Logging format template
# c.TerminalIPythonApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# List of files to run at IPython startup.
# c.TerminalIPythonApp.exec_files = []

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.TerminalIPythonApp.extra_config_file = ''

# Should variables loaded at startup (by startup files, exec_lines, etc.) be
# hidden from tools like %who?
# c.TerminalIPythonApp.hide_initial_ns = True

#------------------------------------------------------------------------------
# TerminalInteractiveShell configuration
#------------------------------------------------------------------------------

# TerminalInteractiveShell will inherit config from: InteractiveShell

# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
# c.TerminalInteractiveShell.ast_node_interactivity = 'last_expr'

# 
# c.TerminalInteractiveShell.readline_parse_and_bind = ['tab: complete', '"\\C-l": clear-screen', 'set show-all-if-ambiguous on', '"\\C-o": tab-insert', '"\\C-r": reverse-search-history', '"\\C-s": forward-search-history', '"\\C-p": history-search-backward', '"\\C-n": history-search-forward', '"\\e[A": history-search-backward', '"\\e[B": history-search-forward', '"\\C-k": kill-line', '"\\C-u": unix-line-discard']

# 
# c.TerminalInteractiveShell.history_length = 10000

# Enable magic commands to be called without the leading %.
# c.TerminalInteractiveShell.automagic = True

# Start logging to the default log file.
# c.TerminalInteractiveShell.logstart = False

# Set the color scheme (NoColor, Linux, or LightBG).
# c.TerminalInteractiveShell.colors = 'Linux'

# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). deep_reload()
# forces a full reload of modules whose code may have changed, which the default
# reload() function does not.  When deep_reload is off, IPython will use the
# normal reload(), but deep_reload will still be available as dreload().
# c.TerminalInteractiveShell.deep_reload = False

# Set to confirm when you try to exit IPython with an EOF (Control-D in Unix,
# Control-Z/Enter in Windows). By typing 'exit' or 'quit', you can force a
# direct exit without any confirmation.
# c.TerminalInteractiveShell.confirm_exit = True

# 
# c.TerminalInteractiveShell.wildcards_case_sensitive = True

# 
# c.TerminalInteractiveShell.separate_out2 = ''

# Deprecated, use PromptManager.in2_template
# c.TerminalInteractiveShell.prompt_in2 = '   .\\D.: '

# Don't call post-execute functions that have failed in the past.
# c.TerminalInteractiveShell.disable_failing_post_execute = False

# 
# c.TerminalInteractiveShell.object_info_string_level = 0

# The part of the banner to be printed before the profile
# c.TerminalInteractiveShell.banner1 = 'Python 3.4.0+ (default, Apr 30 2014, 15:28:06) \nType "copyright", "credits" or "license" for more information.\n\nIPython 2.0.0 -- An enhanced Interactive Python.\n?         -> Introduction and overview of IPython\'s features.\n%quickref -> Quick reference.\nhelp      -> Python\'s own help system.\nobject?   -> Details about \'object\', use \'object??\' for extra details.\n'

# Deprecated, use PromptManager.justify
# c.TerminalInteractiveShell.prompts_pad_left = True

# 
# c.TerminalInteractiveShell.readline_remove_delims = '-/~'

# The shell program to be used for paging.
# c.TerminalInteractiveShell.pager = 'less'

# Make IPython automatically call any callable object even if you didn't type
# explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
# The value can be '0' to disable the feature, '1' for 'smart' autocall, where
# it is not applied if there are no more arguments on the line, and '2' for
# 'full' autocall, where all callable objects are automatically called (even if
# no arguments are present).
# c.TerminalInteractiveShell.autocall = 0

# 
# c.TerminalInteractiveShell.debug = False

# The part of the banner to be printed after the profile
# c.TerminalInteractiveShell.banner2 = ''

# 
# c.TerminalInteractiveShell.ipython_dir = ''

# 
# c.TerminalInteractiveShell.separate_in = '\n'

# A list of ast.NodeTransformer subclass instances, which will be applied to
# user input before code is run.
# c.TerminalInteractiveShell.ast_transformers = []

# 
# c.TerminalInteractiveShell.separate_out = ''

# auto editing of files with syntax errors.
# c.TerminalInteractiveShell.autoedit_syntax = False

# 
# c.TerminalInteractiveShell.readline_use = True

# Start logging to the given file in append mode.
# c.TerminalInteractiveShell.logappend = ''

# Set the size of the output cache.  The default is 1000, you can change it
# permanently in your config file.  Setting it to 0 completely disables the
# caching system, and the minimum value accepted is 20 (if you provide a value
# less than 20, it is reset to 0 and a warning is issued).  This limit is
# defined because otherwise you'll spend more time re-flushing a too small cache
# than working
# c.TerminalInteractiveShell.cache_size = 1000

# Deprecated, use PromptManager.in_template
# c.TerminalInteractiveShell.prompt_in1 = 'In [\\#]: '

# 
# c.TerminalInteractiveShell.xmode = 'Context'

# Autoindent IPython code entered interactively.
# c.TerminalInteractiveShell.autoindent = True

# Automatically call the pdb debugger after every exception.
# c.TerminalInteractiveShell.pdb = False

# Enable auto setting the terminal title.
# c.TerminalInteractiveShell.term_title = False

# Deprecated, use PromptManager.out_template
# c.TerminalInteractiveShell.prompt_out = 'Out[\\#]: '

# Number of lines of your screen, used to control printing of very long strings.
# Strings longer than this number of lines will be sent through a pager instead
# of directly printed.  The default value for this is 0, which means IPython
# will auto-detect your screen size every time it needs to print certain
# potentially long strings (this doesn't change the behavior of the 'print'
# keyword, it's only triggered internally). If for some reason this isn't
# working well (it needs curses support), specify it yourself. Otherwise don't
# change the default.
# c.TerminalInteractiveShell.screen_length = 0

# The name of the logfile to use.
# c.TerminalInteractiveShell.logfile = ''

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.TerminalInteractiveShell.color_info = True

# Save multi-line entries as one entry in readline history
# c.TerminalInteractiveShell.multiline_history = True

# 
# c.TerminalInteractiveShell.quiet = False

# Set the editor used by IPython (default to $EDITOR/vi/notepad).
# c.TerminalInteractiveShell.editor = 'vim'

# Show rewritten input, e.g. for autocall.
# c.TerminalInteractiveShell.show_rewritten_input = True

#------------------------------------------------------------------------------
# PromptManager configuration
#------------------------------------------------------------------------------

# This is the primary interface for producing IPython's prompts.

# Input prompt.  '\#' will be transformed to the prompt number
# c.PromptManager.in_template = 'In [\\#]: '

# If True (default), each prompt will be right-aligned with the preceding one.
# c.PromptManager.justify = True

# Continuation prompt.
# c.PromptManager.in2_template = '   .\\D.: '

# Output prompt. '\#' will be transformed to the prompt number
# c.PromptManager.out_template = 'Out[\\#]: '

# 
# c.PromptManager.color_scheme = 'Linux'

#------------------------------------------------------------------------------
# HistoryManager configuration
#------------------------------------------------------------------------------

# A class to organize all history-related functionality in one place.

# HistoryManager will inherit config from: HistoryAccessor

# Path to file to use for SQLite history database.
# 
# By default, IPython will put the history database in the IPython profile
# directory.  If you would rather share one history among profiles, you can set
# this value in each, so that they are consistent.
# 
# Due to an issue with fcntl, SQLite is known to misbehave on some NFS mounts.
# If you see IPython hanging, try setting this to something on a local disk,
# e.g::
# 
#     ipython --HistoryManager.hist_file=/tmp/ipython_hist.sqlite
# c.HistoryManager.hist_file = ''

# Options for configuring the SQLite connection
# 
# These options are passed as keyword args to sqlite3.connect when establishing
# database conenctions.
# c.HistoryManager.connection_options = {}

# Should the history database include output? (default: no)
# c.HistoryManager.db_log_output = False

# Write to database every x commands (higher values save disk access & power).
# Values of 1 or less effectively disable caching.
# c.HistoryManager.db_cache_size = 0

# enable the SQLite history
# 
# set enabled=False to disable the SQLite history, in which case there will be
# no stored history, no SQLite connection, and no background saving thread.
# This may be necessary in some threaded environments where IPython is embedded.
# c.HistoryManager.enabled = True

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = ''

#------------------------------------------------------------------------------
# PlainTextFormatter configuration
#------------------------------------------------------------------------------

# The default pretty-printer.
# 
# This uses :mod:`IPython.lib.pretty` to compute the format data of the object.
# If the object cannot be pretty printed, :func:`repr` is used. See the
# documentation of :mod:`IPython.lib.pretty` for details on how to write pretty
# printers.  Here is a simple example::
# 
#     def dtype_pprinter(obj, p, cycle):
#         if cycle:
#             return p.text('dtype(...)')
#         if hasattr(obj, 'fields'):
#             if obj.fields is None:
#                 p.text(repr(obj))
#             else:
#                 p.begin_group(7, 'dtype([')
#                 for i, field in enumerate(obj.descr):
#                     if i > 0:
#                         p.text(',')
#                         p.breakable()
#                     p.pretty(field)
#                 p.end_group(7, '])')

# PlainTextFormatter will inherit config from: BaseFormatter

# 
# c.PlainTextFormatter.max_width = 79

# 
# c.PlainTextFormatter.float_precision = ''

# 
# c.PlainTextFormatter.verbose = False

# 
# c.PlainTextFormatter.deferred_printers = {}

# 
# c.PlainTextFormatter.pprint = True

# 
# c.PlainTextFormatter.type_printers = {}

# 
# c.PlainTextFormatter.singleton_printers = {}

# 
# c.PlainTextFormatter.newline = '\n'

#------------------------------------------------------------------------------
# IPCompleter configuration
#------------------------------------------------------------------------------

# Extension of the completer class with IPython-specific features

# IPCompleter will inherit config from: Completer

# Activate greedy completion
# 
# This will enable completion on elements of lists, results of function calls,
# etc., but can be unsafe because the code is actually evaluated on TAB.
# c.IPCompleter.greedy = False

# Instruct the completer to omit private method names
# 
# Specifically, when completing on ``object.<tab>``.
# 
# When 2 [default]: all names that start with '_' will be excluded.
# 
# When 1: all 'magic' names (``__foo__``) will be excluded.
# 
# When 0: nothing will be excluded.
# c.IPCompleter.omit__names = 2

# Whether to merge completion results into a single list
# 
# If False, only the completion results from the first non-empty completer will
# be returned.
# c.IPCompleter.merge_completions = True

# Instruct the completer to use __all__ for the completion
# 
# Specifically, when completing on ``object.<tab>``.
# 
# When True: only those names in obj.__all__ will be included.
# 
# When False [default]: the __all__ attribute is ignored
# c.IPCompleter.limit_to__all__ = False

#------------------------------------------------------------------------------
# ScriptMagics configuration
#------------------------------------------------------------------------------

# Magics for talking to scripts
# 
# This defines a base `%%script` cell magic for running a cell with a program in
# a subprocess, and registers a few top-level magics that call %%script with
# common interpreters.

# Dict mapping short 'ruby' names to full paths, such as '/opt/secret/bin/ruby'
# 
# Only necessary for items in script_magics where the default path will not find
# the right interpreter.
# c.ScriptMagics.script_paths = {}

# Extra script cell magics to define
# 
# This generates simple wrappers of `%%script foo` as `%%foo`.
# 
# If you want to add script magics that aren't on your path, specify them in
# script_paths
# c.ScriptMagics.script_magics = []

#------------------------------------------------------------------------------
# StoreMagics configuration
#------------------------------------------------------------------------------

# Lightweight persistence for python variables.
# 
# Provides the %store magic.

# If True, any %store-d variables will be automatically restored when IPython
# starts.
# c.StoreMagics.autorestore = False