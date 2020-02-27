import deepcut

def main(Text) :

    Words = deepcut.tokenize(Text)

    ListofCharacter = ["ข", "ฃ", "ฉ", "ฐ", "ถ", "ผ", "ฝ", "ศ", "ษ", "ส", "ห", "ก", "จ", "ฎ", "ฏ", "ด", "ต", "บ", "ป", "อ", "ค", "ฅ", "ฆ", "ง", "ช", "ซ", "ฌ", "ญ", "ฑ", "ฒ", "ณ", "ท", "ธ", "น", "พ", "ฟ", "ภ", "ม", "ย", "ร", "ล", "ว", "ฬ", "ฮ"]

    Count = 0
    CountWord = 0

    ListofReplace = []

    WordsOutput = []

    for i in Words :

        for i in Words[Count] :

            for i in Words[Count][CountWord] :

                if Words[Count][CountWord] in ListofCharacter :
                    
                    ListofReplace.append(CountWord)

            CountWord = CountWord + 1

        Output = Words[Count][0 : min(ListofReplace)] + "ล" + Words[Count][min(ListofReplace) + 1 :] + Words[Count][min(ListofReplace)] + "ู"

        WordsOutput.append(Output)

        ListofReplace = []
        CountWord = 0
        Count = Count + 1

    print({"input" : Words, "Output" : WordsOutput})

    return({"input" : Words, "Output" : WordsOutput})

main(input())