#!/usr/bin/env python

importos
importsys
defmain():
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','carretail.settings')
    try:
        fromdjango.core.managementimportexecute_from_command_line
    exceptImportErrorasexc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )fromexc
    execute_from_command_line(sys.argv)
if__name__=='__main__':
    main()
