TXTMSG_directory = {
    "CU":	"see you",
    ":-)":	"I’m happy",
    ":-(":	"I’m unhappy",
    ";-)":	"wink",
    ":-P":	"stick out my tongue",
    "(~.~)":	"sleepy",
    "TA":	"totally awesome",
    "CCC":	"Canadian Computing Competition",
    "CUZ":	"because",
    "TY":	"thank-you",
    "YW":	"you’re welcome",
    "TTYL":	"talk to you later"
}

while True:
    text = input()
    if text in TXTMSG_directory:
        print(TXTMSG_directory[text])
    else:
        print(text)
    if text == 'TTYL':
        break