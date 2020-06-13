def balanced_check(exp):
    stack=[]
    result="balanced"
    for i in range(len(exp)):
        if exp[i]=='[' or exp[i]=='{' or exp[i]=='(':
            stack.append(exp[i])
        elif exp[i]==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                result="unbalanced"
                break
        elif exp[i]=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
                result="unbalanced"
                break
        elif exp[i]==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                result="unbalanced"
                break
    if len(stack)!=0:
        result="unbalanced"
    return result

exps=["[()]{}{[()()]()}","[(])"]
for exp in exps:
    print(balanced_check(exp))