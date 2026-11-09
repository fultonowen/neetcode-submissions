class TimeMap {
private:
    std::unordered_map<string, std::vector<std::pair<int, string>>> store;

public:
    TimeMap() {
        store = unordered_map<string, vector<pair<int, string>>>();
    }
    
    void set(string key, string value, int timestamp) {
        store[key].push_back(std::make_pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        if (!store.contains(key)) return "";
        int low{0}, mid;
        int high = store[key].size() - 1;

        while (low <= high) {
            mid = low + (high - low) / 2;
            if (store[key][mid].first > timestamp) high = mid - 1;
            else low = mid + 1;
        }
        if (high < 0) return "";
        return store[key][high].second;
    }
};
