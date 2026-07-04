class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            while (!isalnum(s[i]) && i < j) {
                i++;
            }
            while (!isalnum(s[j]) && i < j) {
                j--;
            }
            if (tolower(s[i]) != tolower(s[j])) {
                cout << s[i] << s[j] << "\n";
                return false;
            }
            i++; j--;
        }
        return true;
    }
    bool isalnum(char s) {
        return (('A' <= s && s <= 'Z') || 
                ('a' <= s && s <= 'z') || 
                ('0' <= s && s <= '9'));
    }
};
