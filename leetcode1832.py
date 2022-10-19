class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return (
            True
            if re.fullmatch(r'[a-z]*', sentence) and len(Counter(sentence)) == 26
            else False
        )
