struct Node {
  int value;
  Node* next;
  Node(int value, Node* next) : value(value), next(next) {}
};

class LinkedList {
private:
    Node* head;
    int size;
public:
    LinkedList() {
        head = nullptr;
        size = 0;
    }

    int get(int index) {
        if (index > size - 1) return -1;
        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->value;
    }

    void insertHead(int val) {
        Node* insert_node = new Node(val, head);
        head = insert_node;
        size++;
    }
    
    void insertTail(int val) {
        if (size == 0) {
            head = new Node(val, nullptr);
            size++;
            return;
        }
        Node* curr = head;
        while (curr && curr->next) {
            curr = curr->next;
        }
        curr->next = new Node(val, nullptr);
        size++;
    }

    bool remove(int index) {
        if (index > size - 1) return false;

        Node* curr = head;
        Node* prev = nullptr;
        for (int i = 0; i < index; i++) {
            prev = curr;
            curr = curr->next;
        }
        if (prev == nullptr) {
            Node* tmp = head;
            head = head->next;
            delete tmp;
        } else {
            prev->next = curr->next;
            delete curr;
        }

        size--;
        return true;
    }

    vector<int> getValues() {
        vector<int> res;
        Node* curr = head;
        while (curr != nullptr) {
            res.push_back(curr->value);
            curr = curr->next;
        }
        return res;
    }
};
