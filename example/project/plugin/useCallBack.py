def testUseCallBack(itemId):
    return """println("ItemIns_%d count OnUse Callback")""" % (itemId)


callback = {
    9999: testUseCallBack
}
