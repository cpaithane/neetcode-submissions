
typedef struct TrieNode {
    bool ends;
    unordered_map<char, TrieNode *> children;

    TrieNode() {
        ends = false;
    }

} TrieNode;

class WordDictionary {
private:
    TrieNode *root;

public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode *root = this->root;

        for (char ch : word) {
            if (root->children[ch] == nullptr) {
                root->children[ch] = new TrieNode();
            }
            root = root->children[ch];
        }

        root->ends = true;
    }

    bool search_core(TrieNode *root, string word, int idx) {
        for (int i = idx; i < word.size(); i++) {
            char ch = word[i];
            if (ch == '.') {
                for (auto &[key, child] : root->children) {
                    if (search_core(child, word, i + 1)) {
                        return true;
                    }
                }
                return false;
            } else {
                if (root->children.find(ch) == root->children.end()) {
                    return false;
                } else {
                    root = root->children[ch];
                }
            }
        }

        return root->ends;
    }

    bool search(string word) {
        return search_core(this->root, word, 0);        
    }
};
