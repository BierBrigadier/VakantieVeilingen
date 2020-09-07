import requests
import csv
from bs4 import BeautifulSoup

bidder = ''
auction = ''
final_bid = ''
time = ''


def get_bid(url):
    global bidder, auction, final_bid, time
    page = requests.get(url, params=None).content
    content = BeautifulSoup(page, features="html.parser")

    winner = content.find('span', {'id': 'highestBidder'}, recursive=True)
    if winner is not None:
        if winner.text.strip('\n, ') == "Nog geen biedingen":
            return False
    bidder = winner.text.strip('\n, ')

    title = content.find('h1', {'id': 'lotTitle'}, recursive=True).text.strip('\n, ')
    auction = title.replace(',', '')

    highest_bid = content.find('span', {'class': 'jsBidAmountUpdate highest-bid'}, recursive=True)
    final_bid = highest_bid.text.strip('\n, ')

    time_of_highest_bid = content.find('span', {'id': 'timeOfHighestBid'}, recursive=True).text.strip('\n, ')
    time = time_of_highest_bid
    return True


def write_auction(auction, final_bid, bidder, time):
    with open('auctions.csv', mode='a+') as auction_file:
        fieldnames = ['auction', 'final_bid', 'bidder', 'time']
        writer = csv.DictWriter(auction_file, fieldnames=fieldnames)
        writer.writerow({'auction': auction, 'final_bid': final_bid, 'bidder': bidder, 'time': time})


def main(url):
    global bidder, auction, final_bid, time
    try:
        while get_bid(url):
            pass
    except:
        pass
    if bidder is not None and bidder != '':
        print("FINAL BID:")
        print(bidder)
        print(auction)
        print(final_bid)
        print(time)
        write_auction(auction, final_bid, bidder, time)
        bidder = ''
        auction = ''
        final_bid = ''
        time = ''
        return True
    else:
        return False


