# You are asked to design a file system that allows you to create new paths and associate them with different values.

# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

# Implement the FileSystem class:

# bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
# int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.


# Example 1:

# Input:
# ["FileSystem","createPath","get"]
# [[],["/a",1],["/a"]]
# Output:
# [null,true,1]
# Explanation:
# FileSystem fileSystem = new FileSystem();

# fileSystem.createPath("/a", 1); // return true
# fileSystem.get("/a"); // return 1
# Example 2:

# Input:
# ["FileSystem","createPath","createPath","get","createPath","get"]
# [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
# Output:
# [null,true,true,2,false,-1]
# Explanation:
# FileSystem fileSystem = new FileSystem();

# fileSystem.createPath("/leet", 1); // return true
# fileSystem.createPath("/leet/code", 2); // return true
# fileSystem.get("/leet/code"); // return 2
# fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
# fileSystem.get("/c"); // return -1 because this path doesn't exist.


# Constraints:

# 2 <= path.length <= 100
# 1 <= value <= 109
# Each path is valid and consists of lowercase English letters and '/'.
# At most 104 calls in total will be made to createPath and get
#
#
# Initial Thoughts/Clarifying Questions:
# Do these values for the given path is always unique? What if I try to create a path that exist but with a different value?
# Do we support empty paths or just a root path?
#
# Approach: We can use a dictinory to map the path to it's value. Each new path will directly stored as the key with it's associate value
#
#
# TC: Both createPath() and get() methods will take O(1) operation
# SC: O(no of createPath calls amortized)



class FileSystem:
    def __init__(self):
        self.file_map: dict = {}

    def createPath(self, path: str, value: int) -> bool:

        if not self._isValidPath(path): return False #Invalid Paths
        if self._isPathExist(path): return False # Path already exists

        parent_path = self._compute_parent_path(path)

        # Parent Path does not exists
        if parent_path != "/" and not self._isPathExist(parent_path): return False

        self.file_map[path] = value
        return True

    def get(self, path) -> int:
        if not self._isPathExist(path): return -1 #Path does not exists
        return self.file_map[path]

    def _isValidPath(self, path: str):
        if path == "" or path == "/" : return False
        if path[0] != "/": return False
        return True

    def _compute_parent_path(self, path) -> str:
        i =  path.rfind("/")
        if i == 0:
            return "/"
        return path[:i]


    def _isPathExist(self, path: str):
        return path in self.file_map


def main():

    file_obj = FileSystem()
    got = file_obj.createPath("/a", 1)
    assert got == True, f"expected: {True}, got: {got}"
    assert file_obj.get("/a") == 1

    file_obj_1 = FileSystem()
    assert file_obj_1.createPath("/leet", 1) == True
    assert file_obj_1.createPath("/leet/code", 2) == True
    assert file_obj_1.get("/leet") == 1
    assert file_obj_1.get("/leet/code") == 2
    assert file_obj_1.createPath("/c/d", 3) == False
    assert file_obj_1.get("/c") == -1
    assert file_obj_1.createPath("c/d", 4) == False

    print("All tests passed")

if __name__ == "__main__":
    main()
