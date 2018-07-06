# Tuesday: 
# 1.) time w/ perf_counter and O() in terms of length of string
# 2.) comment this code and other code
# 3.) skype

def lcs(a, b):
    if a == "" or b == "":
        return 0
    if a[0] == b[0]:
        return lcs(a[1:], b[1:])+1
    else:
        return max(lcs(a[1:], b), lcs(a, b[1:]))


already_computed = {}
def lcs_memoized(a, b):
    if (a, b) in already_computed:
        return already_computed[(a, b)]
    else:
        if a == "" or b == "":
            already_computed[(a, b)] = 0
            return already_computed[(a, b)]
        if a[0] == b[0]:
            already_computed[(a, b)] = lcs_memoized(a[1:], b[1:])+1
            return already_computed[(a, b)] 
        else:
            already_computed[(a, b)] = max(lcs_memoized(a[1:], b), lcs_memoized(a, b[1:]))
            return already_computed[(a, b)]
