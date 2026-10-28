struct TrieNode {
    children: HashMap<char, TrieNode>,
    is_end: bool,
}

impl TrieNode {
    pub fn new(is_end: bool) -> Self {
        Self {
            children: HashMap::new(),
            is_end,
        }
    }
}

struct PrefixTree {
    root: TrieNode,
}

impl PrefixTree {
    pub fn new() -> Self {
        Self { root: TrieNode::new(false) }
    }

    pub fn insert(&mut self, word: String) {
        let mut node = &mut self.root;
        for ch in word.chars() {
            node = node.children.entry(ch).or_insert(TrieNode::new(false));
        }
        node.is_end = true;
    }

    pub fn search(&self, word: String) -> bool {
        let mut curr = &self.root;
        for ch in word.chars() {
            match curr.children.get(&ch) {
                Some(child) => {
                    curr = child;
                }
                None => return false
            }
        }
        curr.is_end
    }

    pub fn starts_with(&self, prefix: String) -> bool {
        let mut curr = &self.root;
        for ch in prefix.chars() {
            match curr.children.get(&ch) {
                Some(child) => {
                    curr = child;
                }
                None => return false
            }
        }
        true
    }
}