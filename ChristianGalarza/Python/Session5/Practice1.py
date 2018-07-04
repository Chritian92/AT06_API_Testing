class StoreSms:
    has_been_viewed = False
    inboxList = []
    indexList = []

    def add_new_sms(self, from_number, time_arrived, text_of_SMS):
        self.add = (from_number, time_arrived, text_of_SMS, self.has_been_viewed)
        self.inboxList.append(self.add)
        return self.inboxList

    def get_unread_indexes(self):
        for i in range(0, len(self.inboxList)):
            if self.inboxList[i][3] == False:
                self.indexList.append(i)
        return self.indexList

    def message_legth(self):
        return len(self.inboxList)

    def get_message(self, i):
        for j in self.inboxList:
            if self.inboxList[i] == j:
                j = list(j)
                j[3] = True
                self.inboxList[i] = tuple(j)
                print(j)
                if j[3] == True:
                    return "Message Viewed" + "\nFrom:" + str(j[0]) + "\n Time:" + str(j[1]) + "\n Text: \t" + str(j[2])
            elif i > len(self.inboxList) or i < 0:
                return None

    def delete(self, i):
        del self.inboxList[i]
        print("The message {} was deleted".format(i))

    def clear(self):
        del self.inboxList[::]
        print("The list of messages was deleted")


my_inbox = StoreSms()
my_inbox.add_new_sms("65324310", "14:00", "Hello, how are you?")
my_inbox.add_new_sms("71234567", "23:19", "where are you?")
my_inbox.add_new_sms("79876543", "08:05", "goodbye, don't forget to buy eggs")
print(my_inbox.get_message(0))
print(my_inbox.get_message(1))
print(my_inbox.get_unread_indexes())
print(my_inbox.message_legth())
my_inbox.delete(1)
print(my_inbox.message_legth())
my_inbox.clear()
print(my_inbox.message_legth())
