print("Output : ")
# Binary Types:	bytes, bytearray, memoryview
myBytes = b"BYTE"
print("Byte", type(myBytes), " value:", myBytes)

myBytes2 = b"1"
print("Byte2", type(myBytes2), " value:", myBytes2)

myByteArray = bytearray(11)
print("ByteArray", type(myByteArray), " value:", myByteArray)

# Remark Invalid Conversions
#myByteArray2 = bytearray("11")
#myByteArray3 = bytearray(2j)

myMemoryView = memoryview(bytes(11))
print("MemoryView", type(myMemoryView), " value:", myMemoryView)

myMemoryView2 = memoryview(b"aaa")
print("MemoryView2", type(myMemoryView2), " value:", myMemoryView2)
