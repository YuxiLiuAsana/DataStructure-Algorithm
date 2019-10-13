class Solution {
public:
    int myAtoi(string str) {
        int i;
        // get rid of space
        for(i = 0; i < str.size(); i ++){
            if(str[i] != ' ') break;
        }
        long ret = 0;
        int minusFlag = 1;
        if(i < str.size()){
            if(str[i] == '-') {minusFlag=-1; i++;}
            else if (str[i] == '+') i++;
        }
        while(i < str.size() && str[i] >='0' && str[i] <= '9'){
            ret *= 10;
            ret += (minusFlag) * (str[i]-'0');
            if(ret > INT_MAX){
                ret = INT_MAX;
                break;
            }
            if(ret < INT_MIN){
                ret = INT_MIN;
                break;
            }
             i++;
        }
        return ret;
        
    }
};
