__author__ = 'philroche'

#!/usr/bin/python
'''
pip install --allow-external eyed3 --allow-unverified eyed3 --upgrade eyed3
'''

import os
import sys
import getopt
import shutil
import eyed3
import eyed3.mp3

def main(argv):
   inputdirectory = '.'
   try:
      opts, args = getopt.getopt(argv,"hi:",["inputdirectory="])
   except getopt.GetoptError:
      print 'mp3TitleFromTrackNumber.py -i <inputdirectory>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputdirectory> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--inputdirectory"):
        inputdirectory = arg
        # traverse root directory, and list directories as dirs and files as files
        for root, dirs, files in os.walk(inputdirectory):

            files = [ fi for fi in files if fi.endswith(".mp3") ]

            for file in files:
                abs_mp3_path =  os.path.join(root, file)
                print abs_mp3_path
                if eyed3.mp3.isMp3File(abs_mp3_path):
                    audiofile = eyed3.load(abs_mp3_path)

                    audiofile.tag.title = u"Track %s" % audiofile.tag.track_num[0]
                    audiofile.tag.save()
                    new_file_name = '%s - %s.mp3' % (audiofile.tag.album, audiofile.tag.track_num[0])
                    new_file_name_abs_path = os.path.join(root, new_file_name)
                    print new_file_name_abs_path
                    shutil.copy(abs_mp3_path, new_file_name_abs_path)
                    os.remove(abs_mp3_path)



   print 'Input file is ', inputdirectory

if __name__ == "__main__":
   main(sys.argv[1:])