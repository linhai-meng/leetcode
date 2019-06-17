
class Solution:
    def findSubstring(self, s: str, words):
        words_dict = dict()
        len_words = len(words)
        if len_words == 0:
            return []
   
        if len_words != 0:
            len_word = len(words[0])
        res = []
        if len(s) < len_words * len_word:
            return []
        for w in words:
            if w not in words_dict:
                words_dict[w] = 1
            else:
                words_dict[w] += 1
        for i in range(0, len(s)-(len_words*len_word)+1):
            l = i
            print(i)
            count = 0
            temp_dict = dict()
            while s[l:l+len_word] in words_dict and count <= len_words:
                if s[l:l+len_word] not in temp_dict:
                    temp_dict[s[l:l+len_word]] = 1
                elif words_dict[s[l:l+len_word]] > temp_dict[s[l:l+len_word]]:
                    temp_dict[s[l:l+len_word]] += 1
                else:
                    break
                count += 1
                l = l+len_word
            if count == len_words:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    str1 = ""

    str2 = []
    res = s.findSubstring(str1, str2)
    print(res)
