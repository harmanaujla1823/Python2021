class Order:
    id = 1
    def __init__(self, name, address, price):
        self.oid = Order.id
        self.name = name
        self.address = address
        self.price = price
        Order.id += 1

    def showOrderDetails(self):
        print("{}, {}, {}, {}".format(self.oid, self.name, self.address, self.price))

    def toCSV(self):
        return "{},{},{},{}\n".format(self.oid, self.name, self.address, self.price)

    def saveOrder(self):
        file = open("orders.csv", "a")
        orderData = self.toCSV()
        file.write(orderData)
        file.close()
        print(">> Order[{}] Saved :)".format(self.oid))

    @staticmethod
    def readOrders():
        file = open("orders.csv", "r")
        lines = file.readlines()

        for line in lines:
            data = line.split(",")
            order = Order(data[1], data[2], int(data[3]))
            order.oid = int(data[0])
            order.showOrderDetails()

        file.close()





Order.readOrders()