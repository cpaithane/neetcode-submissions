class MinStack {
private:
    stack<pair<int, int>> st;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        int min = val;
        int v, m;
        pair<int, int> p;

        if (st.size() > 0) {
            p = st.top();
            v = p.first;
            m = p.second;
        }
        
        if (m < min) {
            min = m;
        }
        st.push({val, min});
    }
    
    void pop() {
        if (st.size() > 0) {
            st.pop();
        }
    }
    
    int top() {
        if (st.size() > 0) {
            auto [v, m] = st.top();
            return v;
        }
    }
    
    int getMin() {
        if (st.size() > 0) {
            auto [v, m] = st.top();
            return m;
        }        
    }
};
