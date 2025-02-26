# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
from collections import defaultdict

class Master(object):
    def __init__(self, words, secret, allowedGuesses):
        self.words = [w for w in words]
        self.secret = secret
        self.guesses_allowed = allowedGuesses
        self.guesses_left = allowedGuesses
        self.guessed = False

    def num_guesses(self):
        return self.guesses_allowed - self.guesses_left

    def guess(self, word):
        if self.guesses_left == 0:
            raise Exception("Either you took too many guesses, or you did not find the secret word.")
        self.guesses_left -= 1
        if word == self.secret:
            self.guessed = True
            return len(self.secret)
        if word not in self.words:
            return -1
        return sum(ch1 == ch2 for ch1, ch2 in zip(self.secret, word))

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """

        attempts = 1
        blacklist = defaultdict(int)
        guesses = defaultdict(int)
        while len(words) > 0:
            word = words.pop()
            score = master.guess(word)
            guesses[word] = score

            print(f'Guess {attempts}: Master.guess({word}) = {score} (words {len(words)})')

            if score == 6:
                print(f' caught you, {word}!')
                return

            # all the letters in the word are in the wrong positions,
            # so we go through them and set the appropriate bits in
            # the bitmasks
            if score == 0:
                # mark invalid positions for the letters in their bitmasks
                for pos, ch in enumerate(word):
                    blacklist[ch] |= 1 << pos

                _words = []
                for word in words:
                    include_word = True
                    for pos, c in enumerate(word):
                        if c in blacklist and blacklist[c] & 1 << pos:
                            # word has a letter on the invalid position,
                            # so do not include it to the new list
                            include_word = False
                            break
                    if include_word:
                        _words.append(word)

                print(f' {len(words) - len(_words)} word(s) removed')
                words = _words

# https://leetcode.com/problems/guess-the-word/solutions/5081100/finding-best-next-guess-python/?envType=problem-list-v2&envId=game-theory
            # The best next candidate word will have to also give similarity scores
            # equal to those that have been guessed before in guesses. Therefore, we
            # iterate through all the remaining words in words and try to see if they
            # produce the similar scores to all words in guesses.
            for w in range(len(words)):
                matches = 0
                for guess, score in guesses.items():
                    # count the number of letters occupying the same positions
                    count = sum(ch1 == ch2 for ch1, ch2 in zip(guess, words[w]))
                    # count the number of matches in the score with already
                    # guessed words 
                    matches += count == score

                if matches == len(guesses):
                    # put possible candidate word at the end of the list
                    temp = words[w]
                    words[w] = words[-1]
                    words[-1] = temp
                    break

            attempts += 1

vectors = [
        ["acckzz", "ccbazz", "eiowzz", "abcczz"], "acckzz", 10,
        ["acckzz", "ccbazz", "eiowzz", "abcczz"], "abcczz", 10,
        ["acckzz", "ccbazz", "eiowzz", "abcczz", "aaaaaa"], "eiowzz", 10,
        ["hamada", "khaled"], "hamada", 10,
        ["hamada", "khaled"], "khaled", 10,
        ["xxxxxx", "abcdef", "ghijkl", "abywlp", "pkkgkd", "zyfjmk"], "xxxxxx", 10,
        ["aaaaaa", "bbbbbb", "cccccc", "dddddd", "eeeeee", "ffffff", \
                "gggggg", "hhhhhh", "iiiiii", "jjjjjj", "kkkkkk", "llllll", \
                "mmmmmm", "nnnnnn", "oooooo", "pppppp", "qqqqqq", "rrrrrr", \
                "ssssss", "tttttt", "uuuuuu", "vvvvvv", "wwwwww", "xxxxxx", \
                "yyyyyy", "zzzzzz"], "aaaaaa", 26,
        ["pzrooh", "aaakrw", "vgvkxb", "ilaumf", "snzsrz", "qymapx", \
                "hhjgwz", "mymxyu", "jglmrs", "yycsvl", "fuyzco", "ivfyfx",\
                "hzlhqt", "ansstc", "ujkfnr", "jrekmp", "himbkv", "tjztqw",\
                "jmcapu", "gwwwmd", "ffpond", "ytzssw", "afyjnp", "ttrfzi",\
                "xkwmsz", "oavtsf", "krwjwb", "bkgjcs", "vsigmc", "qhpxxt",\
                "apzrtt", "posjnv", "zlatkz", "zynlqc", "czajmi", "smmbhm",\
                "rvlxav", "wkytta", "dzkfer", "urajfh", "lsroct", "gihvuu",\
                "qtnlhu", "ucjgio", "xyycvd", "fsssoo", "kdtmux", "bxnppe",\
                "usucra", "hvsmau", "gstvvg", "ypueay", "qdlvod", "djfbgs",\
                "mcufib", "prohkc", "dsqgms", "eoasya", "kzplbv", "rcuevr",\
                "iwapqf", "ucqdac", "anqomr", "msztnf", "tppefv", "mplbgz",\
                "xnskvo", "euhxrh", "xrqxzw", "wraxvn", "zjhlou", "xwdvvl",\
                "dkbiys", "zbtnuv", "gxrhjh", "ctrczk", "iwylwn", "wefuhr",\
                "enlcrg", "eimtep", "xzvntq", "zvygyf", "tbzmzk", "xjptby",\
                "uxyacb", "mbalze", "bjosah", "ckojzr", "ihboso", "ogxylw",\
                "cfnatk", "zijwnl", "eczmmc", "uazfyo", "apywnl", "jiraqa",\
                "yjksyd", "mrpczo", "qqmhnb", "xxvsbx"], "anqomr", 11,\
        ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", \
                "ldzccp", "nqsjoa", "qrjasy", "pcldos", "acrtag", "buyeia",\
                "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw",\
                "evtkhl", "bhpfla", "ymqhxk", "qkvipb", "tvmued", "rvbass",\
                "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc",\
                "tamszl", "osdifo", "dvxlxm", "iwmyfb", "wmnwhe", "hslnop",\
                "nkrfwn", "puvgve", "rqsqpq", "jwoswl", "tittgf", "evqsqe",\
                "aishiv", "pmwovj", "sorbte", "hbaczn", "coifed", "hrctvp",\
                "vkytbw", "dizcxz", "arabol", "uywurk", "ppywdo", "resfls",\
                "tmoliy", "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy",\
                "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg",\
                "egcdab", "cykndr", "lkzobv", "ifwmwp", "jqmbib", "mypnvf",\
                "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg", "sczjmz",\
                "hsdjfp", "mjcgvm", "ajotcx", "olgnfv", "mjyjxj", "wzgbmg",\
                "lpcnbj", "yjjlwn", "blrogv", "bdplzs", "oxblph", "twejel",\
                "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu",\
                "xgqpsr", "wxdyho", "alrplq", "brklfk"], "hbaczn", 10,\
        ["eykdft", "gjeixr", "eksbjm", "mxqhpk", "tjplhf", "ejgdra", \
                "npkysm", "jsrsid", "cymplm", "vegdgt", "jnhdvb", "jdhlzb",\
                "sgrghh", "jvydne", "laxvnm", "xbcliw", "emnfcw", "pyzdnq",\
                "vzqbuk", "gznrnn", "robxqx", "oadnrt", "kzwyuf", "ahlfab",\
                "zawvdf", "edhumz", "gkgiml", "wqqtla", "csamxn", "bisxbn",\
                "zwxbql", "euzpol", "mckltw", "bbnpsg", "ynqeqw", "uwvqcg",\
                "hegrnc", "rrqhbp", "tpfmlh", "wfgfbe", "tpvftd", "phspjr",\
                "apbhwb", "yjihwh", "zgspss", "pesnwj", "dchpxq", "axduwd",\
                "ropxqf", "gahkbq", "yxudiu", "dsvwry", "ecfkxn", "hmgflc",\
                "fdaowp", "hrixpl", "czkgyp", "mmqfao", "qkkqnz", "lkzaxu",\
                "cngmyn", "nmckcy", "alpcyy", "plcmts", "proitu", "tpzbok",\
                "vixjqn", "suwhab", "dqqkxg", "ynatlx", "wmbjxe", "hynjdf",\
                "xtcavp", "avjjjj", "fmclkd", "ngxcal", "neyvpq", "cwcdhi",\
                "cfanhh", "ruvdsa", "pvzfyx", "hmdmtx", "pepbsy", "tgpnql",\
                "zhuqlj", "tdrsfx", "xxxyle", "zqwazc", "hsukcb", "aqtdvn",\
                "zxbxps", "wziidg", "tsuxvr", "florrj", "rpuorf", "jzckev",\
                "qecnsc", "rrjdyh", "zjtdaw", "dknezk"], "cymplm", 15,
        ["oahwep", "eqznzs", "vvmplb", "dqefpt", "kmjmxr", "ihkovg", \
                "trbzyb", "xqulhc", "bcsbfw", "rwzslk", "abpjhw", "mpubps",\
                "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo",\
                "awvqlr", "uooeon", "sajxgr", "oxgaix", "fnugyu", "lkxwru",\
                "mhtrvb", "xxonmg", "hhfuzz", "tqxlbr", "euxtzg", "tjwvad",\
                "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm", "uinqur",\
                "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn", "kmbeok",\
                "biywow", "wichbx", "tpulot", "hwzodo", "loffxk", "xavzqd",\
                "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa", "kqbttl",\
                "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv",\
                "rpbdjh", "wynohw", "lhqxvx", "kaaaaa", "dxxwut", "vjtskm",\
                "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu",\
                "wrrpoc", "khuopg", "ooxarg", "vcvfry", "thaawc", "bssybb",\
                "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne",\
                "swcrkh", "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp",\
                "xfnayl", "ccoyyo", "eywinm", "ktgmfn", "xrmzzm", "fgtuki",\
                "zcffuv", "srxuus", "pydgmq"], "ccoyyo", 10
        ]


all_guesses = 0
for i in range(0, len(vectors), 3):
    words = vectors[i]
    secret = vectors[i + 1]
    guesses = vectors[i + 2]
    print(f'{words} {secret} {guesses}')
    master = Master(words, secret, guesses)
    Solution().findSecretWord(words, master)
    all_guesses += master.num_guesses()
    print('')
    assert master.guessed, f'for {words} you did not guess the secret!'
print(f'Total guesses: {all_guesses}')
