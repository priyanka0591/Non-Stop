from newspaper import Article
import csv

def scrape_and_save_news(urls, output_file):
    # Create a CSV file for saving the data
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Text', 'Section']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through each URL and scrape the news
        for url in urls:
            article = Article(url)
            article.download()
            article.parse()

            # Write the data to the CSV file
            writer.writerow({'Title': article.title, 'Text': article.text, 'Section': 'Entertainment'})

if __name__ == "__main__":
    # List of news article URLs to scrape
    news_urls = [
'https://www.hindustantimes.com/entertainment/bollywood/tiger-3-box-office-collection-day-11-salman-khan-film-witnesses-dip-101700668327613.html',
'https://www.hindustantimes.com/entertainment/bollywood/ranbir-kapoor-teases-paparazzo-rashmika-mandanna-reacts-when-called-cute-duo-pose-with-finger-hearts-at-animal-event-101700665894610.html',
'https://www.hindustantimes.com/entertainment/music/lana-del-rey-says-shes-absolutely-not-in-love-after-recent-heartbreak-101700663409460.html',
'https://www.hindustantimes.com/entertainment/music/coldplay-concert-in-malaysia-could-be-stopped-via-kill-switch-if-the-band-misbehaves-government-says-101700663024894.html',
'https://www.hindustantimes.com/htcity/cinema/anubhav-singh-bassi-on-comedy-finding-a-place-in-the-market-i-can-afford-big-auditoriums-sell-tickets-at-a-good-price-101700656009647.html',
'https://www.hindustantimes.com/entertainment/anime/return-of-the-kingdom-critically-acclaimed-anime-to-launch-season-5-101700658805564.html',
'https://www.hindustantimes.com/entertainment/bollywood/as-internet-laughs-at-his-liver-description-for-himself-orry-hopes-he-isnt-asked-bhai-tu-karta-kya-hai-again-101700655564037.html',
'https://www.hindustantimes.com/entertainment/telugu-cinema/jyothika-opens-up-about-her-ideal-marriage-it-is-important-to-respect-and-appreciate-your-partner-101700657127269.html',
'https://www.hindustantimes.com/entertainment/tv/taylor-swift-night-on-dancing-with-the-stars-recap-heres-who-went-home-during-week-9-101700649332581.html',
'https://www.hindustantimes.com/entertainment/bollywood/fan-asks-shah-rukh-khan-to-do-bike-stunts-like-tom-cruise-actor-reveals-whats-stopping-him-101700653330660.html',
'https://www.hindustantimes.com/htcity/cinema/rakeysh-omprakash-mehra-approaches-nayanthara-for-karna-to-go-on-floors-in-january-2024-source-101700641202571.html',
'https://www.hindustantimes.com/entertainment/bollywood/bhumi-pednekar-shares-pics-from-hospital-bed-as-she-recovers-from-dengue-101700640342337.html',
'https://www.hindustantimes.com/entertainment/hollywood/from-gal-gadot-to-mia-khalifa-hollywood-celebs-who-were-cancelled-over-remarks-about-israel-hamas-conflict-101700641764467.html',
'https://www.hindustantimes.com/entertainment/bollywood/dunki-drop-2-song-lutt-putt-gaya-shah-rukh-khan-taapsee-pannu-dance-101700634745786.html',
'https://www.hindustantimes.com/entertainment/karan-johar-reveals-how-he-got-hints-about-sidharth-malhotra-and-kiara-advanis-relationship-101700644274583.html',
'https://www.hindustantimes.com/entertainment/anime/where-is-yuta-in-the-jujutsu-kaisen-anime-101700641449462.html',
'https://www.hindustantimes.com/entertainment/telugu-cinema/rashmika-mandanna-teaches-ranbir-kapoor-how-to-talk-in-telugu-while-promoting-animal-watch-101700641446700.html',
'https://www.hindustantimes.com/entertainment/bollywood/tiger-3-worldwide-box-office-collection-day-10-salman-khan-film-crosses-400-crore-mark-katrina-kaif-reacts-101700643944554.html',

    ]

    # Output CSV file name
    output_csv_file = 'Entertainment_data.csv'

    # Scrape and save the news articles
    scrape_and_save_news(news_urls, output_csv_file)