class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        while command:
            if command.startswith("G"):
                ans += "G"
                command = command[1:]
            
            elif command.startswith("()"):
                ans += "o"
                command = command[2:]
            
            elif command.startswith("(al)"):
                ans += "al"
                command = command[4:]
        return ans