struct TrieNode {
    std::unordered_map<char, TrieNode*> neighbors;
    bool is_end;
    TrieNode(bool is_end) : is_end(is_end), neighbors(std::unordered_map<char, TrieNode*>()) {}
};

class PrefixTree {
private:
    TrieNode* root;
public:
    PrefixTree() {
        root = new TrieNode(false);
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char letter: word) {
            if (!curr->neighbors.contains(letter)) {
                curr->neighbors[letter] = new TrieNode(false);
            }
            curr = curr->neighbors[letter];
        }
        curr->is_end = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char letter: word) {
            if (!curr->neighbors.contains(letter)) {
                return false;
            }
            curr = curr->neighbors[letter];
        }
        return curr->is_end;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char l: prefix) {
            if (!curr->neighbors.contains(l)) {
                return false;
            }
            curr = curr->neighbors[l];
        }
        return true;
    }
};
