#include <string>

#define MAX_CHARS 26

typedef struct TrieNode {
    char trie_chars[MAX_CHARS];
    bool ends[MAX_CHARS];
    TrieNode *children[MAX_CHARS];
} TrieNode;

class PrefixTree {
private:
    TrieNode *root;

public:
    void init(TrieNode *node) {
        for (int i = 0; i < MAX_CHARS; i++) {
            node->trie_chars[i] = (char) (i + 97);
            node->children[i] = NULL;
            node->ends[i] = false;
        }
        return;
    }

    PrefixTree() {
        root = new TrieNode();
        init(root);
    }
    
    void insert(string word) {
        TrieNode *tmp_root = root;
        int i = 0;
        int len = word.size();
        int idx = (char)(word[0] - 97);

        while (i < len) {
            char ch = word[i];
            idx = (int) (ch - 97);
            if (tmp_root->children[idx] == NULL) {
                tmp_root->children[idx] = new TrieNode();
            }
            tmp_root = tmp_root->children[idx];
            i++;
        }
        tmp_root->ends[idx] = true;
        cout << endl;
    }
    
    bool search(string word) {
        TrieNode *tmp_root = root;
        int i = 0;
        int len = word.size();
        int idx = (char)(word[0] - 97);

        while (i < len) {
            char ch = word[i];
            idx = (int) (ch - 97);

            if (tmp_root->children[idx] != NULL) {
                tmp_root = tmp_root->children[idx];
            } else {
                return false;
            }
            i++;
        }

        return tmp_root->ends[idx];
    }
    
    bool startsWith(string prefix) {
        TrieNode *tmp_root = root;
        int i = 0;
        int len = prefix.size();

        while (i < len) {
            char ch = prefix[i];
            int idx = (int) (ch - 97);

            if (tmp_root->children[idx] != NULL) {
                tmp_root = tmp_root->children[idx];
            } else {
                return false;
            }
            i++;
        }
        return true;
    }
};
