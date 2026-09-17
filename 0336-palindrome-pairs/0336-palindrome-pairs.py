class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
        self.palindrome_suffix = []


class Solution:
    def palindromePairs(self, words):
        root = TrieNode()

        
        for i, word in enumerate(words):
            node = root

            for j in range(len(word) - 1, -1, -1):
                
                if word[:j + 1] == word[:j + 1][::-1]:
                    node.palindrome_suffix.append(i)

                ch = word[j]

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.index = i

        result = []

    
        for i, word in enumerate(words):
            node = root

            for j, ch in enumerate(word):
                
                if node.index != -1 and node.index != i:
                    if word[j:] == word[j:][::-1]:
                        result.append([i, node.index])

                if ch not in node.children:
                    break

                node = node.children[ch]

            else:
                
                for idx in node.palindrome_suffix:
                    if idx != i:
                        result.append([i, idx])

                if node.index != -1 and node.index != i:
                    result.append([i, node.index])

        return result