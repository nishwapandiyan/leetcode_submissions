class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            local,domain = e.split("@")
            unique.add((local.split("+")[0].replace(".",""),domain))
        return len(unique)    