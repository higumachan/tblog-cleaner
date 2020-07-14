from tensorboardX import SummaryWriter

if __name__ == '__main__':
    writer = SummaryWriter("logs/big_log")

    for i in range(10000):
        writer.add_scalar("loss", 100, i)
    writer.close()

    writer = SummaryWriter("logs/small_log")

    for i in range(5):
        writer.add_scalar("loss", 100, i)
    writer.close()
