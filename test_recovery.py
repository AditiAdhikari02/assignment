import unittest
import os
import shutil
from tempfile import TemporaryDirectory
from recovery import FileRecovery, FolderRecovery  # Assuming the main code is in `recovery.py`

class TestFileRecovery(unittest.TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.source_file = os.path.join(self.test_dir.name, 'source.txt')
        self.destination_file = os.path.join(self.test_dir.name, 'destination.txt')
        
        with open(self.source_file, 'w') as f:
            f.write('Test data')

    def tearDown(self):
        self.test_dir.cleanup()

    def test_recover_file(self):
        recovery = FileRecovery(self.source_file, self.destination_file)
        recovery.recover()
        self.assertTrue(os.path.isfile(self.destination_file))
        with open(self.destination_file, 'r') as f:
            data = f.read()
        self.assertEqual(data, 'Test data')

    def test_file_not_found(self):
        invalid_file = os.path.join(self.test_dir.name, 'invalid.txt')
        recovery = FileRecovery(invalid_file, self.destination_file)
        with self.assertRaises(FileNotFoundError):
            recovery.recover()

class TestFolderRecovery(unittest.TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.source_folder = os.path.join(self.test_dir.name, 'source_folder')
        self.destination_folder = os.path.join(self.test_dir.name, 'destination_folder')
        os.makedirs(self.source_folder)
        
        with open(os.path.join(self.source_folder, 'file1.txt'), 'w') as f:
            f.write('File 1 data')
        with open(os.path.join(self.source_folder, 'file2.txt'), 'w') as f:
            f.write('File 2 data')

    def tearDown(self):
        self.test_dir.cleanup()

    def test_recover_folder(self):
        recovery = FolderRecovery(self.source_folder, self.destination_folder)
        recovery.recover()
        for item in os.listdir(self.source_folder):
            self.assertTrue(os.path.isfile(os.path.join(self.destination_folder, item)))
            with open(os.path.join(self.destination_folder, item), 'r') as f:
                data = f.read()
            self.assertEqual(data, f'File {item[-5]} data')

    def test_directory_not_found(self):
        invalid_folder = os.path.join(self.test_dir.name, 'invalid_folder')
        recovery = FolderRecovery(invalid_folder, self.destination_folder)
        with self.assertRaises(NotADirectoryError):
            recovery.recover()

if __name__ == '__main__':
    unittest.main()
