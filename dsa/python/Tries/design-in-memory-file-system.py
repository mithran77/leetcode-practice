# 588. Design In-Memory File System

# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

#     FileSystem() Initializes the object of the system.
#     List<String> ls(String path)
#         If path is a file path, returns a list that only contains this file's name.
#         If path is a directory path, returns the list of file and directory names in this directory.
#     The answer should in lexicographic order.
#     void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist.
#     If the middle directories in the path do not exist, you should create them as well.
#     void addContentToFile(String filePath, String content)
#         If filePath does not exist, creates that file containing given content.
#         If filePath already exists, appends the given content to original content.
#     String readContentFromFile(String filePath) Returns the content in the file at filePath.

# Example 1:
# Input
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
# Output
# [null, [], null, null, ["a"], "hello"]

# Explanation
# FileSystem fileSystem = new FileSystem();
# fileSystem.ls("/");                         // return []
# fileSystem.mkdir("/a/b/c");
# fileSystem.addContentToFile("/a/b/c/d", "hello");
# fileSystem.ls("/");                         // return ["a"]
# fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

# Constraints:
# 1 <= path.length, filePath.length <= 100
# path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
# You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
# You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a
# directory or file that does not exist.
# You can assume that the parent directory for the file in addContentToFile will exist.
# 1 <= content.length <= 50
# At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.

# preddy
from collections import defaultdict
import bisect
from typing import List

class FileSystem:

    def __init__(self):
        self.paths = defaultdict(list) # <path: [File|Folder]>
        self.files = defaultdict(str) # <path: content>

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split('/')[-1]]
        else:
            return self.paths[path]

    def mkdir(self, path: str) -> None:
        directories = path.split('/')

        for i in range(1, len(directories)):
            # Parent dir
            if directories[:i] == ['']:
                cur = '/'
            else:
                cur = '/'.join(directories[:i])

            if cur not in self.paths or directories[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur], directories[i])


    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)

        # Add content
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]

# Time  : 
# ls: O(F) -> F is length of filepath
# mkdir: O(log(P) * P) * O(F) -> P = # of items at paths[path] & F is length of filepath
# addContentToFile: (log(P) * P) * O(F)
# readContentFromFile: O(1)

# Space : O(P) + O(F) P = number of files and directories, F = File contents


