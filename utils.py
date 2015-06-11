"""here is my cool utility kitchen"""
import colors as c
def ask(question,color=c.yellow):
    print(color + question + c.reset)
    answer = input('> ' + c.cyan).lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    color = ask('what is your name in color' ,c.random_color())
    name = ask('what is your name')
