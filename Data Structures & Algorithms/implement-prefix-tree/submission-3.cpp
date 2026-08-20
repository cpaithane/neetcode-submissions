#define MAX_CHARS 26
typedef struct TrieNode {
    bool ends[MAX_CHARS];
    char ch[MAX_CHARS];
    struct TrieNode *children[MAX_CHARS];
} TrieNode_t;

class PrefixTree {
private:
    TrieNode_t *root;

public:
    void init(TrieNode_t *node) {
        for (int i = 0; i < MAX_CHARS; i++) {
            node->ch[i] = (char)(i + 'a');
            node->children[i] = nullptr;
            node->ends[i] = false;
        }
    }

    PrefixTree() {
        root = new TrieNode();
        init(root);
    }
    
    ~PrefixTree() {}

    void insert(string word) {
        TrieNode_t *node = root;
        int idx = 0;

        for (char &ch : word) {
            idx = (int) (ch - 'a');

            if (node->children[idx] == nullptr) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->ends[idx] = true;
    }
    
    bool search(string word) {
        TrieNode_t *node = root;
        int idx = 0;

        for (char &ch : word) {
            idx = (int) (ch - 'a');

            if (node->children[idx] == nullptr) {
                return false;
            } else {
                node = node->children[idx];
            }
        }

        return node->ends[idx];
    }
    
    bool startsWith(string prefix) {
        TrieNode_t *node = root;
        int idx = 0;

        for (char &ch : prefix) {
            idx = (int) (ch - 'a');

            if (node->children[idx] == nullptr) {
                return false;
            } else {
                node = node->children[idx];
            }
        }

        return true;        
    }
};
