import scraperwiki

def run_fixtures():
    scraperwiki.sqlite.save_var("recipient", "me@matthewhughes.co.uk")
    scraperwiki.sqlite.save_var("url", "http://example.com")
    scraperwiki.sqlite.save_var("tablename", "swdata")

def main():
    run_fixtures()

if __name__ == '__main__':
    main()
