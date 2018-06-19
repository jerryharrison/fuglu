# -*- coding: UTF-8 -*-
import unittest
import sys
import email
from os.path import join
from fuglu.extensions.mailattach import MailAttachMgr
from unittestsetup import TESTDATADIR, CONFDIR

class FileArchiveBase(unittest.TestCase):
    def testMailAttachment(self):

        #tempfile = join(TESTDATADIR,"6mbrarattachment.eml")
        tempfile = join(TESTDATADIR,"nestedarchive.eml")

        if sys.version_info > (3,):
            # Python 3 and larger
            # file should be binary...

            # IMPORTANT: It is possible to use email.message_from_bytes BUT this will automatically replace
            #            '\r\n' in the message (_payload) by '\n' and the endtoend_test.py will fail!
            with open(tempfile, 'rb') as fh:
                source = fh.read()
            msgrep = email.message_from_bytes(source)
        else:
            # Python 2.x
            with open(tempfile, 'r') as fh:
                msgrep = email.message_from_file(fh)
        mAttachMgr = MailAttachMgr(msgrep)
        print("Filenames, base   Level : [%s]"%", ".join(mAttachMgr.get_fileslist(0)))
        print("Filenames, first  Level : [%s]"%", ".join(mAttachMgr.get_fileslist(1)))
        print("Filenames, second Level : [%s]"%", ".join(mAttachMgr.get_fileslist(2)))
        print("Filenames, all    Levels: [%s]"%", ".join(mAttachMgr.get_fileslist()))

        print("\n")
        print("-------------------------------------")
        print("- Extract objects util second level -")
        print("-------------------------------------")
        secAttList = mAttachMgr.get_objectlist(2)
        for att in secAttList:
            print(att)

        print("\n")
        print("--------------------------------------------")
        print("- Extract objects until there's no archive -")
        print("--------------------------------------------")
        fullAttList = mAttachMgr.get_objectlist()
        for att in fullAttList:
            print(att)

