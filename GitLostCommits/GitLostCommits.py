'''
 to create the required commit lists use:
 git log --oneline --no-merges  v1.0.18.0..HEAD
'''


import re
import conf


regex_match_sha1 = '\b[0-9a-f]{5,40}\b' 


def main():
    sourceCommitList = create_commit_list_from_string(read_commit_list(conf.sourceCommitList))
    targetCommitList = create_commit_list_from_string(read_commit_list(conf.targetCommitList))

    print('Result is..')
    missingCommits = get_missing_commits(sourceCommitList, targetCommitList)
    print_commit_list(missingCommits)
    raw_input('press any key to quit')
    


def get_missing_commits(sourceCommitList, targetCommitList):
    result = []
    for commit in sourceCommitList:
        notFound = True
        for targetCommit in targetCommitList:
            if commit == targetCommit:
                notFound = False
                break
        if notFound: 
            result.append(commit)
    return result; 

def create_commit_list_from_string(str):
    result = []
    for line in str.split('\n'):
        line = line.strip()
        match = re.search(conf.regex_match_task_id, line)
        if match:
            taskid = match.group()
            sha1 = line[0:7]
            result.append(Commit(taskid, sha1, line[8:len(line)]))
    return result

def read_commit_list(path):
    result = ''
    with open (path, "r") as myfile:
        result=myfile.read()
    return result

def print_commit_list(commitList):
    for commit in commitList:
        print('{sha1}\t{taskid}\t{message}'.format(sha1 = commit.commitSha, taskid=commit.taskId, message = commit.commitMessage ))


class Commit():
    '''
    represents a commit identified by taskid
    '''
    def __init__(self, taskId, commitSha, commitMessage):
        self.taskId = taskId
        self.commitSha = commitSha
        self.commitMessage = commitMessage

    def __eq__(self, other):
         return self.taskId == other.taskId

if __name__ == '__main__':
    main()




