#include "algorithm.h"
string to_morse(string s){
    string ans;
    for (unsigned i = 0; i < s.size(); i++){
        if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i]>='a' && s[i]<='z')){
            ans += dictio.at(tolower(s[i])) + '/';

        }
        else ans+=s[i];
    }
    return ans;
}
