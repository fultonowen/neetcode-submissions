class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = 0
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '').split('+')[0]
            seen.add(local + domain)
        return len(seen)
            
