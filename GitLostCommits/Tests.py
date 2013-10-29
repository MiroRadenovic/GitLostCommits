import unittest
from GitLostCommits import *

class Tests(unittest.TestCase):
    """description of class"""

    def test_create_commit_list_from_string(self):
        inputStr =  """
                    36de53f Fixed: NX-1373 Create CteInjectionDataRequestDto Test with more cases
                    af09038 Fixed: NX-1372 AthenaDtoAdaptor ConvertEvent AddtionalData Null Check
                    56cb77d Fixed: NX-1326 add stress runner xml files to repo
                    """
        result = create_commit_list_from_string(inputStr)
        self.assertTrue(len(result) == 3)

    def test_get_missing_commits(self):
        sourceCommitList = [
                            Commit('NX-001', 'sha1', 'message'),
                            Commit('NX-002', 'sha2', 'message2'),
                            Commit('NX-003', 'sha3', 'message3')
                            ]

        targetCommitList = [
                            Commit('NX-001', 'sha1', 'message'),
                            Commit('NX-003', 'sha3', 'message3'),
                            Commit('NX-004', 'sha4', 'message4')
                            ]

        result = get_missing_commits(sourceCommitList,targetCommitList)
        self.assertTrue(len(result) == 1)
        self.assertTrue((result[0].taskId == 'NX-002'))

    def test_commits_are_equal(self):
        com1 = Commit('NX-001', 'sha1', 'message')
        com2 = Commit('NX-001', 'sha2', 'message2')
        com3 = Commit('NX-002', 'sha3', 'message3')

        self.assertEqual(com1, com2)
        self.assertTrue(com1 != com3)
        self.assertTrue(com2 != com3)
    

if __name__ == '__main__':
    unittest.main()