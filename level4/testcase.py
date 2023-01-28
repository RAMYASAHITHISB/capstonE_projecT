import pytest
from level1.findfile import FileFinder
from level1.find_drives import SystemDriverFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriverFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual

    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','C:\hcl')
        self.expected_filename=d[0]
        self.actual_res='C:\\hcl\\demo.txt'
        assert self.expected_filename==self.actual_res







