# install: pip3 install camelcase
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))

#######


def willThrowError():
    print("This function will throw error ...")
    raise Exception("An Exception for test")


try:
    print("Trying ...")
    willThrowError()
except Exception as ex:
    print("Exception ...")
    print(str(ex))
finally:
    print("Exitted!")
