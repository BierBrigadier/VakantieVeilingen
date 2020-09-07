import auction

url = 'https://www.vakantieveilingen.nl/producten/elektronica/bluetooth-draadloos-oordopjes_dutch-originals-wit.html'

while True:
    while not auction.main(url=url):
        print("auction has not ended, restarting...")


