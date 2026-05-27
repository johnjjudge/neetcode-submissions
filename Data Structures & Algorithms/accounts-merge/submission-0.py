class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #{name: [set, set, set]}
        seen = {}
        for account in accounts:
            if account[0] in seen:
                seen[account[0]].append(set(account[1:len(account)]))
            else:
                seen[account[0]] = [set(account[1:len(account)])]

        mergedAccounts = []
        for kv in seen:
            # check if there is over laps between the sets, if so consolidate
            sets = seen[kv]
            merged = []
            while sets:
                current, *rest = sets
                current = set(current)
                changed = True

                while changed:
                    changed = False
                    new_rest = []
                    for s in rest:
                        if current & s:      # overlap?
                            current |= s     # merge
                            changed = True
                        else:
                            new_rest.append(s)
                    rest = new_rest

                merged.append(current)
                sets = rest
            for setss in merged:
                mergedAccounts.append([kv] + sorted(list(setss)))
        return mergedAccounts
