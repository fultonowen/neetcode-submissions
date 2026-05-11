class DynamicArray {
private:
    int* arr;
    int capacity;
    int count = 0;
public:
    DynamicArray(int capacity) : capacity(capacity) {
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (count >= capacity) {
            resize();
        }
        arr[count++] = n;
    }

    int popback() {
        int value = arr[count - 1];
        count--;
        return value;
    }

    void resize() {
        int* new_array = new int[capacity * 2];
        for (int i =0; i < count; i++) {
            new_array[i] = arr[i];
        }
        delete[] arr;
        arr = new_array;
        capacity *= 2;
    }

    int getSize() {
        return count;
    }

    int getCapacity() {
        return capacity;
    }
};
