from django.core.management.base import BaseCommand, CommandError
from django.core import management
import subprocess
import os
from optparse import make_option
import south.logger
import logging
logging.getLogger('south').setLevel(logging.CRITICAL)

import settings as production_settings
from settings import development as development_settings

cwd = os.getcwd()


class Command(BaseCommand):
    help = 'Dump data from the remote production database and load it up locally'
    
    remote = 'ledgerapp@ledgerapp.cc'
    production_database_name = 'ledgerapp_production'
    development_database_name = 'ledgerapp_development'
    database_dump = os.path.join(development_settings.TMP_ROOT, '%s_dump.sql' % production_database_name)
    
    def handle(self, *args, **options):
        self.stdout.write('Dumping and downloading production database:\n')
        cmd = "touch %s && ssh %s 'pg_dump %s' > %s" % (
            self.database_dump,
            self.remote,
            self.production_database_name,
            self.database_dump
        )
        retcode = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
        self.stdout.write(' - done!')
        
        self.stdout.write('\n\n')
        
        self.stdout.write('Preparing database:\n')
        self.stdout.write(' - ')
        self.stdout.write('reset_db, ')
        management.call_command('reset_db', verbosity=0, interactive=False, router='default')
        self.stdout.write('syncdb, ')
        management.call_command('syncdb', verbosity=0, interactive=False, no_input=True)
        self.stdout.write('migrate, ')
        management.call_command('migrate', verbosity=0, interactive=False)
        self.stdout.write('flush')
        management.call_command('flush', verbosity=0, interactive=False, no_input=True)
        self.stdout.write('\n - done!')
        
        self.stdout.write('\n\n')
        
        self.stdout.write('Importing live data:\n')
        cmd = "psql -U `whoami` -d %s < %s" % (self.development_database_name, self.database_dump)
        self.stdout.write(' - %s\n' % cmd)
        retcode = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
        self.stdout.write(' - done!')
        
        self.stdout.write('\n\n')
        
        self.stdout.write('Resetting all user passwords to "test123":\n')
        from django.contrib.auth.models import User
        for user in User.objects.all():
            user = user.set_password('test123')
            user.save()
        self.stdout.write(' - done!')
        self.stdout.write('\n\n')
        